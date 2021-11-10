# Documentación adicional del Objetivo 4

## Elección de la biblioteca de aserción y test runner

Se ha elegido usar `assert` como biblioteca de aserción ya que es una funcionalidad incorporada en python, por lo que no es necesario instalar ninguna depedencia externa, y por su simplicidad.

Respecto al testrunner, se consideraron como opciones `pytest` y `unittest`.

`Pytest` es mucho más sencillo y fácil de usar, pero finalmente se ha usado `unittest`, ya que pese a que necesita declarar una clase hija de `unittest.TestCase` ofrece una forma sencilla de comprobar si se lanzan excepciones concretas al ejecutar funciones o métodos. Esta funcionalidad la he considerado especialmente útil, lo que me ha hecho decantarme por usar `unittest`.

