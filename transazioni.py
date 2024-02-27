import csv
import random
from datetime import datetime, timedelta

# Funzione per generare una data casuale tra due date specificate
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Apertura del file CSV in modalità scrittura
with open('transazioni.csv', 'w', newline='') as csvfile:
    fieldnames = ['cliente_id', 'auto_id', 'data', 'tipo', 'prezzo', 'concessionaria_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Scrittura dell'intestazione del file CSV
    writer.writeheader()

    # Generazione delle righe
    for _ in range(1200):  # Modifica questo valore al numero desiderato di righe
        cliente_id = random.randint(1, 100)
        auto_id = random.randint(1, 1000)
        data = random_date(datetime(2005, 1, 1), datetime.now())
        tipo = random.choice(['ACQUISTO', 'VENDITA'])
        prezzo = random.randint(20000, 50000)
        concessionaria_id = random.randint(1, 50)
        writer.writerow({'cliente_id': cliente_id, 'auto_id': auto_id, 'data': data.strftime('%Y-%m-%d'),
                         'tipo': tipo, 'prezzo': prezzo, 'concessionaria_id': concessionaria_id})

print("Generazione completata. Il file 'transazioni.csv' è stato creato.")
