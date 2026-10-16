from models.persona import Persona

class PersonaRepository:
    """Repositorio en memoria. Los datos se reinician al detener la API."""

    def __init__(self):
        
        self._personas: dict[str, Persona] = {}

        # Cargar datos de prueba
        personas_prueba = [
            Persona(dni="30111222", nombre="Juan perez"),
            Persona(dni="32444555", nombre="Maria lopez"),
            Persona(dni="35666777", nombre="Carlos gomez"),
            Persona(dni="38999888", nombre="Ana martinez"),
            Persona(dni="41222333", nombre="Lucas fernandez"),
        ]

        for persona in personas_prueba:
            self._personas[persona.dni] = persona

    def listar(self) -> list:
        return list(self._personas.values())

    def obtener(self, dni: str):
        return self._personas.get(dni)

    def crear(self, persona):
        if self.existe(persona.dni):
            raise ValueError("Ya existe una persona con ese DNI.")
        self._personas[persona.dni] = persona
        return persona
    
    def existe(self, dni: str) -> bool:
        return dni in self._personas

    def actualizar(self, dni: str, persona):
        if not self.existe(dni):
            return None
        # El DNI identifica a la persona y no se modifica durante la actualización.
        persona.dni = dni
        self._personas[dni] = persona
        return persona

    def eliminar(self, dni: str) -> bool:
        if not self.existe(dni):
            return False
        del self._personas[dni]
        return True

 
    
