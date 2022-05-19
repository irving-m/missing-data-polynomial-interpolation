def lagrange (x , y , xp ) :
  if len ( x ) != len ( y ) :
      print (" Longitudes de vectores diferentes ")
  else :
    yp = 0
    for j in range ( len ( y ) ) :
      p = 1
      for i in range ( len ( x ) ) :
        if i != j :
          p = p *( xp - x [ i ]) /( x [ j ] - x [ i ])
      yp += p * y [ j ]
    return yp
