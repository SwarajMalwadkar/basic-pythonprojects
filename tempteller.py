import requests
import json
import win32com.client as wincom


speak = wincom.Dispatch("sapi.SpVoice")

city = input("enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=33fe0fc02fc542beb5762433242005&q={city}"
r = requests.get(url)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
l=wdic["location"]["country"]
u=wdic["current"]["last_updated"]
text= " the curret temperature of {} which is situated in {} is {} which was updated at {} ".format(city,l,w,u)
speak.Speak(text)