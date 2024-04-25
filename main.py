#import moduler
import PySimpleGUI as sg
import basic_bubble_sort
import pandas as pd
import time 

#funktionen som jag bara döpte till gui för att det är basically vad det är
def gui():
    # Hur layouten, dvs verkytygen kommer se ut (just nu kommer den ha 3 knapp, en var man skriver våran lista, en sortera knapp och en exit knapp)
    layout = [
        [sg.Text("Ange en lista med nummer separerade med kommatecken:")],
        [sg.InputText(size=(40, 40), key='-INPUT-')],
        [sg.Button('Sortera'), sg.Button('Exit')],
    ]

    # Vad själva window heter eller typ kommer visa
    window = sg.Window("Välkommen till min fina Bubblesort & Matplotlib verktyg! :)", layout)

    #While loopen för själva gui'n
    while True:
        event, values = window.read()
        # Om vi trycker på exit eller stänger verkytg, sluta programmet
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        # Om vi trycker på sortera, sortera listan genom att använda funktionen i basic_bubble_sort.py filen
        elif event == 'Sortera':
            #börja stopwatch eller typ "timer" när "Sortera" knappen trycks
            #använder en inbyggd funktion speciell till time modulen
            start_tid = time.perf_counter() 
            print("Sorting började vid:\n", start_tid)
            # Input värde sparade som inputs.
            inputs = values['-INPUT-']
            elements = [int(x.strip()) for x in inputs.split(',') if x.strip().isdigit()]
            #
            if elements:
                sorterade_värde = basic_bubble_sort.bubblesort(elements.copy())
                slut_tid = time.perf_counter()  # stoppa timer eller stopwatchen när sortering är klar
                print("Sorting slutade vid:\n", slut_tid)
                total_tid = slut_tid - start_tid #total_tid är så klart slut tid - start tid
                print("Total tid som tagits:\n", total_tid)

                # Visa tid  i en  popup fönster
                sg.popup(f'Total tid som tagits: {total_tid:.6f} sekunder', title='sorterings_tid')

                # Rita graferna tillsammans med tiden som krävs för sortering EFTER att du har tryckt på knappen.
                basic_bubble_sort.plot(elements, sorterade_värde, total_tid)

        # Vid en fall var en oförväntade situation tar plats
        else:
            sg.popup_error("Ogiltig input. Skriv in bara nummer, separerade med kommatecken.")


#kör gui funktionen
if __name__ == '__main__':
    gui()
