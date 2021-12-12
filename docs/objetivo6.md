# Documentación adicional del Objetivo 6

Para comprobar que el proyecto funciona con diferentes versiones de python se van a usar varios sistemas de integración continua.

Se ha priorizado que el sistema de integración continua proporcione servidores propios para ejecutar los procesos, su integración con github sea sencilla y, ya que vamos a probar varias versiones de python a la vez en una misma ejecución, que pueda lanzarlos en paralelo.

Se ha probado a configurar [azure](https://azure.microsoft.com/es-es/), pero no se logró configurar para emplearlo.

También se ha mirado [semaphore](https://semaphoreci.com/), pero el período de prueba era de 14 días, por lo que se podría haber acabado antes de terminar el desarrollo del proyecto.

Por esto, finalmente se ha elegido [circleci](https://circleci.com/). Ha sido necesario activar la checksapi, pero no ha requerido de configuración adicional, por lo que es sencillo de usar. También admite paralelización en sus ejecuciones, por lo que cumple con los requesitos.

Respecto a las versiones de python a comprobar, se ha elegido la 3.7, ya que es la mínima versión de python que admite dataclass, la 3.10 por ser la última versión y la 3.9, ya que la versión 3.8 ya se comprobó en el objetivo anterior. Así, se han comprobado todas las versiones de python.

En circleci se comprueban las versiones 3.7 y 3.9, ya que poetry no puede instalarse mediante wget a partir de python 3.9.7, pues por problemas de poetry le faltan algunos módulos. Para comprobar la versión de python 3.10 por tanto se ha usado un contenedor docker en el que se han instalado manualmente los módulos necesarios para instalar poetry usando wget. No se ha instalado usando pip porque al hacerlo de esta manera requiere de compiladores externos como c y rust, lo que habría realentizado mucho la instalación.

Como segundo sistema para lanzar el docker que emplea la versión 3.10 de python se ha usado github actions, pues cumple con todos los requisitos y proporciona muchas actions ya preparadas para trabajar con docker, haciéndolo así sencillo.