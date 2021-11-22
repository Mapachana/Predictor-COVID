# Documentación adicional del Objetivo 5

## Elección del contenedor base

El proyecto está programado en python, por lo que como contenedor base se ha usado el contenedor oficial de Python en su versión 3.8, ya que es la misma versión en la que se ha desarrollado el proyecto en primer lugar y es estable.

Además al usar alpine el contenedor es más ligero.

## Tamaño del contenedor

Se han probado diversas configuraciones en el docker, ya sea poniendo en un `run` aparte el comando para crear el grupo de usuario, dejando curl instalado sin borrarlo pese a no ser necesario o borrándolo tras dejar de ser útil. En todas estas configuraciones el contenedor ha ocupado 219MB, por lo que finalmente se ha optado por desinstalar curl al terminar de usarlo.

## ¿Por qué instalar curl?

Se ha instalado curl ya que es necesario para instalar poetry, y tras instalarlo se ha desinstalado curl.