import os
import os.path
import PyPDF2


def getFileName(filepath):
    file_list = []
    for root, dirs, files in os.walk(filepath):
        for filespath in files:
            file_list.append(os.path.join(root, filespath))
    return file_list


file_dir = 'pythonPDF/'
pdf_fileName = getFileName(file_dir)
flag = 0
pdfWriter = PyPDF2.PdfFileWriter()
for each in pdf_fileName:
    flag += 1
    reader = PyPDF2.PdfFileReader(open(each, 'rb'))
    if flag == 1:
        pdfWriter.addPage(reader.getPage(0))
    for i in range(2, reader.numPages):
        pdfWriter.addPage(reader.getPage(i))
with open('2908.pdf', 'wb') as f:
    pdfWriter.write(f)
