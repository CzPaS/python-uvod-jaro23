import json

with open('bonusy.json', encoding= 'utf-8') as file:
    bonusy = json.load(file)

#print(bonusy)

with open('body2.json', encoding= 'utf-8') as file:
    body = json.load(file)

#print(body)

for jmeno in bonusy:
    if jmeno in bonusy:
        body[jmeno] += bonusy[jmeno] 

print(body)

for jmeno in body:
    if body[jmeno] >= 90:
       body[jmeno] = "1"
    elif body[jmeno] >= 70:
         body[jmeno] = "2"
    elif body[jmeno] >= 50:
         body[jmeno] = "3"
    elif body[jmeno] >= 30:
         body[jmeno] = "4"
    else:
         body[jmeno] = "5"

print(body)

with open('znamky.json', mode = 'w', encoding = 'utf-8') as file:
    json.dump(body, file, ensure_ascii=False, indent='')