from models.persona import Persona
from repositories.persona_repository import PersonaRepository


class PersonaService:
    def __init__(self, repositorio: PersonaRepository):
        self.repositorio = repositorio

    def listar_personas(self):
        return self.repositorio.listar()

    def obtener_persona(self, dni: str):
        return self.repositorio.obtener(dni)

    def crear_persona(self, datos: dict):
        if not isinstance(datos, dict):
            raise ValueError("El cuerpo de la solicitud debe ser un objeto JSON.")
        if "dni" not in datos or "nombre" not in datos:
            raise ValueError("Se requieren los campos 'dni' y 'nombre'.")
        persona = Persona(datos["dni"], datos["nombre"])
        return self.repositorio.crear(persona)

    def actualizar_persona(self, dni: str, datos: dict):
        if not isinstance(datos, dict):
            raise ValueError("El cuerpo de la solicitud debe ser un objeto JSON.")
        if "nombre" not in datos:
            raise ValueError("Se requiere el campo 'nombre'.")
        if not self.repositorio.existe(dni):
            return None
        persona = Persona(dni, datos["nombre"])
        return self.repositorio.actualizar(dni, persona)


    def eliminar_persona(self, dni: str) -> bool:
        return self.repositorio.eliminar(dni)
