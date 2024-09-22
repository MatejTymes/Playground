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

    bgC=(240,255,220)
    fill_rect(0,0,320,220,bgC)

    # grid - back side
    for wz in (wZA,wZB):
        line_3d_opaq(wXA-wXOvfl,wYA,wz,wXB+wXOvfl,wYA,wz,wOpac,(0,0,0))
        line_3d_opaq(wXA,wYA-wYOvfl,wz,wXA,wYB+wYOvfl,wz,wOpac,(0,0,0))
    for (wx,wy) in [(wXA,wYA),(wXA,wYB),(wXB,wYA)]:
        line_3d_opaq(wx,wy,wZA-wZOvfl,wx,wy,wZB+wZOvfl,wOpac,(0,0,0))

    # wireframe

    xDist,yDist,zDist=xMax-xMin,yMax-yMin,zMax-zMin
    steps=drawSteps

    # calculate the values
    xVals=[0]*(steps+2)
    yVals=[0]*(steps+2)
    zVals=[[0]*(steps+2) for k in range(steps+2)]
    for s in range(steps+2):
        xVals[s]=s*xDist/(steps+1)+xMin
        yVals[s]=s*yDist/(steps+1)+yMin
    for xInd in range(steps+2):
        xVal=xVals[xInd]
        for yInd in range(steps+2):
            yVal=yVals[yInd]
            zVals[xInd][yInd]=f3d(xVal,yVal)

    # draw the values - new approach
    for ind in range(steps+1):
        xInd,yInd=0,ind
        while yInd>=0:
            xValA,xValB=xVals[xInd],xVals[xInd+1]
            yValA,yValB=yVals[yInd],yVals[yInd+1]
            zValAA=zVals[xInd][yInd]
            zValAB=zVals[xInd][yInd+1]
            zValBA=zVals[xInd+1][yInd]

            pxA=wXDist*(xValA-xMin)/xDist+wXA
            pxB=wXDist*(xValB-xMin)/xDist+wXA
            pyA=wYDist*(yValA-yMin)/yDist+wYA
            pyB=wYDist*(yValB-yMin)/yDist+wYA
            pzAA=wZDist*(zValAA-zMin)/zDist+wZA
            pzAB=wZDist*(zValAB-zMin)/zDist+wZA
            pzBA=wZDist*(zValBA-zMin)/zDist+wZA

            line_3d(pxA,pyA,pzAA,pxA,pyB,pzAB,(0,180,0))
            line_3d(pxA,pyA,pzAA,pxB,pyA,pzBA,(0,0,180))

            xInd+=1
            yInd-=1

    for ind in range(steps+1):
        xInd,yInd=1+ind,steps+1
        while xInd<=steps+1:
            xValA,xValB=xVals[xInd-1],xVals[xInd]
            yValA,yValB=yVals[yInd-1],yVals[yInd]
            zValAB=zVals[xInd-1][yInd]
            zValBA=zVals[xInd][yInd-1]
            zValBB=zVals[xInd][yInd]

            pxA=wXDist*(xValA-xMin)/xDist+wXA
            pxB=wXDist*(xValB-xMin)/xDist+wXA
            pyA=wYDist*(yValA-yMin)/yDist+wYA
            pyB=wYDist*(yValB-yMin)/yDist+wYA
            pzAB=wZDist*(zValAB-zMin)/zDist+wZA
            pzBA=wZDist*(zValBA-zMin)/zDist+wZA
            pzBB=wZDist*(zValBB-zMin)/zDist+wZA

            line_3d(pxB,pyA,pzBA,pxB,pyB,pzBB,(0,180,0))
            line_3d(pxA,pyB,pzAB,pxB,pyB,pzBB,(0,0,180))

            xInd+=1
            yInd-=1

    # grid - front side
    for wz in (wZA,wZB):
        line_3d_opaq(wXA-wXOvfl,wYB,wz,wXB+wXOvfl,wYB,wz,wOpac,(0,0,0))
        line_3d_opaq(wXB,wYA-wYOvfl,wz,wXB,wYB+wYOvfl,wz,wOpac,(0,0,0))
    line_3d_opaq(wXB,wYB,wZA-wZOvfl,wXB,wYB,wZB+wZOvfl,wOpac,(0,0,0))

    # draw_string("x=0",260,160,(180,0,0),bgC)
    # draw_string("y=0",260,180,(180,0,0),bgC)
    # draw_string("z=3",260,200,(180,0,0),bgC)


# todo: add tracing functionality
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

