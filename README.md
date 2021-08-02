# Backend test Grupodot #

La aplicación fue desarrollada con el framework web Django y una base de datos MySQL.

## Base de datos ##
*   MySQL

## Instalación ##
*   Primero crer una base de datos MySQL llamada "backend_test_grupodot" 
*   Para conectar la aplicación Django con la base de datos MySQL, ir al archivo settings.py, que está en el directorio backend_test_grupodot/backend_test_grupodot y en el diccionario DATABASES, configurar las credenciales, host etc.
*   Crear un ambiente virtual para las dependencias de Django [Link documentación oficial](https://docs.djangoproject.com/en/3.1/intro/contributing/#getting-a-copy-of-django-s-development-version "djangoenviroment")
*   Activar el ambiente virtual e ir a la carpeta backend_test_grupodot e instalar las dependencias de Django con el siguiente comando usando el archivo requirements.txt que tiene las dependencias
	* ### `pip install -r requirements.txt`
*   Para crear las tablas en la base de datos, en la carpeta backend_test_grupodot ejecutar los siguientes comandos (python o python 3 depende de su configuración cuando la variable de entorno fue establecida)
	* ### `python manage.py makemigrations`
	* ### `python manage.py migrate`
*   Para insertar los registros de ejemplo en la base de datos para ejecutar la aplicación, ejecutar las consultas que se encuentran en el archivo sql_queries_registers.sql en la base de datos.

## Como ejecutarlo ##
*   Ir a la carpeta backend_test_grupodot y ejecutar
	* ### `python manage.py runserver`
*   El enlace en donde se envian las peticiones al endpoint es: http://127.0.0.1:8000/loan_quotation/4000000 como se puede apreciar el valor 4000000 es el parametro (monto) al endpoint

## Ejecutar test unitarios ##
*   Para ejecutar los test unitarios, ir a la carpeta backend_test_grupodot y ejecutar:
	* ### `python manage.py test cotizacion_prestamo`
