import PySimpleGUI as sg

sg.theme('DarkPurple2')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Я ChatBot! Напишите (команды) для подробностей.')],
            [sg.Text('Спросите что угодно (выкл - выключить)'), sg.InputText()],
            [sg.Button('Send'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('ChatBot', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()