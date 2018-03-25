########################################################################
Codigos utilizados en la unidad de investigacion I - Bioinformatica Unab
Nestor Palominos 2017-2018
########################################################################

Se presentan los codigos de filtrado para archivos de expresiones de Pseudomonas Syringae Tomato DC300

Filtro01: Corresponde a un match entre la planilla base y el archivo de anotaciones disponible en pseudomonas.com, tal de aislar solamente aquellos genes pertenecientes a Pseudomonas Syringae, puesto a que en la planilla original aparecen tambien de otras especies, tales como Homo Sapiens o E. Coli

Filtro01: Corresponde a un filtrado de aquellos genes con expresion distinta a cero y marcados como reviewed por Uniprot, tal de hacer match con la base de datos de interacciones proteina.proteina STRING. El csv de salida, luego fue analizado usando Cytoscape

Cobra: Creacion del modelo en formato SBML de la red de reacciones y metabolitos de Pseudomonas Syringae tomato DC3000 utilizando el paquete de optimizacion COBRA

comentarios a nestor.palominos@gmail.com
