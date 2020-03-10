# Pregunta un dato hasta que sea correcto, haciendo validaciones usando
# expresiones regulares.

# Importa el módulo requerido para usar Expresiones regulares.
importar  re

def  main ():
  # Infinty Loop - Itera hasta que se presenta un break
  # Estará preguntando el dato, mientras no cumpla con el patrón de la
  # Expedición regular.
  mientras  cierto :
    strRFC  =  input ( "Dame el RFC:" )
    coincidir  =  re . búsqueda ( "^ [AZ] {4} - [0-9] {6} - [A-Z0-9] {3} $" , strRFC )
    si ( coincidir ):
      print ( "RFC Correcto!" )
      descanso
    más :
      print ( "RFC incorrecto. Intenta de nuevo." )
