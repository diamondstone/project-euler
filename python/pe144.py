from math import tan,atan,pi

def ellipseintersect(m,b): #returns the two points of intersection between the line y=mx+b and the ellipse 4x^2+y^2=100
#    (4+m^2)x^2+2mbx+b^2-100=0
    d=4*m**2*b**2-4*(4+m**2)*(b**2-100)
    x0=-m*b/(4+m**2)
    x1=x0-d**.5/2/(4+m**2)
    x2=x0+d**.5/2/(4+m**2)
    y1=m*x1+b
    y2=m*x2+b
    return ((x1,y1),(x2,y2))

def d(point1,point2):
    x1,y1=point1
    x2,y2=point2
    return ((x2-x1)**2+(y2-y1)**2)**.5

def line(x,y,m):
    b=y-m*x
    return (m,b)

def reflectslope(m_inc,m_surf):
    angle_inc=atan(m_inc)
    angle_perp=atan(-1/m_surf)
    return tan(2*angle_perp-angle_inc)

def reflect(x,y,m):
    p,p2=ellipseintersect(*line(x,y,m))
    d1=d(p,(x,y))
    d2=d(p2,(x,y))
    if d2>d1: p=p2
    x,y=p
    m=reflectslope(m,-4*x/y)
    return x,y,m

def main():
    bounces=1
    x,y,m=reflect(0,10.1,-19.7/1.4)
    while x<-.01 or x>.01:
        print "bounce",bounces,':',x,y,m
        x,y,m=reflect(x,y,m)
        bounces+=1

main()
