import argparse
import requests
import time


parser = argparse.ArgumentParser(description="Realiza una petición GET a múltiples URLs con diferentes datos.")
parser.add_argument("-u", "--urls", required=True, help="Archivo de texto con las URLs a las que se les realizará la petición GET.")
parser.add_argument("-d", "--data", required=True, help="Archivo de texto con los datos que se agregarán a las URLs.")
parser.add_argument("-c", "--cookie", help="Cookie a incluir en la petición GET.")
args = parser.parse_args()


# Abre el archivo de texto con las URLs
with open(args.urls) as file:
    urls = file.read().splitlines()

# Abre el archivo de texto con los datos
with open(args.data) as file:
    data = file.read().splitlines()

# Recorre la lista de URLs
for url in urls:
    # Recorre la lista de datos y agrega los valores a la URL
    for d in data:
        url_with_data = url + d

        start_time = time.time()  # Obtiene el tiempo actual

        # Realiza la petición GET con la cookie si es que existe
        try:
            if args.cookie:
                response = requests.get(url_with_data, cookies={'cookie': args.cookie})
            else:
                response = requests.get(url_with_data)
        except requests.exceptions.RequestException as e:
            print("\033[1;31mURL {} - Error: {}\033[0m".format(url_with_data, e))
            continue

        end_time = time.time()  # Obtiene el tiempo después de la respuesta

        # Imprime la URL y el tiempo de respuesta en color verde o rojo
        if response.ok and end_time - start_time <= 20:
            print("\033[1;32mURL {} - {:.2f} segundos\033[0m".format(url_with_data, end_time - start_time))
        else:
            print("\033[1;31mURL {} - {:.2f} segundos\033[0m".format(url_with_data, end_time - start_time))
