import PySimpleGUI as sg
import PyPDF2
import sys


sg.theme('Light Blue 3')
layout = [
            [sg.Text("Welcome to Pdf Glue. Select your files below...")],
          [sg.Text("Choose first pdf file: "), sg.Input(key="-IN-"), sg.FileBrowse()],
          [sg.Text("Choose second pdf file: "), sg.Input(key="-IN-0"), sg.FileBrowse()],
          [sg.Text("Choose destination folder: "), sg.Input(key="-IN-1"), sg.FolderBrowse()],
          [sg.Button("Submit")]
          ]
window=sg.Window('Pdf Glue',layout,size=(800,400))



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        file1=values["-IN-"]
        file2=values["-IN-0"]
        destination=values["-IN-1"]

        merger = PyPDF2.PdfFileMerger()
        p1 = PyPDF2.PdfFileReader(file1)
        p2 = PyPDF2.PdfFileReader(file2)

        merger.append(p1)
        merger.append(p2)

        merger.write(destination + "/output.pdf") 
                





'''
# Has the user entered any pdf files as arguments?
if len(sys.argv) > 1:

    p1 = PyPDF2.PdfFileReader(sys.argv[1])
    p2 = PyPDF2.PdfFileReader(sys.argv[2])

    merger.append(p1)
    merger.append(p2)

    merger.write("./output.pdf") '''




