# SEDUZAC-Libros
Proyecto para la gestión de entrada y salidas de libros

# Pasos para correr el programa
## 1. Creación del Entorno Virtual
> [!warning] Versión de Python
> Verificar que se tenga la version de python de `Python 3.12.0` para la creación del entorno virtual

Creación del entorno virtual: 
```
python -m venv env
```

Verificar la versión de python
```
python --version
```

Activar el entorno virtual
```
.\env\Scripts\activate
```

Instalar Django en el entorno virtual
```
pip install django
```

## 2. Ejecutar aplicación Django
Ejecutar Django
```
python manage.py runserver
```

## Comandos de DJANGO
Crear un super usuario
```
python manage.py createsuperuser
```

Crear una app
```
python manage.py startapp nombre_de_la_aplicacion
```

> [!WARNING] Recordatorio
> **Registrar la aplicación en el proyecto**: 
> Dentro de `settings.py` agrega el nombre de la aplicación en `INSTALLED_APPS`
