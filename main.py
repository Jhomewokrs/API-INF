#VARIABLES DE ENTORNO
#ABRAHAM ORTIZ VALLENILLA/INGENIERIA INFORMATICA
#Uso de apredizaje= Clean code 

#Objetivo del programa= Crear una API que permita buscar, procesar y mostrar resultados de busqueda en la web

import os  #nteractuar con el sistema operativo, como leer y escribir variables de entorno.
import requests #realizar solicitudes HTTP en Python. Nos servirá para interactuar con la API.
from dotenv import load_dotenv #cargar variables de entorno desde un archivo

# Cargar variables de entorno
def load_environment_variables():
    load_dotenv()
    return os.getenv("API_KEY_SEARCH_GOOGLE"), os.getenv("SEARCH_ENGINE_ID")

# Construir la URL de la solicitud
def build_url(api_key, search_engine_id, query, page, lang):
    base_url = "https://www.googleapis.com/customsearch/v1"
    return f"{base_url}?key={api_key}&cx={search_engine_id}&q={query}&start={page}&lr={lang}"

# Realizar la solicitud y obtener datos
def fetch_results(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        return None

# Procesar y mostrar resultados
def display_results(results):
    if not results:
        print("No se encontraron resultados.")
    else:
        for item in results:
            print(f"Title: {item.get('title')}")
            print(f"Link: {item.get('link')}")
            print(f"Snippet: {item.get('snippet')}")
            print("-" * 80)

# Main
def main():
    API_KEY, SEARCH_ENGINE_ID = load_environment_variables()
    if not API_KEY or not SEARCH_ENGINE_ID:
        print("Faltan las claves API o el ID del motor de búsqueda.")
        return
   
    query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
    page = 1
    lang = "lang_es"
   
    url = build_url(API_KEY, SEARCH_ENGINE_ID, query, page, lang)
    results = fetch_results(url)
    display_results(results)

if __name__ == "__main__":
    main()

