# hismetag-corpus
Corpus anotados manualmente para la evaluación de HisMeTag. Cálculo del acuerdo entre anotadores humanos.

La carpeta agreement incluye el script que extrae las etiquetas para las anotaciones de Pablo y Elena y obtiene el cálculo del acuerdo entre anotadores. El fichero output.txt devuelve la lista de triples con anotador, posición en el fichero y etiqueta y las cifras de kappa.

IMPORTANTE: si lo que interesa es:
- el corpus manualmente anotado por Pablo y por Elena A. -> véase la carpeta manually_tagged/agreement/corpus_agreement
- el cálculo del agreement -> véase la carpeta manually_tagged/agreement donde está el archivo `agreement.py` (prolijamente documentado) y `output.txt` con la salida de las triplas generadas y el agreement (kappa y alpha) obtenido. 
