 # il codice si baserà su una serie di produzioni e selezioni randomiche di valori che verranno correlate 
#tra loro tramite dizionari python. Le liste dalle quali avvengono le scelte sono sta generate in gran parte con 
#chat gpt. 
#ci sono tante migliorie da effettuare, ma il tempo è tiranno.

from random import randint, choice, shuffle
from datetime import date, timedelta

TEL = "123456"

#le macchine verranno generate da una combinazione randomica dei seguenti valori
marche = ["BMW", "Audi", "Mercedes", "Toyota"]
colori = ["rosso", "verde", "blu", "giallo", "arancione", "viola", "rosa", "marrone", "grigio", "nero"]
lettere_maiuscole = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cilindrate = ["1.2L", "1.6L", "2.0L", "2.5L", "3.0L", "3.5L", "4.0L", "4.5L", "5.0L", "5.5L"]
cambio = ["Manuale", "Automatico"]
data_inizio = "2010-01-01"
citta_italiane = ["Milano", "Roma", "Napoli", "Torino", "Palermo", "Genova", "Bologna", "Firenze", "Bari", "Catania",
                  "Venezia", "Verona", "Messina", "Padova", "Trieste", "Brescia", "Parma", "Taranto", "Prato", "Modena",
                  "Reggio Calabria", "Reggio Emilia", "Perugia", "Livorno", "Cagliari", "Forlì", "Ravenna", "Rimini",
                  "Foggia", "Salerno"]
toponom = ["Via", "Largo", "Viale", "Piazza"]
personaggi_Italiani= [
    "Luigi Cadorna", "Aldo Finzi", "Alcide De Gasperi", "Andrea Graziani", "Antonio Gramsci", "Antonio Locatelli",
    "Carlo Pecorini", "Carlo Sforza", "Emanuele Filiberto di Savoia-Aosta", "Emilio De Bono", "Enrico Caviglia",
    "Enrico Tellini", "Francesco Baracca", "Francesco Saverio Grazioli", "Giovanni Battista Agnese", "Giovanni Boano",
    "Giovanni Pascoli", "Giuseppe Giardino", "Giuseppe Melchiorre Serrati", "Guido Keller", "Guido Podrecca",
    "Ippolito Nievo", "Luigi Facta", "Luigi Rizzo", "Luigi Sturzo", "Luigi Tosti", "Luigi Volpicelli",
    "Orazio Giustiniani", "Paolo Emiliani Giudici", "Pietro Badoglio", "Pietro Frugoni", "Renato Cialente",
    "Ruggero Ricciardi", "Umberto Biancamano", "Umberto Cagni", "Umberto Marzotto", "Umberto Nobile", "Vittorio Emanuele III",
    "Silvio Berlusconi", "Aldo Moro", "Enrico Berlinguer", "Giulio Andreotti", "Bettino Craxi", "Palmiro Togliatti",
    "Giovanni Leone", "Giuliano Amato", "Franco Frattini", "Gianfranco Fini", "Emma Bonino", "Ciriaco De Mita",
    "Giuseppe Saragat", "Romano Prodi", "Giorgio Napolitano", "Giuseppe Garibaldi II", "Alcide De Gasperi",
    "Antonio Di Pietro", "Rita Levi-Montalcini", "Massimo D'Alema", "Carlo Azeglio Ciampi", "Giorgio Almirante",
    "Giulietto Chiesa", "Giovanni Falcone", "Paolo Borsellino", "Enrico Mattei", "Giorgio La Pira", "Aldo Aniasi"
]
nomi = [
    "Luca", "Andrea", "Matteo", "Giovanni", "Davide", "Alessandro", "Gabriele", "Lorenzo", "Simone", "Francesco",
    "Marco", "Riccardo", "Filippo", "Federico", "Antonio", "Alberto", "Stefano", "Mario", "Paolo", "Giacomo",
    "Giuseppe", "Alessio", "Christian", "Enrico", "Raffaele", "Leonardo", "Michele", "Daniele", "Emanuele",
    "Fabio", "Luigi", "Salvatore", "Roberto", "Vincenzo", "Claudio", "Ivan", "Diego", "Gianluca", "Giacomo",
    "Nicola", "Domenico", "Pietro", "Samuele", "Angelo", "Dario", "Cristian", "Massimo", "Rocco", "Giorgio",
    "Salvatore", "Tommaso", "Gabriele", "Luca", "Alberto", "Enzo",
    "Giulia", "Sofia", "Alice", "Giorgia", "Martina", "Francesca", "Alessia", "Elena", "Elisa", "Chiara",
    "Emma", "Ludovica", "Valentina", "Roberta", "Anna", "Laura", "Giovanna", "Veronica", "Silvia", "Maria",
    "Caterina", "Federica", "Marta", "Nicole", "Simona", "Eleonora", "Rosa", "Teresa", "Stefania", "Beatrice",
    "Noemi", "Aurora", "Eva", "Lucia", "Elisabetta", "Angelica", "Camilla", "Sabrina", "Serena", "Isabella",
    "Sara", "Vittoria", "Miriam", "Carla", "Ginevra", "Linda", "Lara", "Irene", "Mara", "Amanda", "Cinzia",
    "Giada", "Cristina", "Daniela", "Michela", "Eleonora", "Clara", "Rita", "Arianna", "Emma"
]
cognomi = [
    "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco",
    "Bruno", "Gallo", "Conti", "De Luca", "Mancini", "Costa", "Giordano", "Rizzo", "Lombardi", "Moretti",
    "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone",
    "Longo", "Gentile", "Martinelli", "Vitale", "Lombardo", "Serra", "Coppola", "De Santis", "Paris", "Fiore",
    "De Angelis", "Marchetti", "De Rosa", "Coppola", "Pellegrini", "Palumbo", "Sorrentino", "Amato", "De Filippo",
    "De Luca", "Pellegrino", "Caputo", "Villa", "Conte", "Ferri", "Fabbri", "Cattaneo", "Morelli", "Grasso",
    "Gallo", "D'Amico", "Mazza", "Giuliani", "Rossetti", "Palmieri", "Bernardi", "Martino", "Catalano"
]

