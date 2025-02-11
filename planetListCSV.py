import csv
import random
from faker import Faker
import os
fake = Faker()

compositions = ['Rocky', 'Gaseous', 'Liquid', 'Frozen', 'Vaporous']
csv_filename = "planets.csv"
file_exists = os.path.exists(csv_filename)
with open(csv_filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["name", "temperature", "gravity", "composition", "habitability"])
    
    for i in range(10):
        name_planet = fake.unique.first_name() 
        temperature = round(random.uniform(-200, 500), 2)
        gravity = round(random.uniform(0.5, 2.5), 2)      
        composition = random.choice(compositions)
        if composition in ('Rocky', 'Liquid') and -50 < temperature < 100 and 0.5 < gravity < 1.5:
            habitability = "Yes"
        else: habitability = "No"
        try:
            writer.writerow([name_planet, temperature, gravity, composition, habitability])
            print(f"Insertado: {name_planet}")
        except Exception as e:
            print(f"Error insertando {name_planet}: {e}")
print(f"Archivo '{csv_filename}' creado con éxito.")