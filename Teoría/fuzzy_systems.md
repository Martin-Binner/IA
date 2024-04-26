# Fuzzy Systems

Rama  de la IA que permite trabajar con razonamientos impresisos a partir de razonamientos impresisos mediante *Conjuntos Borrosos* (_fuzzy sets_).

En conjuntos normales, se puede definir una función característica a partir de si un elemento pertence a dicho conjunto o si nó pertenece al mismo. Esto es está claro en el concepto de lógica al que estamos acostumbrados, ya que la semántica de un 
predicado puede ser T o F, pero acá estamos trabajando con lógicas _multivaluadas_
donde la semántica de una proposición no es necesariamente "verdadera" o "falsa".
De acá viene el término "difuso" o "borroso". En este caso, nosotros vamos a determinar que tan verdad es algo a partir de inferecias o razonamientos que no son exactos.

Por ejemplo, en el caso de la función característica de un conjunto A sub X,
podemos definirla como $f_{A} : X  -> [0,1]$, donde $f_{A}(x)$ indica el grado 
de pertencia de x en el conjunto $A$. Si estamos completamente seguros, decimos 
$f_{A}(x) = 1$ pero si creemos lo contrario decimos $f_{A}(x) = 0$. Ahora podemos
no estar tan seguros de si pertenece o no, por lo que un valor como $f_{A}(x) = 0,5$
sigue siendo totalmente válido.

Luego podemos caracterizar estos conjuntos con el grado de pertenecia que le damos
a cada uno de los elementos de X con respecto a A. Por lo que tenemos
$$A = {(x,f_{A}(x)) | x \in X}$$.

Si el conunto X es de elementos contínuos, basta con dar la ley de una función del 
tipo correspondiente. Si el conjunto es finito, se puede simplenete enumerar los
valores en una tupla $(f_{A}(x_{1})/x_{1},...,f_{A}(x_{n})/x_{n})$


