#importera de olika moduler som vi kommer använda
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import time 


#funktionen bubblesort, koden under kommer sortera en lista med nummer på "bubble sort" sättet
def bubblesort(elements):
    # Yttre loop som går igenom listan från slutet till början.
    for n in range(len(elements)-1, 0, -1):
        byta = False #en sorts indikator som indikerar om byten gjorts under en iterationen
        # Mer av en inre loop som går igenom listan från början till näst sista elementet.
        for i in range(n):
            # Jämför varje element med sitt nästa element,  och byt plats på de om de är i fel ordning. (dvs om talen innan är större än talen efteer)
            if elements[i] > elements[i + 1]:
                byta = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

        #om inga byten gjorts, är listan redan sorterad så loopen kan avslutas efter
        if not byta:
            break  
    return elements  

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

    # titeln 
    fig.suptitle(f'Heap sort! :)', fontsize=16)

    #Undvika overlapping av olika diagramsdelar 
    plt.tight_layout()
    
    #print, eller skriva ut diagram
    plt.show()
    

