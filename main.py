import PyPDF2
import sys

merger = PyPDF2.PdfFileMerger()

if len(sys.argv) > 1:

    p1 = PyPDF2.PdfFileReader(sys.argv[1])
    p2 = PyPDF2.PdfFileReader(sys.argv[2])

    merger.append(p1)
    merger.append(p2)

    merger.write("./output.pdf")

else:

    p1_address = input("> Enter the full path to first pdf file: ")
    p2_address = input("> Enter the full path to second pdf file: ")

    print(p1_address, p2_address)

    p1 = PyPDF2.PdfFileReader(p1_address)
    p2 = PyPDF2.PdfFileReader(p2_address)

    merger.append(p1)
    merger.append(p2)

    merger.write("./output.pdf")