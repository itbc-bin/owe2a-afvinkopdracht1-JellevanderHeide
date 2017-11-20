def main():
    bestand = "enzymen.txt"
    '''
    omschrijving: stopt het programma als er te veel waarden zijn om te splitsen
    verwacht resultaat: programma stopt wanneer er te veel waarden zijn
    pass/fail: pass
    opmerkingen: werkt prima, weet niet of het ook werkt met te weinig waarden
    '''
    try:
        headers, seq = lees_inhoud(bestand) #voeg hier een waarde aan toe om te testen
    except ValueError:
        print(' je kan dit bestand niet opdelen op de manier die je aangegeven hebt')
        errorJa()
    woord = input('welk woord zoek je?')                                    #vraag om een woord
    nummer = -1                                                             #zet nummer op -1                                               
    for i in headers:                                                       #loop door de sequentie
        nummer += 1                                                         #verhoog nummer met 1
        if woord in headers[nummer]:                                        #als woord voorkomt in de header bij het huidige nummer...
            sequentieNummer = nummer                                        #sequentieNummer krijgt dezelfde waarde als nummer 
            jaNee, seqNummer = is_dna(seq, sequentieNummer, headers)        
            if jaNee == True:                                               #als jaNee waar is...
                '''
                omschrijving:verkeerde parameters opgeven
                verwacht resultaat: programma stopt als het programma de functie aanroept
                pass/fail: pass
                opmerkingen: het programma wordt netjes stopgezet
                '''
                try:
                    knipt(seq, seqNummer)
                except TypeError:
                    print('\nje parameters kloppen niet')
                    errorJa()


def lees_inhoud(bestand):                                       #DEZE FUNCTIE WERKT CORRECT.

    '''
    omschrijving: niet bestaand bestand openen
    verwacht resultaat: programma geeft een error als het bestand niet in de directory staat
    pass/fail: pass
    opmerkingen: het bestand bestaat niet, dus het programma stopt met uitvoeren
    '''
    
    try:                                #probeer of dit werkt
        bestand = open("alpaca.fa")     #(alpaca.fa = [willekeurig] voor error)
    except FileNotFoundError:           #anders, doe dit...
        print('het bestand dat je hebt ingevuld bestaat niet in deze directory', '\n', '-'*70)
        errorJa()
    stringTestobject = "woord"    
    headers = []
    seqs = []
    newLine = 0                                                 #newLine wordt gebruikt om te kijken of de sequentie is afgelopen bij het samenvoegen
    seqSamen = ''                                               #hier komt de samengestelde sequentie in te staan

    '''
    omschrijving: het bestand is een string?
    verwacht resultaat: de error wordt netjes afgehandeld en het programma stopt
    pass/fail: pass
    opmerkingen: het bestand is een string, dus het programma stopt
    '''  
    try:
        for line in bestand.readlines():                            #loop door het bestand  (bestand = stringTestobject voor error)
            line = line.rstrip()
            if line[0] =='>':                                       #als er een > staat aan het begin van de line is het een header dus...
                headers.append(line)                                #voeg de header toe aan de 'headers' lijst
                newLine = 1                                         #newLine wordt hier op 1 gezet om aan te geven dat er een nieuwe sequentie aankomt
            else:
                if newLine == 0:                                    #is newLine 0...
                    seqSamen = seqSamen + line                      #dan is er geen nieuwe header geweest en kan dit deel toegevoegd worden aan de samenstelling
                else:                                               #anders...
                    newLine = 0                                     #zet newLine op 0 om aan te geven dat er een nieuwe samenstelling wordt gestart
                    if seqSamen != '':                              #is seqSamen niet leeg...
                        seqs.append(seqSamen)                       #voeg gemaakte seq toe aan de lijst
                    seqSamen = ''                                   #maak seq weer leeg om een nieuwe te kunnen gaan samenstellen
                    seqSamen = seqSamen + line                      #voeg de huidige line toe aan de samenstelling
        seqs.append(seqSamen)                                       #voeg de laatste sequentie toe aan de lijst
#    print(headers[35570])                                      voor testen
#    print(seqs[35570])
#    print(len(headers))
#    print(len(seqs))
    except AttributeError:
        print('dit object is een String en deze kan niet gebruikt worden door de Readlines \nfunctie','\n','-'*70)
        errorJa()
    return headers, seqs
   
def is_dna(seq, sequentieNummer, headers):                                                          #DEZE FUNCTIE WERKT CORRECT                                         
    print('-'*60, '\n', headers[sequentieNummer], '\n', '-'*60)                                 
    print(sequentieNummer)
    C = seq[sequentieNummer].count('C')                                                             #tel het aantal C
    A = seq[sequentieNummer].count('A')                                                             #tel het aantal A
    T = seq[sequentieNummer].count('T')                                                             #tel het aantal T
    G = seq[sequentieNummer].count('G')                                                             #tel het aantal G
    CTAG = C + A + T + G                                                                            #tel het aantal C, G, T en A bij elkaar op
    totaleLengte = len(seq[sequentieNummer])                                                        #tel hoe lang de sequentie is
    print('deze sequentie is: ', totaleLengte, ' lang waarvan: ', CTAG, 'C, A, T en G zijn')        
    if totaleLengte == CTAG:                                                                        #zijn de lengtes gelijk...
        print('dit is DNA')
        print('-'*60)
        return True, sequentieNummer
    else:                                                                                           #zijn de lengtes ongelijk...
        print('dit is geen DNA')
        return False, sequentieNummer

def knipt(seq, seqNummer):    #voer hier een extra niet bestaande parameter in voor test                                                                      #DEZE FUNCTIE WERKT CORRECT
    enzymenLijst = open('enzymen.txt')                                                                                                                            
    for line in enzymenLijst.readlines():                                                           #loop door de enzymenlijst
        enzym, fileSeq = line.split()                                                               #zet de enzymnaam en de bijhorende sequentie los van elkaar
        fileSeq = fileSeq.replace('^', '')                                                          #haal het dakje uit de sequentie
        if fileSeq in  seq[seqNummer]:                                                              #als de seq van het enzym in de sequentie zit...
            print ('het enzym: ', enzym, ' met sequentie: ', fileSeq, ' knipt in de sequentie')     
        else:                                                                                       #anders
            print ('het enzym: ', enzym, ' met sequentie: ', fileSeq, ' knipt niet in de sequentie')

def errorJa():
    print ('\n\n er is een fout opgetreden, pas je code aan en run deze opnieuw. \n ----P R O G R A M  E N D E D---- ')
    exit()                                                                                         #stop het programma
'''
omschrijving: programma wordt onderbroken
verwacht resultaat: programma stopt gelijk, 
pass/fail: pass
opmerkingen: het programma stopt gelijk
'''
try:
    main()
except KeyboardInterrupt:
    print('\n\n je programma is onderbroken')
    errorJa()

