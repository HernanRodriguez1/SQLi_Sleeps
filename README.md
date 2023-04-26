# SQLi_Sleeps

```sh
usage: sqli2.py [-h] -u URLS -d DATA [-c COOKIE]

Realiza una petición GET a múltiples URLs con diferentes datos.

options:
  -h, --help            show this help message and exit
  -u URLS, --urls URLS  Archivo de texto con las URLs a las que se les realizará la petición GET.
  -d DATA, --data DATA  Archivo de texto con los datos que se agregarán a las URLs.
  -c COOKIE, --cookie COOKIE
                        Cookie a incluir en la petición GET.

```

```sh
cat urls.txt | sed 's/FUZZ//g'
```
![image](https://user-images.githubusercontent.com/66162160/234191152-7f27d67b-2a32-476d-8668-0334b1ff08ae.png)

## PoC

```sh
python3 SQLi_Sleeps2.py -u urls.txt -d data.txt

```
![image](https://user-images.githubusercontent.com/66162160/234198892-44835b84-9d06-4280-9a11-7348bfc301f4.png)
