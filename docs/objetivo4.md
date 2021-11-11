# Documentación adicional del Objetivo 4

## Elección de la biblioteca de aserción y test runner

Se ha elegido usar `unittest` como biblioteca de aserción ya que, a pesar de ser más compleja y necesitar heredar de la clase `unittest.TestCase`, tiene funcionalidad para comprobar cuándo se lanza una excepción concreta al ejecutar diversos métodos y funciones, lo que he considerado especialmente útil. También va a usarse `assert` por su simplicidad.

Respecto al testrunner, se ha usado `pytest` ya que es muy sencilla y su uso está muy extendido para ejecutar tests en python.

