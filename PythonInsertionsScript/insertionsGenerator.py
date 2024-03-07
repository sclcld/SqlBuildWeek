 # il codice si baserà su una serie di produzioni e selezioni randomiche di valori che verranno correlate 
# tra loro tramite iterazioni su liste e dizionari e l'ultillizzo del modulo random dizionari python. 
# Le liste dalle quali avvengono le scelte sono sta generate in gran parte con chat gpt. 
# Ogni generazione casuale verrà effettuata nell'ambito di range prestabiliti, in modo 
# da provare a garantire la coerenza dei dati

from random import randint, choice
from datetime import date, timedelta

TEL = "123456"

marche = ["BMW", "Audi", "Mercedes", "Toyota"]
colori = ["rosso", "verde", "blu", "giallo", "arancione", "viola", "rosa", "marrone", "grigio", "nero"]
lettere_maiuscole = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cilindrate = [1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
cambi = ["Manuale" ,"Automatico"]
cittaRegPair  = {
    "Roma": "Lazio",
    "Milano": "Lombardia",
    "Napoli": "Campania",
    "Torino": "Piemonte",
    "Palermo": "Sicilia",
    "Genova": "Liguria",
    "Bologna": "Emilia-Romagna",
    "Firenze": "Toscana",
    "Bari": "Puglia",
    "Catania": "Sicilia",
    "Venezia": "Veneto",
    "Verona": "Veneto",
    "Messina": "Sicilia",
    "Padova": "Veneto",
    "Trieste": "Friuli-Venezia Giulia",
    "Brescia": "Lombardia",
    "Taranto": "Puglia",
    "Prato": "Toscana",
    "Modena": "Emilia-Romagna",
    "Reggio Calabria": "Calabria",
    "Reggio Emilia": "Emilia-Romagna",
    "Perugia": "Umbria",
    "Ravenna": "Emilia-Romagna",
    "Livorno": "Toscana",
    "Cagliari": "Sardegna",
    "Foggia": "Puglia",
    "Rimini": "Emilia-Romagna",
    "Salerno": "Campania",
    "Ferrara": "Emilia-Romagna",
    "Sassari": "Sardegna",
    "Latina": "Lazio",
    "Monza": "Lombardia",
    "Siracusa": "Sicilia",
    "Pescara": "Abruzzo",
    "Bergamo": "Lombardia",
    "Forlì": "Emilia-Romagna",
    "Trento": "Trentino-Alto Adige",
    "Vicenza": "Veneto",
    "Terni": "Umbria",
    "Bolzano": "Trentino-Alto Adige",
    "Novara": "Piemonte",
    "Piacenza": "Emilia-Romagna",
    "Ancona": "Marche",
    "Andria": "Puglia",
    "Udine": "Friuli-Venezia Giulia",
    "Cosenza": "Calabria",
    "Sassuolo": "Emilia-Romagna",
    "La Spezia": "Liguria",
    "Trapani": "Sicilia"
}
toponimi = ["Via", "Largo", "Viale", "Piazza"]

personaggi_Italiani= personaggi_italiani = [
    "Leonardo da Vinci", "Marco Polo", "Dante Alighieri", "Michelangelo Buonarroti", "Galileo Galilei",
    "Giuseppe Garibaldi", "Niccolò Machiavelli", "Giotto di Bondone", "Amerigo Vespucci", "Caravaggio",
    "Filippo Brunelleschi", "Alessandro Volta", "Giovanni Boccaccio", "Sandro Botticelli", "Francesco Petrarca",
    "Giovanni Pico della Mirandola", "Luigi Pirandello", "Antonio Vivaldi", "Titian", "Enrico Fermi",
    "Giovanni Bellini", "Niccolò Paganini", "Francesco Redi", "Benvenuto Cellini", "Giacomo Puccini",
    "Raffaello Sanzio", "Torquato Tasso", "Vittorio Emanuele II", "Niccolò Copernico", "Alessandro Manzoni",
    "Gabriele DAnnunzio", "Antonio Canova", "Giovanni Palestrina", "Dante Gabriel Rossetti", "Antonio Allegri da Correggio",
    "Giorgio Vasari", "Ferdinando Magellano", "Luigi Galvani", "Andrea Palladio", "Francesco Hayez",
    "Alessandro Scarlatti", "Ugo Foscolo", "Giovanni Battista Tiepolo", "Piero della Francesca", "Ruggero Boscovich",
    "Alessandro Cagliostro", "Francesco Borromini", "Giovanni Segantini", "Camillo Benso, conte di Cavour", "Gaspare Spontini",
    "Giovanni Battista Piranesi", "Paolo Uccello", "Gaetano Donizetti", "Giovanni Agnelli", "Giovanni Battista Pergolesi",
    "Niccolò Jommelli", "Francesco Maria Grimaldi", "Luigi Boccherini", "Carlo Goldoni", "Tommaso Campanella",
    "Jacopo della Quercia", "Guglielmo Marconi", "Piero di Cosimo", "Giovanni Battista Belzoni", "Giovanni Battista Moroni",
    "Luigi Federico Menabrea", "Giovanni Paolo Panini", "Ignazio Silone", "Giovanni Domenico Cassini", "Alessandro Longhi",
    "Ludovico Ariosto", "Luigi Piranesi", "Lorenzo Ghiberti", "Benedetto Croce", "Giovanni Battista Vico", "Vittorio Alfieri"
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
    "Gallo", "D Amico", "Mazza", "Giuliani", "Rossetti", "Palmieri", "Bernardi", "Martino", "Catalano"
]



targhe = [f"{choice(lettere_maiuscole)}{choice(lettere_maiuscole)}{randint(100, 999)}{choice(lettere_maiuscole)}{choice(lettere_maiuscole)}" for targa in range(1, 1200)]
targhe = list(set(targhe))[:1001]

targhe_index = 0
transazioni_index = 0
id_macchina = list(range(1,1100))
id_deposito = list(range(1,1100))
id_cliente = list(range(1,1100))
records_concessionarie = []
records_auto = []
records_clienti = []
records_deposito = []
records_transazioni = []


for index, filiale in enumerate(list(cittaRegPair.keys()), start=1):

    macchine_per_filiale = targhe[targhe_index : targhe_index + 20]
    indirizzo_filiale = f"{choice(toponimi)} {choice(personaggi_Italiani)} {randint(1,200)}"
    reg = cittaRegPair[filiale]
    nome_responsabile = f"{choice(nomi)} {choice(cognomi)}"
    concessionaria_completo = (index, filiale, indirizzo_filiale, reg, TEL, nome_responsabile)
    records_concessionarie.append(concessionaria_completo)
    for targa in macchine_per_filiale:

        indirizzo_cliente = choice(list(cittaRegPair.keys()))
        regione_c = cittaRegPair[indirizzo_cliente]
        marca = choice(marche)
        prezzo = randint(2000, 40000)
        colore = choice(colori)
        cambio = choice(cambi)
        id_mac = id_macchina.pop(0)
        id_cli = id_cliente.pop(0)
        cilindrata = choice(cilindrate)
        nome_cliente = f"{choice(nomi)}"
        cognome_cliente = f"{choice(cognomi)}"
        auto_completo = (id_mac, marca, targa, colore, cilindrata, cambio, prezzo)
        cliente_completo = (id_cli, nome_cliente, cognome_cliente, indirizzo_cliente, regione_c, TEL)
        records_auto.append(auto_completo)
        records_clienti.append(cliente_completo)
        
    targhe_index += 20
    


for trans_id, aut in enumerate(records_auto, start=1):
    id_client = randint(1,999)
    id_conc = randint(1,50)
    data_ingresso = (date(year=2001, month=1, day=1) + timedelta(days=randint(30,5000)))
    venduta = choice((True, False))
    data_uscita = data_ingresso + timedelta(days=randint(30, 2000)) if venduta else "NULL"
    deposito_completo = (trans_id, id_client, id_conc, str(data_ingresso), str(data_uscita) )
    records_deposito.append(deposito_completo)

record_id = 1

for index, record in enumerate(records_deposito, start = 1):
    rec = record[1:]
    auto, cliente, ingresso, uscita = rec
    acquisizione_completa = (record_id, cliente, auto, ingresso, "Acquisizione", records_auto[index - 1][-1], randint(1,50) )
    record_id += 1
    records_transazioni.append(acquisizione_completa)
    if uscita == "NULL":

        vendita_completa = (record_id, randint(1,1000), auto, ingresso, "Vendita", records_auto[index - 1][-1] + records_auto[index - 1][-1] * 0.2 , randint(1,50))
        record_id += 1
        records_transazioni.append(vendita_completa)



with open("insertions/auto.txt", "a") as file_auto:

    for auto in records_auto:

        a,b,c,d,e,f,g = auto
        to_write =f"({a}, '{b}', '{c}', '{d}', {e}, '{f}', {g}),\n"
        file_auto.write(to_write)


with open("insertions/cliente.txt", "a") as file_clienti:

    for cliente in records_clienti:
        a, b, c, d, e, f = cliente
        to_write =  f"({a},'{b}', '{c}', '{d}', '{e}', {TEL}),\n"
        print(to_write)
        file_clienti.write(to_write)

with open("insertions/concessionaria.txt", "a") as file_concessionaria:

    for concessionaria in records_concessionarie:
        
       a,b,c,d,e,f = concessionaria
       to_write = f"({a}, '{b}', '{c}', '{d}', '{e}', '{f}'),\n"
       file_concessionaria.write(to_write)

with open("insertions/deposito.txt", "a") as file_deposito:

    
    for deposito in records_deposito:
        
        a, b, c, d, e = deposito
        ap = "'" if e != "NULL" else ""
        to_write = f"({a}, {b}, {c}, '{d}', {ap}{e}{ap}),\n"
        file_deposito.write(to_write)    

with open("insertions/transazione.txt", "a") as file_transazione:

    for trans in records_transazioni :

        a, b, c, d, e, f, g = trans
        to_write = f"({a}, {b}, {c}, '{d}', '{e}', {f}, {g}),\n" 
        file_transazione.write(to_write)
    
