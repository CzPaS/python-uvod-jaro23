import json

with open("body2.json", encoding='utf-8') as file:
    body = json.load(file)

for jmeno in body:
   if body[jmeno] >= 60:
       body[jmeno] = "Pass"
   else:
       body[jmeno] = "Fail"

with open("prospech.json", "w", encoding = 'utf-8') as file:
    json.dump(body, file, ensure_ascii=False, indent="")
