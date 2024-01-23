import argparse
import requests
import time

def perform_request(url, data, cookie):
    url_with_data = "{}{}".format(url, data)
    start_time = time.time()

    try:
        response = requests.get(url_with_data, cookies={'cookie': cookie} if cookie else None)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        return False, url_with_data, time.time() - start_time, str(e)

    return True, url_with_data, time.time() - start_time, None

def main():
    parser = argparse.ArgumentParser(description="Realiza una petición GET a múltiples URLs con diferentes datos.")
    parser.add_argument("-u", "--urls", required=True, help="Archivo de texto con las URLs a las que se les realizará la petición GET.")
    parser.add_argument("-d", "--data", required=True, help="Archivo de texto con los datos que se agregarán a las URLs.")
    parser.add_argument("-c", "--cookie", help="Cookie a incluir en la petición GET.")
    args = parser.parse_args()

    with open(args.urls) as file:
        urls = file.read().splitlines()

    with open(args.data) as file:
        data = file.read().splitlines()

    for url in urls:
        for d in data:
            success, url_with_data, response_time, error_message = perform_request(url, d, args.cookie)

            if success and response_time <= 20:
                print("\033[1;32mURL {} - {:.2f} segundos\033[0m".format(url_with_data, response_time))
            else:
                print("\033[1;31mURL {} - {:.2f} segundos - Error: {}\033[0m".format(url_with_data, response_time, error_message))

if __name__ == "__main__":
    main()
