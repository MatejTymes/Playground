from kandinsky import *
from math import sqrt,sin,cos,pi
# from time import sleep

# center points
cx,cy=320/2,220/2

# 3d wireframe edges
wXA,wXB,wXOvfl=-100,100,15
wYA,wYB,wYOvfl=-100,100,15
wZA,wZB,wZOvfl=-40,40,10
wOpac=20

wXDist,wYDist,wZDist=wXB-wXA,wYB-wYA,wZB-wZA

def line(x1,y1,x2,y2,c):
    w=x2-x1
    h=y2-y1
    if abs(w)>=abs(h):
        d=h/w
        for i in range(0,w,(w>0)*2-1):
            set_pixel(x1+i,y1+int(d*i+0.5),c)
    else:
        d=w/h
        for i in range(0,h,(h>0)*2-1):
            set_pixel(x1+int(d*i+0.5),y1+i,c)

try:
    line=draw_line
except:
    pass

sq2 = sqrt(2)

def line_3d(x1,y1,z1,x2,y2,z2,c):
    rx1=(x1-y1)/sq2+cx
    rx2=(x2-y2)/sq2+cx
    ry1=(y1+x1)/sq2/2.5+cy-z1
    ry2=(y2+x2)/sq2/2.5+cy-z2
    line(int(rx1),int(ry1),int(rx2),int(ry2),c)
    # sleep(0.03)

def line_opaq(x1,y1,x2,y2,opac,c):
    w=x2-x1
    h=y2-y1
    rOpac=100-opac
    if abs(w)>=abs(h):
        d=h/w
        for i in range(0,w,(w>0)*2-1):
            px,py=x1+i,y1+int(d*i+0.5)
            oc=get_pixel(px,py)
            nc=(
                ((oc[0]*rOpac)+(c[0]*opac))/100,
                ((oc[1]*rOpac)+(c[1]*opac))/100,
                ((oc[2]*rOpac)+(c[2]*opac))/100
            )
            set_pixel(px,py,nc)
    else:
        d=w/h
        for i in range(0,h,(h>0)*2-1):
            px,py=x1+int(d*i+0.5),y1+i
            oc=get_pixel(px,py)
            nc=(
                ((oc[0]*rOpac)+(c[0]*opac))/100,
                ((oc[1]*rOpac)+(c[1]*opac))/100,
                ((oc[2]*rOpac)+(c[2]*opac))/100
            )
            set_pixel(px,py,nc)

def line_3d_opaq(x1,y1,z1,x2,y2,z2,opac,c):
    rx1=(x1-y1)/sq2+cx
    rx2=(x2-y2)/sq2+cx
    ry1=(y1+x1)/sq2/2.5+cy-z1
    ry2=(y2+x2)/sq2/2.5+cy-z2
    line_opaq(int(rx1),int(ry1),int(rx2),int(ry2),opac,c)
    # sleep(0.03)

def draw3dGraph(f3d,xRange,yRange,zRange,drawSteps):
    xMin,xMax=xRange[0],xRange[1]
    yMin,yMax=yRange[0],yRange[1]
    zMin,zMax=zRange[0],zRange[1]

    fill_rect(0,0,320,220,(240,255,220))

    # grid - back side
    for wz in (wZA,wZB):
        # line_3d(wXA-wXOvfl,wYA,wz,wXB+wXOvfl,wYA,wz,(100,100,100))
        # line_3d(wXA,wYA-wYOvfl,wz,wXA,wYB+wYOvfl,wz,(100,100,100))
        line_3d_opaq(wXA-wXOvfl,wYA,wz,wXB+wXOvfl,wYA,wz,wOpac,(0,0,0))
        line_3d_opaq(wXA,wYA-wYOvfl,wz,wXA,wYB+wYOvfl,wz,wOpac,(0,0,0))
    for (wx,wy) in [(wXA,wYA),(wXA,wYB),(wXB,wYA)]:
        # line_3d(wx,wy,wZA-wZOvfl,wx,wy,wZB+wZOvfl,(100,100,100))
        line_3d_opaq(wx,wy,wZA-wZOvfl,wx,wy,wZB+wZOvfl,wOpac,(0,0,0))

    # wireframe

    xDist,yDist,zDist=xMax-xMin,yMax-yMin,zMax-zMin
    steps=drawSteps
    for s in range(steps):
        xS=s*xDist/(steps-1)+xMin
        pxS=wXDist*(xS-xMin)/xDist+wXA
        for s2 in range(steps-1):
            yS1=s2*yDist/(steps-1)+yMin
            yS2=(s2+1)*yDist/(steps-1)+yMin
            z1=f3d(xS,yS1)
            z2=f3d(xS,yS2)

            pyS1=wYDist*(yS1-yMin)/yDist+wYA
            pyS2=wYDist*(yS2-yMin)/yDist+wYA
            pz1=wZDist*(z1-zMin)/zDist+wZA
            pz2=wZDist*(z2-zMin)/zDist+wZA

            line_3d(pxS,pyS1,pz1,pxS,pyS2,pz2,(0,180,0))

        yS=s*yDist/(steps-1)+yMin
        pyS=wYDist*(yS-yMin)/yDist+wYA
        for s2 in range(steps-1):
            xS1=s2*xDist/(steps-1)+xMin
            xS2=(s2+1)*xDist/(steps-1)+xMin
            z1=f3d(xS1,yS)
            z2=f3d(xS2,yS)

            pxS1=wXDist*(xS1-xMin)/xDist+wXA
            pxS2=wXDist*(xS2-xMin)/xDist+wXA
            pz1=wZDist*(z1-zMin)/zDist+wZA
            pz2=wZDist*(z2-zMin)/zDist+wZA

            line_3d(pxS1,pyS,pz1,pxS2,pyS,pz2,(180,0,0))


    # grid - front side
    for wz in (wZA,wZB):
        # line_3d(wXA-wXOvfl,wYB,wz,wXB+wXOvfl,wYB,wz,(100,100,100))
        # line_3d(wXB,wYA-wYOvfl,wz,wXB,wYB+wYOvfl,wz,(100,100,100))
        line_3d_opaq(wXA-wXOvfl,wYB,wz,wXB+wXOvfl,wYB,wz,wOpac,(0,0,0))
        line_3d_opaq(wXB,wYA-wYOvfl,wz,wXB,wYB+wYOvfl,wz,wOpac,(0,0,0))
    # line_3d(wXB,wYB,wZA-wZOvfl,wXB,wYB,wZB+wZOvfl,(100,100,100))
    line_3d_opaq(wXB,wYB,wZA-wZOvfl,wXB,wYB,wZB+wZOvfl,wOpac,(0,0,0))


draw3dGraph(
    # lambda x,y: sin(y-x)+cos(x)+cos(y),
    # (-3,3),(-3,3),(-3,3),15
    # lambda x,y: sin(y-x)+cos(x),
    # (-3,3),(-3,3),(-2,2),15
    # lambda x,y: -x*x-y*y,
    # (-3,3),(-3,3),(-20,0),10
    lambda x,y: -5*sin(y-x)-10*cos(x),
    (-5,5),(-5,5),(-20,20),20
)
