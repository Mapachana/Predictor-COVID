# Fichero para automatizar la gestión de tareas y dependencias

from invoke import task, run

@task
def installdeps(c, dev=False):
	"""
	Tarea encargada de instalar las dependencias del programa.

	Si se usa con la flasg --dev se instalarán las dependencias de desarrollo también. 
	"""

	if(dev):
		print("Instalando dependencias de dev:")
		
		run("poetry install", shell="/bin/sh")
	else:
		print("Instalando dependencias:")
		run("poetry install --no-dev", shell="/bin/sh")

@task
def test(c):
	"""
	Tarea que lanza los tests para comprobar el correcto funcionamiento del programa
	"""
	print("Lanzando comprobaciones... ")
	run("pytest", shell="/bin/sh")

@task
def check(c):
	"""
	Tarea que comprueba si la sintaxis de todos los ficheros del proyecto es correcta
	"""
	run("pylint --errors-only prediccion", shell="/bin/sh")


@task
def docker(c):
	"""
	Tarea que construye y ejecuta el docker que lanza los tests
	"""
	run("docker build --tag mapachana/predictor-covid . && docker run -t -v `pwd`:/app/test mapachana/predictor-covid", shell="/bin/sh")