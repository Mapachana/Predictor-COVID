# Documentación adicional del Objetivo 5

## Requisitos

Se quiere probar el proyecto en entornos estables, en concreto para python 3.8, usando un contenedor base que tenga soporte y cuya versión sea la última estable disponible del mismo.

Además, será importante que el contenedor sea lo más pequeño posible, haciendo así que sea más rápido y eficiente, y minimizando también el número de dependencias.

## Elección del contenedor base

Como contenedor base se ha usado el contenedor oficial de Python con Python 3.8.

Además al elegir qué variante del contenedor oficial se va a usar (las variantes pueden consultarse [aquí](https://hub.docker.com/_/python)), ya que no necesitamos demasiadas funcionalidades propias de un sistema operativo y buscamos hacer el contenedor lo más ligero posible se ha elegido alpine, que es menos pesado y más rápido.

Se va a usar la versión `latest` de alpine para asegurar que la versión sea la última estable.

## ¿Cómo instalar poetry?

Para instalar poetry podemos usar curl, wget o pip. Si usamos curl, solo es necesario instalar curl, mientras que si usamos pip es necesario tener la libreria libffi-dev y gcc instalado.

En lugar de usar curl finalmente se ha usado wget, que viene instalado por defecto. De esta forma se minimizan las dependencias a mantener. ¿Pero y el tamaño?

## Tamaño del contenedor

Se han probado diversas configuraciones en el docker, ya sea poniendo en un `run` aparte el comando para crear el grupo de usuario, dejando curl instalado sin borrarlo pese a no ser necesario o borrándolo tras dejar de ser útil. En todas estas configuraciones, instalando poetry con curl, el contenedor ha ocupado 219MB, por lo que finalmente se ha optado por desinstalar curl al terminar de usarlo.

Si en lugar de usar curl se usa pip para instalar poetry entonces es necesario instalar gcc y la librería libffi-dev, por lo que el tamaño del contenedor es 305MB.

Finalmente, al usar wget en lugar de curl el contenedor pesa 219MB. Es decir, no hay diferencia en el peso del contenedor, pero para minimizar las dependencias en la configuración final del contenedor se instalará con poetry.

## Configuración de poetry

En el contenedor, al construirlo se ha ejecutado este comando de poetry.

```shell
RUN  poetry config virtualenvs.create false; invoke installdeps --dev
```

Poetry por defecto poetry instala las dependencias en entornos virtuales propios para encapsularlos y aislarlos. Pero esto es innecesario, ya que estamos usando un contenedor para tener las dependencias y el proyecto aislados del resto del sistema, luego se desactiva la creación de entornos virtuales.

De esta manera las dependencias se instalan directamente en el contenedor, haciéndolas accesibles sin usar entornos virtuales y, por tanto, haciéndolo más ligero.
