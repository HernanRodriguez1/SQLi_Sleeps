# SQLi_Sleeps
It is a simple script that allows to find SQLi vulnerabilities, obtaining the response time greater than 20 seconds per medium and time-based injection.


```sh
usage: SQLi_Sleeps2.py [-h] -u URLS -d DATA [-c COOKIE]

Realiza una petición GET a múltiples URLs con diferentes datos.

options:
  -h, --help            show this help message and exit
  -u URLS, --urls URLS  Archivo de texto con las URLs a las que se les realizará la petición GET.
  -d DATA, --data DATA  Archivo de texto con los datos que se agregarán a las URLs.
  -c COOKIE, --cookie COOKIE
                        Cookie a incluir en la petición GET.

# Cookie simple
python3 script.py -u urls.txt -d data.txt -c "session=abc123"

# Múltiples cookies
python3 script.py -u urls.txt -d data.txt -c "session=abc123; user_id=456"

# Sin cookie
python3 script.py -u urls.txt -d data.txt

```

```sh
cat urls.txt | sed 's/FUZZ//g'
```
![image](https://user-images.githubusercontent.com/66162160/234191152-7f27d67b-2a32-476d-8668-0334b1ff08ae.png)

## PoC

```sh
python3 SQLi_Sleeps2.py -u urls.txt -d data.txt

```
![image](https://github.com/HernanRodriguez1/SQLi_Sleeps/assets/66162160/cfe04560-b090-440a-837c-479b37394eb8)


