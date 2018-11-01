from PyPDF2 import PdfFileMerger
import tkinter.filedialog
import tkinter

root = tkinter.Tk()
filez = filedialog.askopenfilenames(parent=root,title='Choose a file')

pdfs = root.tk.splitlist(filez)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('result.pdf', 'wb') as fout:
    merger.write(fout)