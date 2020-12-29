import PyPDF2
import os
import re
import sys

def mergePDF(files):
    print(files)
    opened_file = [open(filename, 'rb') for filename in files]
    pdfFM = PyPDF2.PdfFileMerger()
    for f in opened_file:
        pdfFM.append(f)

    with open('merged.pdf', 'wb') as write_out_file:
        pdfFM.write(write_out_file)

    for f in opened_file:
        f.close()


if __name__ == '__main__':
    mergePDF(sys.argv[1:]) 
