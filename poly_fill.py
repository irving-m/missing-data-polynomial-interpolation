import pandas as pd
import Lagrange

def poly_fill ( data , puntos ) : # el n m e r o de puntos debe ser par
  redf = data
  for column in data : # itera por columnas
    for i in data . index : # itera por filas
      if pd . isna ( data [ column ][ i ]) : # detectar valores nulos
        t = [] # independent variable
        x = [] # dependent variable
        k = 0 # search  radius

        while len ( t ) < puntos /2: # encontrar puntos por la derecha para interpolar
          k = k + 1
          if i + k <= len ( data . index ) - 1:
            if pd . notna ( data [ column ][ i + k ]) :
              t . append ( i + k )
              x . append ( data [ column ][ i + k ])
          else :
            break

        k = 0
        while len ( t ) < puntos : # encontrar puntos por la izquierda para interpolar
        k = k - 1
          if i + k >= 0:
            if pd . notna ( data [ column ][ i + k ]) :
              t . append ( i + k )
              x . append ( data [ column ][ i + k ])
          else :
            break

        intpol = Lagrange . lagrange (t , x , i )
        redf . _set_value (i , column , intpol )
  return redf
