import io
import logging
import os
import re
import sys
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from pathlib import Path

from google.cloud import vision
from tqdm import tqdm

__version__ = "0.1.1"

LINE_BREAKS_PATTERN = r"([\w\s,])(?:\n)"
FIRST_WORD = re.compile(r'((?<=[\.\?!]\s)(\w+)|(?<=\")(\w+)|(^\w+))', flags=re.MULTILINE)  # noqa: E501

logger = logging.getLogger(__name__)


def no_ext(filename):
    return os.path.splitext(filename)[0]


def remove_dummy_line_breaks(longstring):
    # rstrip because last line break becomes
    return re.sub(LINE_BREAKS_PATTERN, r"\1 ", longstring).rstrip()


def remove_multiple_spaces(longstring):
    return re.sub(r" +", " ", longstring, flags=re.MULTILINE)


def cap(match):
    return (match.group().capitalize())


# def sentence_case(text):
#     # Split into sentences. Therefore, find all text that ends
#     # with punctuation followed by white space or end of string.
#     sentences = re.findall(r'[^.!?]+[.!?](?:\s|\Z)', text)

#     # Capitalize the first letter of each sentence
#     sentences = [x[0].upper() + x[1:] for x in sentences]

#     # Combine sentences
#     return ''.join(sentences)


def sentence_case(text):
    return FIRST_WORD.sub(cap, text)


def detect_document(path):
    """Detect document features in an image."""

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)  # pylint: disable=no-member  # noqa: E501
    texts = response.text_annotations

    if texts:
        page = texts[0].description.lower()

        # Remove dummy line breaks
        page = remove_dummy_line_breaks(page)
        logger.debug("DUMMY LINE BREAKS :\n%s", page)

        # Remove double sapces
        page = remove_multiple_spaces(page)
        logger.debug("DOUBLE SPACES :\n%s", page)

        # Capitalize sentences
        page = sentence_case(page)
        logger.debug("SENTENCE CASES :\n%s", page)

        return page
    else:
        return ""


# Select all the text in textbox
def select_all(event):
    text_widget.tag_add(tk.SEL, "1.0", tk.END)
    text_widget.mark_set(tk.INSERT, "1.0")
    text_widget.see(tk.INSERT)
    return 'break'


# GOOGLE Credentials
user = Path("~").expanduser()
credentials = user / ".config" / "google.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str(credentials)

# Input (either a file or a folder)
input_ = Path(sys.argv[1]).resolve()

print(f"Le programme va traiter le fichier/dossier : {str(input_)}")


try:
    if input_.is_file():
        if input_.suffix.lower() in ['.cbz' '.cbr', '.cbz']:
            print("Le programme ne traite que des fichiers individuels (jpg, etc...) ou des dossiers.\n"
                  "Pas les archives .cbz ou .cbr")
            input("Appuyer sur une touche pour quitter.")
            sys.exit()
        else:
            print("Détection d'un fichier")
            output = detect_document(input_)

    elif input_.is_dir():
        print("Détection d'un dossier.")
        output = ""
        ext = ['.png', '.jpg', '.jpeg', '.webp']
        img_list = [i for i in sorted(input_.glob('**/*')) if i.suffix.lower() in ext]  # noqa: E501
        for count, page in enumerate(tqdm(img_list), start=1):
            output += f"Page {count}\n\n"
            page_content = detect_document(page)
            output += page_content + "\n\n"
    else:
        print(f"Erreur avec l'input suivante : {str(input_)}")
        sys.exit()

    root = tk.Tk()
    root.title("Reconnaissance de texte")

    text_widget = scrolledtext.ScrolledText(root, width=150)
    text_widget.insert(tk.END, output)
    text_widget.pack(expand=True, fill='both')

    # Add the binding
    text_widget.bind("<Control-Key-a>", select_all)
    text_widget.bind("<Control-Key-A>", select_all)  # just in case caps lock is on  # noqa: E501

    tk.mainloop()
except Exception as e:
    print(e)
    input("Appuyer sur une touche pour quitter")
