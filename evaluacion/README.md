# Microservicios con Docker Compose

Este proyecto implementa 3 microservicios utilizando Docker Compose:

1. **Microservicio de Estudiante**: Gestiona información de estudiantes
2. **Microservicio de Evaluación**: Gestiona evaluaciones de estudiantes
3. **Base de datos MySQL**: Almacena los datos de ambos microservicios

## Estructura del Proyecto

```
microservicios-docker/
├── docker-compose.yml
├── estudiante/
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── estudiante_project/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── urls.py
│   └── estudiante_app/
│       ├── __init__.py
│       ├── models.py
│       ├── serializers.py
│       ├── urls.py
│       └── views.py
└── evaluacion/
    ├── Dockerfile
    ├── manage.py
    ├── requirements.txt
    ├── evaluacion_project/
    │   ├── __init__.py
    │   ├── settings.py
    │   └── urls.py
    └── evaluacion_app/
        ├── __init__.py
        ├── models.py
        ├── serializers.py
        ├── urls.py
        └── views.py
```

## Requisitos

- Docker
- Docker Compose

## Instrucciones de Uso

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd microservicios-docker
   ```

2. Ejecutar los microservicios con Docker Compose:
   ```bash
   docker compose up -d --build
   ```

3. Los servicios estarán disponibles en:
   - Microservicio de Estudiante: http://localhost:8000/api/estudiantes/
   - Microservicio de Evaluación: http://localhost:8001/api/evaluaciones/
   - Base de datos MySQL: localhost:3306

## API de Microservicios

### Microservicio de Estudiante

- **GET /api/estudiantes/** - Listar todos los estudiantes
- **GET /api/estudiantes/{rut}/** - Obtener estudiante por RUT
- **POST /api/estudiantes/** - Crear un nuevo estudiante

Ejemplo de JSON para crear un estudiante:
```json
{
  "rut": "12345678-9",
  "nombre_completo": "Juan Pérez",
  "edad": 20,
  "curso": "Ingeniería Informática"
}
```

### Microservicio de Evaluación

- **GET /api/evaluaciones/** - Listar todas las evaluaciones
- **GET /api/evaluaciones/{id}/** - Obtener evaluación por ID
- **POST /api/evaluaciones/** - Crear una nueva evaluación

Ejemplo de JSON para crear una evaluación:
```json
{
  "rut_estudiante": "12345678-9",
  "semestre": "2025-1",
  "asignatura": "Programación",
  "evaluacion": 6.5
}
```

## Notas Técnicas

- El microservicio de Evaluación valida que el RUT del estudiante exista en el microservicio de Estudiante antes de crear una evaluación.
- Los microservicios están configurados en una red Docker para comunicarse entre ellos.
- La base de datos MySQL persiste los datos en un volumen Docker para mantener la información entre reinicios.