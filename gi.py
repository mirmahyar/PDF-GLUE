import PySimpleGUI as sg


sg.theme('Light Blue 3')
layout = [
            [sg.Text("Welcome to Pdf Glue. Select your files below...")],
          [sg.Text("Choose first pdf file: "), sg.Input(key="-IN-"), sg.FileBrowse()],
          [sg.Text("Choose second pdf file: "), sg.Input(key="-IN-0"), sg.FileBrowse()],
          [sg.Button("Submit")]
          ]
window=sg.Window('Pdf Glue',layout,size=(800,400))



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])
        print(values["-IN-0"])