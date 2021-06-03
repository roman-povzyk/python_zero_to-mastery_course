import PyPDF2

with open('213_dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))
