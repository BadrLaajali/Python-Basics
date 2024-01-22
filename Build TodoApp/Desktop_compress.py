import PySimpleGUI as sg
import zipfile
import os

def compress_files(source_folder, destination_folder):
    try:
        zip_filename = os.path.join(destination_folder, "compressed_files.zip")
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, source_folder)
                    zipf.write(file_path, relative_path)
        sg.popup("Compression successful!", "The files have been compressed.", title="Success")
    except Exception as e:
        sg.popup_error(f"Error: {str(e)}", title="Error")

layout = [
    [sg.Text("Select files to compress:")],
    [sg.Input(tooltip="Select your files to compress", key='-SOURCE-'), sg.FilesBrowse("Choose")],
    [sg.Text("Select destination folder:")],
    [sg.Input(tooltip="Select your destination", key='-DESTINATION-'), sg.FolderBrowse("Choose")],
    [sg.Button("Compress")]
]

window = sg.Window('File Zipper', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Compress":
        source_folder = values['-SOURCE-']
        destination_folder = values['-DESTINATION-']
        if source_folder and destination_folder:
            compress_files(source_folder, destination_folder)

window.close()
