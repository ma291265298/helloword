import PyPDF2

reader1 = PyPDF2.PdfFileReader(open('meetingminutes.pdf', 'rb'))
page1 = reader1.getPage(0)

reader2 = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
page2 = reader2.getPage(0)

page1.mergePage(page2)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page1)
for num in range(1, reader1.numPages):
    pdfWriter.addPage(reader1.getPage(num))
with open('2907.pdf', 'wb') as f:
    pdfWriter.write(f)
