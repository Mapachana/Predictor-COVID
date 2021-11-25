# Documentación adicional del Objetivo 5

## Elección del contenedor base

El proyecto está programado en python, por lo que como contenedor base se ha usado el contenedor oficial de Python con Python 3.8, ya que es una versión de python bastante extendida y estable.

Además al elegir qué variante del contenedor oficial se va a usar (las variantes pueden consultarse [aquí](https://hub.docker.com/_/python)), ya que no necesitamos demasiadas funcionalidades propias de un sistema operativo y buscamos hacer el contenedor lo más ligero posible me he decantado por alpine. 

Otra ventaja de usar este contenedor como base es que al ser oficial, el contenedor tiene una documentación clara y mucha información sobre dudas frecuentes en la comunidad, así como sus soluciones. Asimismo se garantiza que el contenedor tenga soporte y actualizaciones para garantizar la seguridad de la imagen.

## Tamaño del contenedor

Se han probado diversas configuraciones en el docker, ya sea poniendo en un `run` aparte el comando para crear el grupo de usuario, dejando curl instalado sin borrarlo pese a no ser necesario o borrándolo tras dejar de ser útil. En todas estas configuraciones el contenedor ha ocupado 219MB, por lo que finalmente se ha optado por desinstalar curl al terminar de usarlo.

Si en lugar de usar curl se usa pip para instalar poetry entonces es necesario instalar gcc y la librería libffi-dev, por lo que el tamaño del contenedor es 305MB.

## ¿Cómo instalar poetry?

Para instalar poetry podemos usar curl o pip según la documentación oficial. Si usamos curl, solo es necesario instalar curl, mientras que si usamos pip es necesario tener la libreria libffi-dev y gcc instalado.

En lugar de usar curl finalmente se ha usado wget, que viene instalado por defecto. De esta forma se minimizan las dependencias a mantener.