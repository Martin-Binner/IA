# Árboles de Decisión

- **Método de aproximación de funciones con valores discretos**
- Son uno de los métodos más conocidos
- Son la base para muchos otros métodos
- Nadie usa esto para machine learning, pero son las bases de los bosques de decisión

La idea es ir **descendiendo** por el árbol hasta encontrar una hoja que nos determine el resultado deseado.  
Los nodos son atributos, los sub-árboles representan posibles instancias de los atributos y los hijos son valores (YES-NO).

Al tener distintos árboles, tenemos mayor expresividad ya que tenemos **disyunciones**.  
Se adaptan al posible ruido de la muestra y funcionan cuando faltan datos en la muestra.

## ¿Cuál Árbol de Decisión?

Hay muchos árboles de decisión en la mayoría de los casos, pero nos interesan los **más chicos**, los **más simples**. El problema de esto es que encontrar el más chico es un problema **NP-hard**, lo que implica una restricción computacional.  
Debido a lo anterior, buscaremos un DT "parecido" al más chico.

# Algoritmo ID3

`ID3(Examples, Target_attribute, Attributes)`

**Examples** son los ejemplos de entrenamiento. **Target_attribute** es el atributo cuyo valor será predicho por el árbol. **Attributes** es una lista de otros atributos que pueden ser probados por el árbol de decisión aprendido. Devuelve un árbol de decisión que clasifica correctamente los ejemplos dados.

- Crear un nodo **Root** para el árbol.
- Si todos los **Examples** son positivos, devolver el árbol de un solo nodo **Root**, con la etiqueta = +.
- Si todos los **Examples** son negativos, devolver el árbol de un solo nodo **Root**, con la etiqueta = -.
- Si **Attributes** está vacío, devolver el árbol de un solo nodo **Root**, con la etiqueta = el valor más común del **Target_attribute** en **Examples**.
- De lo contrario, comenzar:
  - A ← el atributo de **Attributes** que mejor clasifica **Examples**.
  - El atributo de decisión para **Root** ← A.
  - Para cada valor posible vi de A:
    - Añadir una nueva rama al árbol debajo de **Root**, correspondiente a la prueba A = vi.
    - Dejar que **Examplesvi** sea el subconjunto de **Examples** que tiene el valor vi para A.
    - Si **Examplesvi** está vacío:
        - Entonces, debajo de esta nueva rama, añadir un nodo hoja con la etiqueta = el valor más común del **Target_attribute** en **Examples**.
        - De lo contrario, debajo de esta nueva rama, añadir el subárbol: `ID3(Examplesvi, Target_attribute, Attributes - {A})`
- Fin
- Devolver **Root**

