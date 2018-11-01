import tkinter
from tkinter import filedialog

from PyPDF2 import PdfFileMerger

root = tkinter.Tk()
filez = filedialog.askopenfilenames(parent=root,title='Choose a file')
filez = sorted(filez)

pdfs = root.tk.splitlist(filez)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))
fname = filedialog.asksaveasfile()

with open(fname.name + ".pdf", 'wb') as fout:
    merger.write(fout)