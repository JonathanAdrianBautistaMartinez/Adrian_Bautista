# Utiliza la función formato de una cadena, para poner valores
# en una salida.

def  main ():
  intBase  =  7
  intAltura  =  5
  fltAreaTriangulo = ( intBase * intAltura ) / 2
  txt  =  "Área: {2: 0.2f} ({0} por {1} entre dos)"
  print ( formato txt . ( intBase , intAltura , fltAreaTriangulo ))

# El orden de los parámetros proporcionados a formato es de base cero.
# formula {2: 0,0f} es una flotante sin decimales.
