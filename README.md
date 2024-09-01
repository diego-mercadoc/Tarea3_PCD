# Tarea3_PCD
Repositorio que contendra los documentos de la tarea 3 de la materia de Proyecto de Ciencia de Datos. Aquí desarrollarás una API utilizando FastAPI para la gestión de usuarios. La API permite crear, actualizar, obtener y eliminar usuarios, almacenando los datos en una base de datos SQLite. A continuación, se detallan los pasos para configurar y ejecutar este proyecto.


## Requisitos

Para ejecutar este proyecto, asegúrate de tener las siguientes herramientas instaladas:

- Python 3.8 o superior
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

## Instalación

### 1. Clona el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/Tarea3_PCD.git
cd Tarea3_PCD
```

### 2. Crea un ambiente virtual

Es recomendable crear un ambiente virtual para evitar conflictos entre las dependencias de diferentes proyectos:

```bash
python -m venv env
```

Activa el ambiente virtual:

- En macOS/Linux:
  ```bash
  source env/bin/activate
  ```
- En Windows:
  ```bash
  env\Scripts\activate
  ```

### 3. Instala las dependencias

Con el ambiente virtual activo, instala las dependencias necesarias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Este archivo incluye las siguientes dependencias:

- FastAPI: Framework para construir la API.
- Uvicorn: Servidor ASGI para ejecutar la aplicación.
- SQLAlchemy: ORM para manejar la base de datos.
- Pydantic: Validación de datos.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura:

```
Tarea3_PCD/
│
├── env/                  # Ambiente virtual
├── main.py               # Código principal de la API
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Archivo README con instrucciones
```

### Archivo `main.py`

Este archivo contiene la implementación de la API con cuatro endpoints principales:

#### 1. Crear un usuario

- **Método:** `POST`
- **Endpoint:** `/users/`
- **Descripción:** Crea un nuevo usuario y lo guarda en la base de datos.
- **Cuerpo de la solicitud:**
  ```json
  {
    "user_name": "John Doe",
    "user_id": 123,
    "user_email": "johndoe@example.com",
    "age": 30,
    "recommendations": ["book1", "book2"],
    "ZIP": "12345"
  }
  ```
- **Errores:** Si se intenta crear un usuario con un email ya existente, se devolverá un error `400 Bad Request` con el mensaje "El email ya está registrado".

#### 2. Actualizar un usuario

- **Método:** `PUT`
- **Endpoint:** `/users/{user_id}`
- **Descripción:** Actualiza la información de un usuario específico buscando por `user_id`.
- **Cuerpo de la solicitud:** Igual al de creación.
- **Errores:** Si el usuario no existe, se devolverá un error `404 Not Found` con el mensaje "Usuario no encontrado".

#### 3. Obtener un usuario

- **Método:** `GET`
- **Endpoint:** `/users/{user_id}`
- **Descripción:** Obtiene la información de un usuario específico buscando por `user_id`.
- **Errores:** Si el usuario no existe, se devolverá un error `404 Not Found` con el mensaje "Usuario no encontrado".

#### 4. Eliminar un usuario

- **Método:** `DELETE`
- **Endpoint:** `/users/{user_id}`
- **Descripción:** Elimina un usuario específico buscando por `user_id`.
- **Errores:** Si el usuario no existe, se devolverá un error `404 Not Found` con el mensaje "Usuario no encontrado".

## Ejecución de la API

Para ejecutar la API en modo de desarrollo, utiliza el siguiente comando:

```bash
uvicorn main:app --reload
```

Esto iniciará un servidor local que escuchará en `http://127.0.0.1:8000`. Con la opción `--reload`, el servidor se reiniciará automáticamente si detecta cambios en el código fuente.

## Documentación de la API

FastAPI genera automáticamente una documentación interactiva para tu API:

- **Swagger UI:** Disponible en `http://127.0.0.1:8000/docs`.
- **ReDoc:** Disponible en `http://127.0.0.1:8000/redoc`.

Estas interfaces te permiten explorar y probar los endpoints de tu API directamente desde el navegador.

## Testing

Es recomendable probar todos los endpoints para asegurarse de que la API funcione correctamente. Puedes hacerlo utilizando herramientas como `curl`, `httpie`, o Postman.

### Ejemplo de pruebas usando `curl`:

1. **Crear un usuario:**
   ```bash
   curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d '{"user_name":"John Doe","user_id":123,"user_email":"johndoe@example.com","age":30,"recommendations":["book1","book2"],"ZIP":"12345"}'
   ```

2. **Actualizar un usuario:**
   ```bash
   curl -X PUT "http://127.0.0.1:8000/users/123" -H "Content-Type: application/json" -d '{"user_name":"John Doe","user_id":123,"user_email":"johndoe@example.com","age":31,"recommendations":["book3"],"ZIP":"54321"}'
   ```

3. **Obtener un usuario:**
   ```bash
   curl -X GET "http://127.0.0.1:8000/users/123"
   ```

4. **Eliminar un usuario:**
   ```bash
   curl -X DELETE "http://127.0.0.1:8000/users/123"
   ```

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Empuja la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
