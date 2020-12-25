import PySimpleGUI as sg
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse()]]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))
event, values = window.read()