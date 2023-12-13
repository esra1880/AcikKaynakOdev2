import requests
import json

def getGenders(names):
    url = ""
    cnt = 0
    if not isinstance(names, list):
        names = [names,]

    for name in names:
        if url == "":
            url = "name[0]=" + name
        else:
            cnt += 1
            url = url + "&name[" + str(cnt) + "]=" + name

    req = requests.get("https://api.genderize.io?" + url)
    results = json.loads(req.text)

    retrn = []
    for result in results:
        if result["gender"] is not None:
            gender = result["gender"]
            message = f"{result['name']} isminin cinsiyeti {gender}"
        else:
            gender = 'None'
            message = f"{result['name']} isminin cinsiyeti yok"

        retrn.append((gender, message))

    return retrn

if __name__ == '__main__':
    results = getGenders(["Esra", "Eslem", "Ayakkabı","Ahmet"])
    for gender, message in results:
        print(message)