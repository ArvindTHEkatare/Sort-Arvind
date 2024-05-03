import matplotlib.pyplot as plt

# funktionen heap_sort, koden under kommer att sortera en lista med nummer med hjälp av "heap sort" algoritmen
def heap_sort(arr):
    n = len(arr)

    # bygg en max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extrahera element från heapen ett efter ett
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # byt plats på det största elementet (roten) med det sista elementet
        heapify(arr, i, 0)  # anropa heapify på den reducerade heapen

    return arr  # returnera den sorterade listan


# funktionen heapify, koden under hjälper till att ordna om en del av heapen för att upprätthålla dess egenskap
def heapify(arr, n, i):
    störst = i  # initialisera störst till roten
    l = 2 * i + 1  # vänster = 2*i + 1
    r = 2 * i + 2  # höger = 2*i + 2

    # om vänster barn är större än roten
    if l < n and arr[l] > arr[störst]:
        störst = l

    # om höger barn är större än störst hittills
    if r < n and arr[r] > arr[störst]:
        störst = r

    # byt roten om det behövs
    if störst != i:
        arr[i], arr[störst] = arr[störst], arr[i]  # byt plats

        # utför heapify på roten.
        heapify(arr, n, störst)

        
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

    # Set the overall title
    fig.suptitle(f'Heap sort! :)', fontsize=16)

    #Undvika overlapping av olika diagramsdelar 
    plt.tight_layout()
    
    #print, eller skriva ut diagram
    plt.show()
    