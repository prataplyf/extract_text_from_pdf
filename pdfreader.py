# import libraries
from PyPDF2 import PdfFileReader
# open pdf file from location
file = open("ncertbook.pdf", 'rb')
# read pdf file
reader = PdfFileReader(file)
print("printing the document file...\n",(reader.getDocumentInfo()))
print("\n number of pages:",reader.getNumPages())

print("pdf created by: ", reader.getDocumentInfo().creator)

pages = reader.getNumPages()
for i in range(0, pages):
    print("page number: ", i+1)
    pageObj = reader.getPage(i)
    print(pageObj.extractText())

file.close()