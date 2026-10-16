# TP - API CRUD de Personas

API REST desarrollada en Python con Flask para crear, consultar, actualizar y eliminar personas. Cada persona tiene un DNI y un nombre.

## Reglas de validación

- El DNI es obligatorio y solo puede contener números.
- No puede haber dos personas con el mismo DNI.
- El nombre es obligatorio y tiene un máximo de 30 caracteres.
- El nombre comienza con mayúscula y todas las letras siguientes deben ser minúsculas. Se permiten espacios, pero no números ni símbolos.
- Los datos se guardan en memoria: se pierden al detener o reiniciar la aplicación.

## Estructura

```text
tp-api-personas/
├── api.py
├── models/
│   └── persona.py
├── repositories/
│   └── persona_repository.py
├── services/
│   └── persona_service.py
├── tests/
│   └── test_persona.py
├── requirements.txt
└── README.md
```



La API queda disponible en `http://127.0.0.1:5000`.

## Endpoints

| Método | Ruta | Acción |
|---|---|---|
| GET | `/` | Comprueba que la API funciona |
| GET | `/personas` | Lista todas las personas |
| GET | `/personas/<dni>` | Busca una persona por DNI |
| POST | `/personas` | Crea una persona |



