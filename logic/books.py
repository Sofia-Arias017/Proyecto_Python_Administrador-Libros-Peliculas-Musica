import json

def findAll():
    with open("data/books.json", "r", encoding="utf-8") as file :
        data = file.read()
        convertBooks = json.loads(data)
        return convertBooks

def addBook(formulary):
    data = findAll()
    data.append(formulary)
    return saveAll(data)

def saveAll(data):
    with open("data/books.json", "w", encoding="utf-8") as file:
        str(data).encode('utf-8')
        convertJSON = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJSON)
        return "Se modifico el archivo books.json"
    