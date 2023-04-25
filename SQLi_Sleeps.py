import requests
import time

# Abre el archivo de texto con las URLs
with open("urls.txt") as file:
    urls = file.read().splitlines()

# Abre el archivo de texto con los datos
with open("data.txt") as file:
    data = file.read().splitlines()

# Recorre la lista de URLs
for url in urls:
    # Recorre la lista de datos y agrega los valores a la URL
    for d in data:
        url_with_data = url + d

        start_time = time.time()  # Obtiene el tiempo actual

        # Realiza la petición GET
        try:
            response = requests.get(url_with_data)
        except requests.exceptions.RequestException as e:
            print("\033[1;31mURL {} - Error: {}\033[0m".format(url_with_data, e))
            continue

        end_time = time.time()  # Obtiene el tiempo después de la respuesta

        # Imprime la URL y el tiempo de respuesta en color verde o rojo
        if end_time - start_time <= 20:
            print("\033[1;32mURL {} - {:.2f} segundos\033[0m".format(url_with_data, end_time - start_time))
        else:
            print("\033[1;31mURL {} - {:.2f} segundos\033[0m".format(url_with_data, end_time - start_time))
