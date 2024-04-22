#import moduler
import PySimpleGUI as sg
import basic_bubble_sort

# skapar funktionen gui
def gui():
    #hur layouten, dvs verkytygen kommer se ut (just nu kommer den ha 3 knapp, en var man skriver våran lista, en sortera knapp och en exit knapp)
    layout = [
        [sg.Text("Ange en lista med nummer separerade med kommatecken:")],
        [sg.InputText(size=(40, 1), key='-INPUT-')],
        [sg.Button('Sortera'), sg.Button('Exit')],
    ]

    #vad själva windown heter eller typ kommer visa
    window = sg.Window("Välkommen till min fina Bubblesort & Matplotlib verktyg! :)", layout)

    #while loop 
    while True:
        event, values = window.read()
        #om vi trycker på exit eller stänger verkytg, sluta programmet
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        #om vi trycker på sortera, sortera listan genom att använda funktionen i basic_bubble_sort.py filen
        elif event == 'Sortera':
            input_str = values['-INPUT-']
            elements = [int(x.strip()) for x in input_str.split(',') if x.strip().isdigit()]
            sorted_arr = basic_bubble_sort.bubblesort(elements.copy())
            basic_bubble_sort.plot(elements, sorted_arr)  
        #Vid en fall var en oförväntade situation tar plats
        else:
            sg.popup_error("Indata innehåller något som inte är ett tal (integer) eller något annat är fel")
            window['-INPUT-'].update('')  

    window.close()

#kör gui funktionen
if __name__ == '__main__':
    gui()
