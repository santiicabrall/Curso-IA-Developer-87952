'''Quiero aplicando la receta y el ejemplo que vimos hagan un CRUD de una Persona que tiene 
DNI y nombre.

El documento no se puede repetir
El nombre comienza con mayucula y las otra otras con minuscula y no tiene mas de 30 caracteres
Solo hacer los gets y el POST

Probarlo con Thunder Client

'''

from flask import Flask, jsonify, request

from repositories.persona_repository import PersonaRepository
from services.persona_service import PersonaService

app = Flask(__name__)
repositorio = PersonaRepository()
servicio = PersonaService(repositorio)


@app.get("/")
def inicio():
    return jsonify({"mensaje": "API de Personas funcionando"}), 200


@app.get("/personas")
def listar_personas():
    return jsonify([persona.to_dict() for persona in servicio.listar_personas()]), 200


@app.get("/personas/<dni>")
def obtener_persona(dni):
    persona = servicio.obtener_persona(dni)
    if persona is None:
        return jsonify({"error": "No existe una persona con ese DNI."}), 404
    return jsonify(persona.to_dict()), 200


@app.post("/personas")
def crear_persona():
    datos = request.get_json(silent=True)
    if datos is None:
        return jsonify({"error": "El cuerpo debe ser JSON válido."}), 400
    try:
        persona = servicio.crear_persona(datos)
    except ValueError as error:
        mensaje = str(error)
        codigo = 409 if "Ya existe" in mensaje else 400
        return jsonify({"error": mensaje}), codigo
    return jsonify(persona.to_dict()), 201

@app.put("/personas/<dni>")
def actualizar_persona(dni):
    datos = request.get_json(silent=True)
    if datos is None:
        return jsonify({"error": "El cuerpo debe ser JSON válido."}), 400
    try:
        persona = servicio.actualizar_persona(dni, datos)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    if persona is None:
        return jsonify({"error": "No existe una persona con ese DNI."}), 404
    return jsonify(persona.to_dict()), 200


@app.delete("/personas/<dni>")
def eliminar_persona(dni):
    if not servicio.eliminar_persona(dni):
        return jsonify({"error": "No existe una persona con ese DNI."}), 404
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
