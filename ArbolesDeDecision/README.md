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

