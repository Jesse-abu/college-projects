import json
import socket
#rt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#rt.connect(("data.pr4e.org", 80))
#cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0 \n\n".encode()
#rt.send(cmd)
estate = """{
"resident1": {"name":"John",
"age":"32",
"address": {
"country":"Nigeria",
"state":"Rivers",
"LGA":"Port Harcourt",
"Road":"Rumodara",
"House":"No_14"}
},
"resident2": {"name":"Gabriel",
"age":"25",
"address": {
"country":"Nigeria",
"state":"Rivers",
"LGA":"Port Harcourt",
"Road":"Elekahia",
"House":"No_24"}
},
"resident3": {"name":"Samuel",
"age":"28",
"address": {
"country":"Nigeria",
"state":"Rivers",
"LGA":"Port Harcourt",
"Road":"Rumola",
"House":"No_11"}
}
}"""

data = {
"lang": None,
"color":"00FF00",
"width": 333,
"height": 111,
"location": "extended",
"picture": "https://commons.wikimedia.org/wiki/File:Green_Slime_in_hand.JPG",
"secret_password": "98h$8h(*#(*H(*#7t737r3bl0Bbl0Bbl0B8dghsytgauhvcjhb4jasdf",
"display_name":"The Real Evilcorp",
"bio": "Your best choice. Most likely, your only choice.",
"location": "Classified",
"picture": "data/images/evilcorp-lowrez.png",
"verification": 2,
"follower_count": 800000000,
"following_count": 0,
"join_date": "2011-12-09",
"posts": [],
"visits_by_date": {
"2011-12-09": 453,
"2011-12-10": 710,
"2011-12-11": 490,
"2011-12-12": 554,
"2011-12-13": 698,
"2011-12-14": 953,
"2011-12-15": 547,
"2011-12-16": 732,
"2011-12-17": 475}
}

location = json.loads(estate)
accounts = json.loads(data)

