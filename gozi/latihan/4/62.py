import PySimpleGUI as sg
import os.path

file_list_column = [
    [
        sg.Text('Image Folder'),
        sg.In(size=(25, 1), enable_events=True, key='-Folder-'),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key='-file list-'
        )
    ],
]

image_viewer_column = [
    [sg.Text('Choose an image from list on left:')],
    [sg.Text(size=(40, 1), key='-TOUT-')],
    [sg.Image(key='-IMAGE-')],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window('Image Viewer', layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == '-Folder-':
        folder = values['-Folder-']
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        
        fnames = [
            f 
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith(('.png', '.gif', '.jpg', '.jpeg'))
        ]
        window['-file list-'].update(fnames)

    elif event == '-file list-':
        try:
            filename = os.path.join(
                values['-Folder-'], values['-file list-'][0]
            )
            window['-TOUT-'].update(filename)
            
            try:
                window['-IMAGE-'].update(filename=filename)
            except Exception as e:
                print(f'Error updating image: {e}')
        except Exception as e:
            print(f'Error loading selected file: {e}')

window.close()