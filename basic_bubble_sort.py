#importera matplotlib.pyplot modulen
import matplotlib.pyplot as plt

#funktionen bubblesort, koden under kommer sortera en lista med nummer på "bubble sort" sättet
def bubblesort(elements):
    # Yttre loop som går igenom listan från slutet till början.
    for n in range(len(elements)-1, 0, -1):
        swapped = False #en sorts indikator som indikerar om byten gjorts under en iteration
        # Mer av en inre loop som går igenom listan från början till näst sista elementet.
        for i in range(n):
            # Jämför varje element med sitt nästa element,  och byt plats på de om de är i fel ordning. (dvs om talen innan är större än talen efteer)
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        
        #om inga byten gjorts, är listan redan sorterad så loopen kan avslutas efter
        if not swapped:
            break  
    return elements  

# en funktion för diagram av olika sorts, kommer använda oss av matplotlib
def plot(elements, sorted_arr):
    #skapa en figur med en given storlek
    plt.figure(figsize=(10, 5))

    #den första subplotten för den osorterade listan. 
    plt.subplot(1, 2, 1)
    plt.bar(range(len(elements)), elements, color='skyblue') #rita ett stapel diagram för osorterade listan 
    plt.title('Osorterad') #titeln
    plt.xlabel('Index') #vad x axeln indikerar
    plt.ylabel('Värde/value') #vad y axeln indikerar

    #den andra subplotten för den sorterade listan.   
    plt.subplot(1, 2, 2)
    plt.bar(range(len(sorted_arr)), sorted_arr, color='lightgreen')#rita ett stapel diagram för sorterade listan 
    plt.title('Sorterad') #titeln
    plt.xlabel('Index') #vad x axeln indikerar
    plt.ylabel('Värde/value') #vad y axeln indikerar

    #Undvika overlapping av olika diagramsdelar
    plt.tight_layout()
    #print, eller skriva ut diagram
    plt.show()
