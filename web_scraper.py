import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
from datetime import datetime

# Función para extraer datos de una página web
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Ejemplo: extraer todos los títulos h2
    data = [h2.text for h2 in soup.find_all('h2')]
    return data

# Función para obtener datos de una API
def get_api_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Función para procesar y combinar datos
def process_data(web_data, api_data):
    # Ejemplo simple: combinar datos en un diccionario
    processed_data = {
        'web_data': web_data,
        'api_data': api_data,
        'timestamp': datetime.now().isoformat()
    }
    return processed_data

# Función para almacenar datos en SQLite
def store_in_database(data, db_name='scraped_data.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Crear tabla si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scraped_data
    (id INTEGER PRIMARY KEY, web_data TEXT, api_data TEXT, timestamp TEXT)
    ''')
    
    # Insertar datos
    cursor.execute('''
    INSERT INTO scraped_data (web_data, api_data, timestamp)
    VALUES (?, ?, ?)
    ''', (str(data['web_data']), str(data['api_data']), data['timestamp']))
    
    conn.commit()
    conn.close()

# Función para exportar datos a CSV
def export_to_csv(data, filename='scraped_data.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

# Función principal
def main():
    # URL de ejemplo (reemplazar con la URL real)
    web_url = 'https://example.com'
    # URL de API de ejemplo (reemplazar con la API real)
    api_url = 'https://api.example.com/data'
    
    web_data = scrape_website(web_url)
    api_data = get_api_data(api_url)
    
    processed_data = process_data(web_data, api_data)
    
    store_in_database(processed_data)
    export_to_csv(processed_data)
    
    print("Datos extraídos, procesados y almacenados con éxito.")

if __name__ == "__main__":
    main()
