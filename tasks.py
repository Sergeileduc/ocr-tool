import os
import shutil
import subprocess
from itertools import chain
from pathlib import Path
from platform import uname

from invoke import task

"""'Makefile' equivalent for invoke tool (invoke or inv).
# Installation
`pip install invoke`
# Usage
> inv test
> inv build
etc...
# Autocompletion
For auto completion, just run:
`source <(inv --print-completion-script bash)`
or
`source <(inv --print-completion-script zsh)`
(or add it to ~/.zshrc or ~/.bashrc)
"""


# UTILS -----------------------------------------------------------------------

def get_platform():
    """Check the platform (Windos, Linux, or WSL)."""
    u = uname()
    if u.system == 'Windows':
        return 'windows'
    elif u.system == 'Linux' and 'microsoft' in u.release:
        return 'wsl'
    else:
        return 'linux'


def get_index_path():
    """Get full path for ./htmlcov/index.html file."""
    platform = get_platform()
    if platform == "wsl":
        # TODO: this part with .strip().replace() is ugly...
        process = subprocess.run(['wslpath', '-w', '.'], capture_output=True, text=True)
        pathstr = process.stdout.strip().replace('\\', '/')
        path = Path(pathstr) / 'htmlcov/index.html'
    else:
        path = Path('.').resolve() / 'htmlcov' / 'index.html'
    return path


# TASKS------------------------------------------------------------------------

@task
def lint(c):
    """flake8 - static check for python files"""
    c.run("flake8 .")


@task
def cleantest(c):
    """Clean artifacts like *.pyc, __pycache__, .pytest_cache, etc..."""
    # Find .pyc or .pyo files and delete them
    exclude = ('venv', '.venv')
    p = Path('.')
    genpyc = (i for i in p.glob('**/*.pyc') if not str(i.parent).startswith(exclude))
    genpyo = (i for i in p.glob('**/*.pyo') if not str(i.parent).startswith(exclude))
    artifacts = chain(genpyc, genpyo)
    for art in artifacts:
        os.remove(art)

    # Delete caches folders
    cache1 = (i for i in p.glob('**/__pycache__') if not str(i.parent).startswith(exclude))
    cache2 = (i for i in p.glob('**/.pytest_cache') if not str(i.parent).startswith(exclude))
    cache3 = (i for i in p.glob('**/.mypy_cache') if not str(i.parent).startswith(exclude))
    caches = chain(cache1, cache2, cache3)
    for cache in caches:
        shutil.rmtree(cache)

    # Delete coverage artifacts
    try:
        os.remove('.coverage')
        shutil.rmtree('htmlcov')
    except FileNotFoundError:
        pass


@task
def cleanbuildocr(c):
    """Clean dist/, build/ and egg-info/."""
    exclude = ('venv', '.venv')
    p = Path('.')
    tool = "ocr"
    gen1 = (i for i in p.glob(f'**/dist/{tool}') if not str(i.parent).startswith(exclude))
    gen2 = (i for i in p.glob('**/build') if not str(i.parent).startswith(exclude))
    gen3 = (i for i in p.glob('**/*.egg-info') if not str(i.parent).startswith(exclude))
    builds = chain(gen1, gen2, gen3)
    for b in builds:
        shutil.rmtree(b)
    # Delete pem file
    # Delete coverage artifacts
    try:
        os.remove('roots.pem')
    except FileNotFoundError:
        pass


@task
def cleanbuildoctrad(c):
    """Clean dist/, build/ and egg-info/."""
    exclude = ('venv', '.venv')
    p = Path('.')
    tool = "ocrtrad"
    gen1 = (i for i in p.glob(f'**/dist/{tool}') if not str(i.parent).startswith(exclude))
    gen2 = (i for i in p.glob('**/build') if not str(i.parent).startswith(exclude))
    gen3 = (i for i in p.glob('**/*.egg-info') if not str(i.parent).startswith(exclude))
    builds = chain(gen1, gen2, gen3)
    for b in builds:
        shutil.rmtree(b)
    # Delete pem file
    # Delete coverage artifacts
    try:
        os.remove('roots.pem')
    except FileNotFoundError:
        pass


@task(cleantest, cleanbuildocr)
def cleanocr(c):
    """Equivalent to both cleanbuild and cleantest..."""
    pass


@task(cleantest, cleanbuildoctrad)
def cleanoctrad(c):
    """Equivalent to both cleanbuild and cleantest..."""
    pass


@task(cleantest, cleanbuildocr, cleanbuildoctrad)
def clean(c):
    """Equivalent to both cleanbuild and cleantest..."""
    pass


# @task
# def test(c):
#     """Run tests with pytest."""
#     c.run("pytest tests/")


# @task
# def coverage(c):
#     """Run unit-tests using pytest, with coverage reporting."""
#     # use the browser defined in varenv $BROWSER
#     # in WSL, if not set, example :  export BROWSER='/mnt/c/Program Files/Google/Chrome/Application/chrome.exe'
#     path = get_index_path()
#     c.run('coverage run --source discord/ext/test -m pytest')
#     c.run('coverage report -m')
#     c.run('coverage html')
#     webbrowser.open(path.as_uri())


# @task(cleanbuild)
# def build(c):
#     """pyinstaller build."""
#     c.run('wget -o roots.pem https://raw.githubusercontent.com/grpc/grpc/master/etc/roots.pem',
#           shell='C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe')
#     # c.run('pyinstaller --windowed main.spec')
#     c.run('pyinstaller ocr.spec')

@task(cleanocr)
def buildocr(c):
    """Build with pyinstaller (Windows)"""
    tool = "ocr"
    print("Build with pyinstaller")
    c.run(f"pyinstaller --icon ico.ico --clean --log-level=WARN {tool}.py")  # noqa:E501
    path = Path(__file__).parent
    dist = path / "dist"
    print("cleaning zip")
    zip_ = Path(__file__).parent / "dist" / f"{tool}.zip"
    try:
        os.remove(zip_)
    except FileNotFoundError:
        pass
    print("making a zip")
    shutil.make_archive(dist / tool, "zip", dist, tool)


@task(cleanbuildoctrad)
def buildocrtrad(c):
    """Build with pyinstaller (Windows)"""
    tool = "ocrtrad"
    print("Build with pyinstaller")
    c.run(f"pyinstaller --icon ico.ico --clean --log-level=WARN {tool}.py")  # noqa:E501
    path = Path(__file__).parent
    src = path / ".env.public"
    dist = path / "dist"
    dst = dist / tool / ".env"
    print("copy dist .env")
    shutil.copy(src, dst)
    print("cleaning zip")
    zip_ = Path(__file__).parent / "dist" / f"{tool}.zip"
    try:
        os.remove(zip_)
    except FileNotFoundError:
        pass
    print("making a zip")
    shutil.make_archive(dist / tool, "zip", dist, tool)


@task()
def release(c, version="patch"):
    """Build and release. Optional parameter is "patch (default) / version=minor / version=major"""  # noqa: E501
    c.run(f"bump2version {version}")
    c.run("git push")
    c.run("git push --tags")
