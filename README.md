# Proyecto de IV

> Por Mapachana 

## ¿Qué es?

Durante la pandemia es difícil encontrar toda la información necesaria sobre el covid-19, mantenerse al día con todas las noticias y entender los datos que nos dan. Por tanto, el propósito de este proyecto es facilitar la comprensión de los datos epidemiológicos diarios y proporcionar un fácil acceso a toda la información y el significado de esta.

Así, cualquier usuario tendrá un acceso rápido, sencillo y directo a toda la información actualizada y ayuda para su interpretación desde el móvil.

## Guía de instalación y uso

Para ejecutar este proyecto, comienza por descargar los archivos fuente del repositorio. Esto puede hacerse descargando el repositorio directamente desde la web de github o clonando el repositorio (más información sobre cómo clonar un repositorio [aquí](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository)).

Una vez clonado o descargado, nos situamos en la carpeta raíz del repositorio y abrimos una terminal.

Ahora, instalamos Invoke abriendo una terminal y usando:

```shell
pip install invoke
```

Para más información sobre cómo instalar invoke se puede consultar la [documentación oficial](https://www.pyinvoke.org/installing.html).

También es necesario instalar poetry, para ello puede consultarse [este enlace](https://python-poetry.org/docs/).

Primero, instalamos las dependencias ejecutando el siguiente comando:

```shell
invoke installdeps
```

Si queremos trabajar con el repositorio como desarrolladores debemos añadir el flag `--dev` para instalar las dependencias de desarrollador también.

Una vez hecho esto, lanzamos los tests para comprobar que todo funciona correctamente ejecutando:

```shell
invoke test
```

También podemos comprobar la correcta sintaxis de todos los ficheros del módulo ejecutando:

```shell
invoke check
```

Si no quisiéramos instalar las dependencias en nuestro ordenador personal, se puede usar un contenedor docker que puede construirse y lanzarse usando la orden:

```shell
invoke docker
```

O puede encontrarse el contenedor [aquí](https://hub.docker.com/u/mapachana)

Y ejecutar los tests en este contenedor ejecutando:

```shell
docker run -t -v `pwd`:/app/test mapachana/predictor-covid
```


## Documentación adicional

- Se puede encontrar documentación adicional sobre los tipos de usuario [aquí](https://github.com/Mapachana/Proyecto-IV/blob/Objetivo-1/docs/objetivo1.md)
- La justificación sobre la elección de invoke para el Objetivo 3 puede encontrarse [aquí](https://github.com/Mapachana/Proyecto-IV/blob/Objetivo-3/docs/objetivo3.md)
- La justificación de la elección del test runner y biblioteca de aserciones puede consultarse [aquí](https://github.com/Mapachana/Predictor-COVID/blob/Objetivo-4/docs/objetivo4.md)
- La justificación de las decisiones tomadas respecto al contenedor docker se encuentran [aquí](https://github.com/Mapachana/Predictor-COVID/blob/Objetivo-5/docs/objetivo5.md)
- La justificación de las decisiones tomadas respecto a los sistemas de integración continua se encuentra [aquí](https://github.com/Mapachana/Predictor-COVID/blob/circleci-project-setup/docs/objetivo6.md)
- En estos enlaces podrá ver los distintos issues creados como programador en el proyecto de Mapachana:
    - HU-P1: [Elección de lenguaje de programación](https://github.com/Mapachana/Proyecto-IV/issues/6)
    - HU-P2: [Organización de las clases](https://github.com/Mapachana/Proyecto-IV/issues/7)
- Los datos usados para el proyecto están sacados del repositorio de [datadista](https://github.com/datadista/datasets).