import os
import sys
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from pathlib import Path

from tools import detect_document

# GOOGLE Credentials
user = Path("~").expanduser()
credentials = user / ".config" / "google.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str(credentials)

# Input (either a file or a folder)
input_ = Path(sys.argv[1]).resolve()

if input_.is_file():
    output = detect_document(input_)

if input_.is_dir():
    output = ""
    ext = ['.png', '.jpg', '.jpeg']
    img_list = [i for i in sorted(input_.glob('**/*')) if i.suffix in ext]
    for count, page in enumerate(img_list, start=1):
        output += f"Page {count}\n\n"
        page_content = detect_document(page)
        output += page_content + "\n\n"


# Select all the text in textbox
def select_all(event):
    text_widget.tag_add(tk.SEL, "1.0", tk.END)
    text_widget.mark_set(tk.INSERT, "1.0")
    text_widget.see(tk.INSERT)
    return 'break'

root = tk.Tk()
root.title("Reconnaissance de texte")

text_widget = scrolledtext.ScrolledText(root, width=150)
text_widget.insert(tk.END, output)
text_widget.pack(expand=True, fill='both')

# Add the binding
text_widget.bind("<Control-Key-a>", select_all)
text_widget.bind("<Control-Key-A>", select_all)  # just in case caps lock is on  # noqa: E501

tk.mainloop()
