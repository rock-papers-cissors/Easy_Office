from docx import Document
from docxcompose.composer import Composer
import sys

def mergeDOC(files):
    new_document = Document()
    composer = Composer(new_document)
    for fn in files:
        composer.append(Document(fn))
    composer.save('mergedDOC.docx')

if __name__ == '__main__':
    mergeDOC(sys.argv[1:])
