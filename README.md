# SQLi_Sleeps

```sh
python3 paramspider.py --domain http://testphp.vulnweb.com/ --exclude woff,css,js,png,svg,jpg --output /home/hernan/urls.txt

cat urls.txt | sed 's/FUZZ//g'
```
![image](https://user-images.githubusercontent.com/66162160/234191152-7f27d67b-2a32-476d-8668-0334b1ff08ae.png)

## PoC

```sh
python3 sqli2.py -u urls.txt -d data.txt

```
![image](https://user-images.githubusercontent.com/66162160/234198892-44835b84-9d06-4280-9a11-7348bfc301f4.png)
