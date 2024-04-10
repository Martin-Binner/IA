# Consistencia

Nuestra elección no trivial de la heuristica se basa en la solución óptima de que no haya muros en el laberinto. 
Al no haber muros, el valor estimado de cumplir el objetivo va a ser siempre menor o igual al real y si hay 
interferencia de muros, el costo estimado será menor. Esto es, la heurística es admisible.
Por otro lado, como el costo de un paso es 1 y al movernos por el recorrido óptimo la heurística se reduce en 1, 
tenemos h(n) = c(n,n') + h(n') para n el nodo actual y n' el sucesor. Si nos alejamos del camino por la 
aparición de un muro, la heurística aumenta en 1, por lo cual tendremos que h(n) < c(n,n') + h(n'). Por lo tanto, 
la heurística es consistente ya que para todo n y n', h(n) =< c(n,n') + h(n').

