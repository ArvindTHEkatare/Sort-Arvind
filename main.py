#våra moduler, de som vi kommer använda
import PySimpleGUI as sg
import basic_bubble_sort
import pandas as pd
import time 
import random

#en sorts default tema om vi ändrar inte tema
sg.theme('LightGrey')

tema = ['LightGrey','DarkBrown4', 'DarkGrey', 'LightGreen', 'DarkBlue', 'DarkPurple', 'Tan', 'Topanga', 'SandyBeach', 'Random']

#frågar användaren att välja en av de tema som finns i variabel "tema" eller en random tema som finns i listan
tema_väljaren = [
    [sg.Text('Välj tema:')],
    [sg.Combo(tema, default_value=tema[0], size=(20, 4), key='-tema combo-', enable_events=True, expand_x=True)],
    [sg.Text('Vill du prova en slumpmässig tema kanske?')],
    [sg.Button('Slumpmässigt', key='-random-', expand_x=True)],
    [sg.Button('OK', expand_x=True)]
]

#vad själva windown heter och vi ska spara det som en variabel
fönstret_tema_väljaren = sg.Window('Temaväljaren :)', tema_väljaren)

#while loopen för själva tema väljaren 
while True:
    event, values = fönstret_tema_väljaren.read()
    #om användaren stänger windown eller trycker på OK knappen, valt tema är då values av tema combo
    if event == sg.WINDOW_CLOSED or event == 'OK':
        valt_tema = values['-tema combo-']
        break
    #om användaren väljar random, välj en random tema i listan
    elif event == '-random-':
        valt_tema = random.choice(tema[:-1])
        fönstret_tema_väljaren['-tema combo-'].update(valt_tema)

fönstret_tema_väljaren.close()

if valt_tema == 'Random':
    valt_tema = random.choice(tema[:-1])

#Den valda teman, kommer nu gälla för gui'n under!
sg.theme(valt_tema)

#funktionen som jag bara döpte till gui för att det är basically vad det är
def gui():
    # Hur layouten, dvs verkytygen kommer se ut (just nu kommer den ha 3 knapp, en var man skriver våran lista, en sortera knapp och en exit knapp)
    layout = [
        [sg.Text("Ange en lista med nummer separerade med kommatecken:")],
        [sg.InputText(size=(40, 40), key='-INPUT-')],
        [sg.Button('Sortera', size=(10, 2)), sg.Button('Exit', size=(10, 2))]
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
            #själva hanteraren för elemenets, en för loop finns och vi ska seperera de olika värde med hj+öp av en kommatecken
            elements = [int(x.strip()) for x in inputs.split(',')]
            #här kommer vi använda själva bubblesort algoritm som jag skrev i basic_bubble_sort.py filen.
            if elements:
                #Ska använda en copy av elements, anledningen till denna är att om vi gör inte en copy, de sorterade kommer visa osorterade istället. 
                sorterade_värde = basic_bubble_sort.bubblesort(elements.copy())
                slut_tid = time.perf_counter()  # stoppa timer eller stopwatchen när sortering är klar
                print("Sorting slutade vid:\n", slut_tid)
                total_tid = slut_tid - start_tid #total_tid är så klart slut tid - start tid
                print("Total tid som tagits:\n", total_tid)
                
                
                #frågan användaren om de vill ha en dubbletter av nummer i graphen
                dubletter = sg.popup_yes_no('Vill du ha dubbletter i grafen?', title='Dubbletter')

                #popup up, var man kan välja mellan att ha dubbletter i grafen eller inte 
                if dubletter == 'Yes':
                    # Rita/visa grafen med dubbletter
                    basic_bubble_sort.plot(elements, sorterade_värde, total_tid)
                else:
                    # Ta bort dubbletter med bibehållen ordning
                    unika_sorterade_värden = []
                    #lägger till varje unikt element från sorterade_värde TILL unika_sorterade_värden om det inte redan finns där..
                    [unika_sorterade_värden.append(x) for x in sorterade_värde if x not in unika_sorterade_värden]
                    # Rita/visa grafen utan dubbletter (för sorterade delen)
                    basic_bubble_sort.plot(elements, unika_sorterade_värden, total_tid)


                # Visa tid  i en  popup fönster1
                sg.popup(f'Total tid som behövdes för att sortera är  {total_tid:.6f} sekunder', title='sorterings_tid')

        # Vid en fall var en oförväntade situation tar plats
        else:
            sg.popup_error("Ogiltig input. Skriv in bara nummer, separerade med kommatecken.")


#kör gui funktionen
if __name__ == '__main__':
    gui()
