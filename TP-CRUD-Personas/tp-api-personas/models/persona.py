import re


class Persona:
    """Representa una persona con DNI y nombre validados."""

    def __init__(self, dni: str, nombre: str):
        self.dni = self._validar_dni(dni)
        self.nombre = self._validar_nombre(nombre)

    @staticmethod
    def _validar_dni(dni: str) -> str:
        if not isinstance(dni, str):
            raise ValueError("El DNI debe enviarse como texto.")

        dni = dni.strip()
        if not dni:
            raise ValueError("El DNI es obligatorio.")
        if not dni.isdigit():
            raise ValueError("El DNI debe contener solamente números.")
        return dni

    @staticmethod
    def _validar_nombre(nombre: str) -> str:
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser texto.")

        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if len(nombre) > 30:
            raise ValueError("El nombre no puede superar los 30 caracteres.")
        if nombre[0] != nombre[0].upper() or nombre[0] == nombre[0].lower():
            raise ValueError("El nombre debe comenzar con mayúscula.")
        if any(letra.isupper() for letra in nombre[1:]):
            raise ValueError("Las letras después de la primera deben ser minúsculas.")
        if not all(letra.isalpha() or letra.isspace() for letra in nombre):
            raise ValueError("El nombre solo puede contener letras y espacios.")
        return nombre

    def to_dict(self) -> dict:
        return {"dni": self.dni, "nombre": self.nombre}
