import os
import random
from dotenv import load_dotenv
import psycopg2
from faker import Faker


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("No se encontró la variable DATABASE_URL en el archivo .env")

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Conexión exitosa")
except Exception as e:
    raise Exception(f"Error al conectar con la base de datos: {e}")

fake = Faker()

compositions = ['Rocky', 'Gaseous', 'Liquid', 'Frozen', 'Vaporous']
cursor = conn.cursor()


for i in range(10):
    name_planet = fake.unique.first_name() 
    temperature = round(random.uniform(-200, 500), 2)
    gravity = round(random.uniform(0.5, 2.5), 2)      
    composition = random.choice(compositions)
    if composition in ('Rocky', 'Liquid') and -50 < temperature < 100 and 0.5 < gravity < 1.5:
        habitability = "Yes"
    else: habitability = "No"

    # habitability = random.choice(["Yes", "No"])
    # Agrgar Air respirable?
    #Agua potable
    query = """
    INSERT INTO "Planets" (name, temperature, gravity, composition, habitability)
    VALUES (%s, %s, %s, %s, %s);
    """
    try:
        cursor.execute(query, (name_planet, temperature, gravity, composition, habitability))
        print(f"Insertado: {name_planet}")
    except Exception as e:
        print(f"Error insertando {name_planet}: {e}")
        print(e)
        conn.rollback()  
    else:
        conn.commit()    

cursor.close()
conn.close()
print("Inserción finalizada.")