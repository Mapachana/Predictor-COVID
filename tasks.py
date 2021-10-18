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
		run("pip3 install -r requirements-dev.txt")

	print("Instalando dependencias:")
	run("pip3 install -r requirements.txt")

@task
def test(c):
	"""
	Tarea que lanza los tests para comprobar el correcto funcionamiento del programa
	"""
	print("Lanzando comprobaciones... ¡no hay!")

@task
def check(c):
	"""
	Tarea que comprueba si la sintaxis de todos los ficheros del proyecto
	"""

	run("pylint prediccion")
