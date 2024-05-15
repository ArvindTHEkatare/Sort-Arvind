#de olika moduler som vi kommer använda.. vi importerar heap_sort filen som hs
import PySimpleGUI as sg
import heap_sort as hs
import pandas as pd
import time 
import random


# Lista över alla tillgängliga PySimpleGUI-teman
tema = sg.theme_list()

#frågar user/användaren att välja en tema
tema_väljaren_layout = [
    [sg.Text('Välj tema:')],
    #default tema är den första (index 0 för dator.)
    [sg.Combo(tema, default_value=tema[0], size=(20, 4), key='-tema_combo-', enable_events=True, expand_x=True)],
    #frågar användaren om de vill prova en random tema
    [sg.Text('Vill du prova en slumpmässig tema kanske?')],
    [sg.Button('Slumpmässigt', key='-random-', expand_x=True)],
    [sg.Button('OK', expand_x=True)]
]

# Skapa temaväljarfönstret
fönstret_tema_väljaren = sg.Window('Temaväljaren :)', tema_väljaren_layout)

# Händelseloop för själva  temaväljaren 
while True:
    event, values = fönstret_tema_väljaren.read()
    #om användar stänger pop up eller trycker på ok, välja teman som är valt 
    if event == sg.WINDOW_CLOSED or event == 'OK':
        valt_tema = values['-tema_combo-']
        break
    #om användaren väljer random då, välja en random tema 
    elif event == '-random-':
        valt_tema = random.choice(tema)
        fönstret_tema_väljaren['-tema_combo-'].update(valt_tema)
#stäng fönstret, vi behöver inte den efter man väljer teman
fönstret_tema_väljaren.close()

#om användaren väljer   random då, välja en random tema 
if valt_tema == 'Slumpmässigt':
    valt_tema = random.choice(tema)

#den tema som vi valde, kommer gälla för alla popups/windows under!
sg.theme(valt_tema)


# funktionen som jag bara döpte till gui för att det är basically vad det är
def gui():
    # Hur layouten, dvs verkytygen kommer se ut.
    layout = [
        [sg.Text("Ange en lista med nummer separerade med kommatecken:")],
        [sg.InputText(size=(40, 40), key='-INPUT-')],
        #2 knapp, exit för att stänga windown och sortera, för att sortera knappen
        [sg.Button('Sortera', size=(10, 2), expand_x=True), sg.Button('Exit', size=(10, 2), expand_x=True)],
        [sg.Text('Välj typ av graf:')],
        #kan också välja mellan 3 olika typer av grafer, stapel, linje och punkt diagram
        [sg.Combo(['Stapel', 'Linje', 'Punktdiagram'], default_value='Stapel', size=(20, 4), key='-graph-type_combo-', enable_events=True, expand_x=True)]
    ]

    # Vad själva window heter eller typ kommer visa
    window = sg.Window("Välkommen till min fina Heap Sort & Matplotlib verktyg! :)", layout)

    # While loopen för själva gui'n
    while True:
        event, values = window.read()
        # Om vi trycker på exit eller stänger verkytg, sluta programmet
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        # Om vi trycker på sortera, sortera listan genom att använda funktionen i heap_sort.py filen
        elif event == 'Sortera':
            # Input värde sparade som inputs.
            inputs = values['-INPUT-'].strip()
            if inputs:
                #den här if statement, kollar om det finns en input som är inte EN nummer, så det emot bara nummer(integers)
                # kontrollerar om varje element i en kommaseparerad sträng 'inputs' representerar heltal (inklusive negativa heltal).
                # för ett element att anses vara ett heltal måste det antingen vara ett positivt heltal eller ett negativt heltal.
                # använder ett generatoruttryck tillsammans med all() för att kontrollera varje element i listan som genereras genom att splitta 'inputs' vid kommatecken.

                if all(num.lstrip('-').isdigit() or (num.startswith('-') and num[1:].isdigit()) for num in inputs.split(',')):
                    start_tid = time.perf_counter() 
                    print("Sorting började vid:\n", start_tid)
                    # själva hanteraren för elemenets, en för loop finns och vi ska separera de olika värde med hjälp av en kommatecken
                    elements = [int(x.strip()) for x in inputs.split(',')]
                    # här kommer vi använda själva heap sort algoritm som jag skrev i heap_sort.py filen.
                    if elements:
                        # Ska använda en copy av elements, anledningen till denna är att om vi gör inte en copy, de sorterade kommer visa osorterade istället. 
                        sorterade_värde = hs.heap_sort(elements.copy())
                        slut_tid = time.perf_counter()  # stoppa timer eller stopwatchen när sortering är klar
                        print("Sorting slutade vid:\n", slut_tid)
                        total_tid = slut_tid - start_tid  # total_tid är så klart slut tid - start tid
                        print("Total tid som tagits:\n", total_tid)
                        
                        # frågan användaren om de vill ha en dubbletter av nummer i graphen
                        dubbletter = sg.popup_yes_no('Vill du ha dubbletter i grafen?', title='Dubbletter')

                        # popup up, var man kan välja mellan att ha dubbletter i grafen eller inte 
                        if dubbletter == 'Yes':
                            # Rita/visa grafen med dubbletter
                            hs.plot(elements, sorterade_värde, total_tid, values['-graph-type_combo-'])
                        else:
                            # Ta bort dubbletter med bibehållen ordning
                            unik_sorterade_värde = []
                            # lägger till varje unikt element från sorterade_värde TILL unika_sorterade_värden om det inte redan finns där..
                            '''     # loopar igenom varje element 'x' i listan 'sorterade_värde'.
                                    # kontrollerar om elementet 'x' inte redan finns i listan 'unik_sorterade_värde'.
                                    # om villkoret är sant läggs 'x' till i listan 'unik_sorterade_värde' med hjälp av listkomprehension.                                   
'''
                            [unik_sorterade_värde.append(x) for x in sorterade_värde if x not in unik_sorterade_värde]
                            # rita/visa grafen utan dubbletter (för sorterade delen)
                            hs.plot(elements, unik_sorterade_värde, total_tid, values['-graph-type_combo-'])

                        # Visa tid  i en  popup fönster bara upp till 6 decimaltecken
                        sg.popup(f'Total tid som behövdes för att sortera är  {total_tid:.6f} sekunder', title='Sorteringstid')
                #om det finns något som är inte en integer
                else:
                    sg.popup_error("Ogiltig input. Skriv in bara HEL nummer, separerade med kommatecken.")
            #om användaren skriver inte något alls..
            else:
                sg.popup_error("Inget värde angivet. Ange en lista med nummer separerade med kommatecken.")
        # Om en ny graf typ väljs
        elif event == '-graph-type_combo-':
            pass
        # Vid en fall var en oförväntade situation tar plats
        else:
            sg.popup_error("Ogiltig input. Skriv in bara nummer, separerade med kommatecken.")

# kör gui funktionen
if __name__ == '__main__':
    gui()