#mentre il numero di telefono sarà un valore di default, la targa è unica e viene generata uniccombinando lettere ed un numero
#da 100 a 999. Creo una lista e la ripulisco dai duplicati convertendola in set prima di riconvertirla in lista
targhe = [f"{choice(lettere_maiuscole)}{choice(lettere_maiuscole)}{randint(100, 999)}{choice(lettere_maiuscole)}{choice(lettere_maiuscole)}" for numero_targhe in range(1000)]
targhe = list(set(targhe))

#creo un dizionario macchina : prezzo in modo da avere coerenza nei record successivi
prezzi = {}
macchine = []
for x in range(1,1001):

    marca = choice(marche)
    targa = choice(targhe)
    colore = choice(colori)
    cil = choice(cilindrate)
    camb = choice(cambio)
    prezzo = randint(10000, 80000)
    macchina = f"({x}, '{marca}', '{targa}', '{colore}', '{cil}', '{camb}', '{prezzo}'),"
    macchine.append(macchina)
    prezzi[x] = prezzo

#FILIALI
    
#viene combinata una citta, un'indicazione toponomastica, un personaggio italiano a caso(avevo chiesto 
# a chat gpt solo personaggi italiani deceduti e lui di tutta risposta ha inserito nella lista Massimo D'Alema e 
#Gianfranco Fini) un numero civico, il valore TEL ed un nome
    
filiali = []    
for x in range(1,51):

    citta = citta_italiane[x % 30]
    indirizzo = f"{choice(toponom)} {choice(personaggi_Italiani)} {randint(1,120)}"
    responsabile = f"{choice(nomi)} {choice(cognomi)}"
    filiali.append(f"('{x}', '{citta}', '{indirizzo}', '{TEL}', '{responsabile}'),")

#CLIENTI 
#il processo di creazione dei clienti avviene più o meno nello stesso modo del precedente
clienti= []    
for x in range(1, 601):

    nome = choice(nomi)
    cognome = choice(cognomi)
    indirizzo = f"{choice(toponom)} {choice(personaggi_Italiani)} {randint(1,120)}"
    cliente = f"({x}, '{nome}', '{cognome}', '{indirizzo}', '{TEL}'),"
    clienti.append(cliente)


#deposito
#deposito combina due id che rientrano nei range necessari e genera una data di entrata ed una eventuale data di uscita
#la data di entrata viene selezionata casualmente in una lista(range) di date, la data d'uscita verrà generata (quando
#non NULL) aggiungendo da 30 a 600 giorni alla data iniziale.
#per creare anche la tabella delle transazioni cercando di mantenere un minimo di coerenza nel dato(anche se in un modo 
#un po' naive e ancora da testare), prende spunto esattamente dalla crezione delle date, la data di ingresso corrisponderà 
#ad una transazione di "acquisizione", la data di uscita corrisponderà(se not NULL) ad una transazione di vendita 
deposito = []
transazioni = []


for x in range(1, 1100):

    cliente = x % 300
    cliente = 1 if cliente == 0 else cliente
    macchina = x % 1000
    macchina = 1 if macchina == 0 else macchina
    concessionaria = x % 50
    delta_to_add = timedelta(days = randint(30, 600))
    start = date(2009, 1, 1)
    ingresso = start + delta_to_add
    uscita = ingresso + delta_to_add if x == 300 else choice(("NULL", ingresso + delta_to_add))
    dep = f"('{cliente}', '{macchina}', '{ingresso}', '{uscita}'),"
    deposito.append(dep)
    
    transazioni.append(f"('{cliente}', '{macchina}', '{str(ingresso)}', 'acquisizione', '{prezzi[macchina]}')")
    if uscita:
        transazioni.append(f"('{cliente}', '{macchina}', '{str(uscita)}', 'vendita', '{prezzi[macchina]}')")




#con with open genero dei file che sono perfettamente formattati per essere direttamente incollati nell'insertion
# sullo script di sql e funzioneranno. Basta solo levare la virgola dopo l'ultimo record di ogni tabella :)        
with open("insertions/auto.txt", "a") as file_auto:

    for car in macchine:

        file_auto.write(car + "\n")

with open("insertions/clienti.txt", "a") as file_clienti:

    for customer in clienti:

        file_clienti.write(customer + "\n")

with open("insertions/concessionarie.txt", "a") as file_concessionarie:

    for fil in filiali:

        file_concessionarie.write(fil + "\n")

with open("insertions/deposito.txt", "a") as file_deposito:

    for dep in deposito:

        file_deposito.write(dep + "\n")

with open("insertions/tansazioni.txt", "a") as file_transazioni:

    for transazione in transazioni:

        file_transazioni.write(transazione + "\n")



