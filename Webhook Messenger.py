#coding: UTF-8
import requests
import json
from colored import fg, bg
import os 

os.system("cls")

#color
white = fg("white") 
red = fg("red")
green = fg("green")
orchid = fg("orchid")


json_file = open('config.json', 'r')
json_data = json.load(json_file)

while True:
    print(red + """

▒█░░▒█ █▀▀ █▀▀▄ █░░█ █▀▀█ █▀▀█ █░█ 
▒█▒█▒█ █▀▀ █▀▀▄ █▀▀█ █░░█ █░░█ █▀▄ 
▒█▄▀▄█ ▀▀▀ ▀▀▀░ ▀░░▀ ▀▀▀▀ ▀▀▀▀ ▀░▀                                
    """ + white)

    message = input(orchid +"MESSAGE TO BE SENT = " + green)

    webhook_url = json_data["webhook"]
 
    main_content = {
       "username":  json_data["name"],
       "avatar_url": json_data["icon"],
       "content": message 
       }
    requests.post(webhook_url,main_content)
    os.system("cls")
