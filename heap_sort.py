#importera de olika moduler som vi kommer använda
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import time 


# funktionen heap_sort sorterar en given lista med nummer med hjälp av "heap sort"-algoritmen.
def heap_sort(arr):
    # längden av arrayen blir till variabeln n.
    n = len(arr)

    # bygger en max-heap genom att heapify varje nod från den sista noden med åtminstone ett barn till roten.
    # iterationen börjar från den sista noden med åtminstone ett barn och går bakåt till roten.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extraherar element från heapen ett efter ett.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # byter plats på det största elementet (roten) med det sista elementet.
        heapify(arr, i, 0)  # anropar heapify på den reducerade heapen.

    return arr  # returnerar den sorterade listan.


# funktionen heapify ordnar om en del av en heap för att upprätthålla dess egenskaper.
def heapify(arr, n, i):
    largest = i  # initialiserar largest till roten.
    vänster = 2 * i + 1  # index för vänster barn.
    höger = 2 * i + 2  # index för höger barn.

    # om vänster barn är större än roten.
    if vänster < n and arr[vänster] > arr[largest]:
        largest = vänster

    # om höger barn är större än störst hittills.
    if höger < n and arr[höger] > arr[largest]:
        largest = höger

    # byter roten om det behövs.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # byter plats.

        # utför heapify på roten.
        heapify(arr, n, largest)  




        
# en funktion för diagram av olika sorts, kommer använda oss av matplotlib
def plot(elements, sorterade_värde, total_tid, graph_type):
   
    #skapa en figur med en given storlek
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    #den första subplotten för den osorterade listan.
    if graph_type == 'Stapel':
        #rita ett stapel diagram för osorterade listan 
        axes[0].bar(range(len(elements)), elements, color='skyblue')
    elif graph_type == 'Linje':
        #rita ett linje diagram för osorterade listan 
        axes[0].plot(range(len(elements)), elements, color='skyblue')
    elif graph_type == 'Punktdiagram':
        #rita ett punkt diagram för osorterade listan 
        axes[0].scatter(range(len(elements)), elements, color='skyblue')
    axes[0].set_title('Osorterad')#titeln
    axes[0].set_xlabel('Index')#vad x axeln indikerar
    axes[0].set_ylabel('Värde')#vad y axeln indikerar

    #den andra subplotten för den sorterade listan. 
    if graph_type == 'Stapel':
        #rita ett stapel diagram för sorterade listan 
        axes[1].bar(range(len(sorterade_värde)), sorterade_värde, color='lightgreen')
    elif graph_type == 'Linje':
        #rita ett linje diagram för sorterade listan 
        axes[1].plot(range(len(sorterade_värde)), sorterade_värde, color='lightgreen')
    elif graph_type == 'Punktdiagram':
        #rita ett punkt diagram för sorterade listan 
        axes[1].scatter(range(len(sorterade_värde)), sorterade_värde, color='lightgreen')
    axes[1].set_title('Sorterad')#titeln
    axes[1].set_xlabel('Index')#vad x axeln indikerar
    axes[1].set_ylabel('Värde')#vad y axeln indikerar

    # Lägg till osorterade och sorterade listor
    axes[0].text(1.02, 0.5, f'Osorterad Lista:\n{elements}', fontsize=16, va='center', transform=axes[0].transAxes)
    axes[1].text(1.02, 0.5, f'Sorterad Lista:\n{sorterade_värde}', fontsize=16, va='center', transform=axes[1].transAxes)

    # titlen
    fig.suptitle(f'Heap sort! :)', fontsize=16)

    #Undvika overlapping av olika diagramsdelar 
    plt.tight_layout()
    
    #print, eller skriva ut diagram
    plt.show()
    