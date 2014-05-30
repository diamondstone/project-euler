triangles=[]
for n in range(100000):
    triangles.append((n*(n+1))/2)
triangles=set(triangles)

pentagons=[]
for n in range(100000):
    pentagons.append((n*(3*n-1))/2)
pentagons=set(pentagons)

hexagons=[]
for n in range(100000):
    hexagons.append(n*(2*n-1))
hexagons=set(hexagons)

all=triangles.intersection(pentagons,hexagons)
print all
