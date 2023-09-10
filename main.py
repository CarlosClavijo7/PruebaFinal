import json
import time
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

uri = "mongodb+srv://admin:Administrad0r@cluster0.mc2jx0g.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(uri, server_api=ServerApi('1'))


driver = webdriver.Chrome()
driver.get("http://worldweather.wmo.int")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#q_search")
search_box.send_keys("Guayaquil, Ecuador")
search_box.send_keys(Keys.ENTER)
search_button = driver.find_element(by=By.CSS_SELECTOR, value="#searchForm > input.top_searchbox_submit")
time.sleep(5)
search_button.click()

tabla_temp = driver.find_elements(By.CSS_SELECTOR, "#climateTable > table")
time.sleep(5)

try:
    db = client['Tratamiento_de_datos']

    col = db['PRUEBA']
    # Crear una lista para almacenar los datos de cada mes

    data_list = []
    for card in tabla_temp:
        mes_data = {}  # Crear un diccionario para almacenar los datos del mes actual
        nombres = ["mes", "dato1", "dato2", "dato3", "dato4"]

        for j in range(2, 14):

            for i in range(1, 6):
                dato = card.find_element(By.CSS_SELECTOR, f"tr:nth-child({j}) > td:nth-child({i})").text
                nombre = nombres[i - 1]
                mes_data[nombre] = dato  # Agregar el dato al diccionario
        data_list.append(mes_data)  # Agregar el diccionario de datos del mes a la lista



    with open('datos.json', 'w') as json_file:
        json.dump(data_list, json_file, indent=4)

    print("Datos guardados en datos.json")
    print(data_list)

    col.insert_many(data_list)

    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print(client.list_database_names())


except Exception as e:
    print(e)

driver.close()