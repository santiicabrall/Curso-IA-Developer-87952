let url = "https://rickandmortyapi.com/api/character"

let respuesta = await fetch(url)

let personajes = await respuesta.json()

console.log(JSON.stringify(personajes, null, 4))

/*import requests
import json
url = "https://rickandmortyapi.com/api/character"
respuesta = requests.get(url)
personajes = respuesta.json()
##print(type(json))
##print(json)
print(json.dumps(personajes, indent=4, ensure_ascii=False))*/