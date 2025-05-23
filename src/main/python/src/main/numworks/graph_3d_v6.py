from kandinsky import *
from math import sqrt,sin,cos,pi
from ion import *
# from time import sleep

# center points
cx,cy=320/2,220/2

# 3d wireframe edges
wXA,wXB,wXOvfl=-100,100,15
wYA,wYB,wYOvfl=-100,100,15
wZA,wZB,wZOvfl=-40,40,10

bgC=(240,255,220)
wOpac=20
wC=(0,0,0)
xlC,ylC=(0,0,180),(0,180,0)
tOpac=60
tC=(255,0,0)
ttC=(180,0,0)
mC=(255,255,255)
mBgC=(255,188,63)

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

iSq2=1/sqrt(2)

def line_3d(x1,y1,z1,x2,y2,z2,c):
    rx1=(x1-y1)*iSq2+cx
    rx2=(x2-y2)*iSq2+cx
    ry1=(y1+x1)*iSq2*0.4+cy-z1
    ry2=(y2+x2)*iSq2*0.4+cy-z2
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
                ((oc[0]*rOpac)+(c[0]*opac))*0.01,
                ((oc[1]*rOpac)+(c[1]*opac))*0.01,
                ((oc[2]*rOpac)+(c[2]*opac))*0.01
            )
            set_pixel(px,py,nc)
    else:
        d=w/h
        for i in range(0,h,(h>0)*2-1):
            px,py=x1+int(d*i+0.5),y1+i
            oc=get_pixel(px,py)
            nc=(
                ((oc[0]*rOpac)+(c[0]*opac))*0.01,
                ((oc[1]*rOpac)+(c[1]*opac))*0.01,
                ((oc[2]*rOpac)+(c[2]*opac))*0.01
            )
            set_pixel(px,py,nc)

def line_3d_opaq(x1,y1,z1,x2,y2,z2,opac,c):
    rx1=(x1-y1)*iSq2+cx
    rx2=(x2-y2)*iSq2+cx
    ry1=(y1+x1)*iSq2*0.4+cy-z1
    ry2=(y2+x2)*iSq2*0.4+cy-z2
    line_opaq(int(rx1),int(ry1),int(rx2),int(ry2),opac,c)
    # sleep(0.03)

def drawValues(steps,xVals,yVals,zVals,xMin,yMin,zMin,xDist,yDist,zDist):
    fill_rect(0,0,320,220,bgC)

    # grid - back side
    for wz in (wZA,wZB):
        line_3d_opaq(wXA-wXOvfl,wYA,wz,wXB+wXOvfl,wYA,wz,wOpac,wC)
        line_3d_opaq(wXA,wYA-wYOvfl,wz,wXA,wYB+wYOvfl,wz,wOpac,wC)
    for (wx,wy) in [(wXA,wYA),(wXA,wYB),(wXB,wYA)]:
        line_3d_opaq(wx,wy,wZA-wZOvfl,wx,wy,wZB+wZOvfl,wOpac,wC)

    iXDist=1/xDist
    iYDist=1/yDist
    iZDist=1/zDist
    iSPls1=1/(steps+1)

    # draw wireframe - new approach
    for ind in range(steps+1):
        xInd,yInd=0,ind
        while yInd>=0:
            xValA,xValB=xVals[xInd],xVals[xInd+1]
            yValA,yValB=yVals[yInd],yVals[yInd+1]
            zValAA=zVals[xInd][yInd]
            zValAB=zVals[xInd][yInd+1]
            zValBA=zVals[xInd+1][yInd]

            pxA=wXDist*(xValA-xMin)*iXDist+wXA
            pxB=wXDist*(xValB-xMin)*iXDist+wXA
            pyA=wYDist*(yValA-yMin)*iYDist+wYA
            pyB=wYDist*(yValB-yMin)*iYDist+wYA
            pzAA=wZDist*(zValAA-zMin)*iZDist+wZA
            pzAB=wZDist*(zValAB-zMin)*iZDist+wZA
            pzBA=wZDist*(zValBA-zMin)*iZDist+wZA

            line_3d(pxA,pyA,pzAA,pxA,pyB,pzAB,ylC)
            line_3d(pxA,pyA,pzAA,pxB,pyA,pzBA,xlC)

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

            pxA=wXDist*(xValA-xMin)*iXDist+wXA
            pxB=wXDist*(xValB-xMin)*iXDist+wXA
            pyA=wYDist*(yValA-yMin)*iYDist+wYA
            pyB=wYDist*(yValB-yMin)*iYDist+wYA
            pzAB=wZDist*(zValAB-zMin)*iZDist+wZA
            pzBA=wZDist*(zValBA-zMin)*iZDist+wZA
            pzBB=wZDist*(zValBB-zMin)*iZDist+wZA

            line_3d(pxB,pyA,pzBA,pxB,pyB,pzBB,ylC)
            line_3d(pxA,pyB,pzAB,pxB,pyB,pzBB,xlC)

            xInd+=1
            yInd-=1

    # grid - front side
    for wz in (wZA,wZB):
        line_3d_opaq(wXA-wXOvfl,wYB,wz,wXB+wXOvfl,wYB,wz,wOpac,wC)
        line_3d_opaq(wXB,wYA-wYOvfl,wz,wXB,wYB+wYOvfl,wz,wOpac,wC)
    line_3d_opaq(wXB,wYB,wZA-wZOvfl,wXB,wYB,wZB+wZOvfl,wOpac,wC)

def drawTracer(xInd,yInd,xVals,yVals,zVals,xMin,yMin,zMin,xDist,yDist,zDist):
    xVal,yVal,zVal=xVals[xInd],yVals[yInd],zVals[xInd][yInd]
    draw_string("x="+str(xVal),0,0,ttC,bgC)
    draw_string("y="+str(yVal),0,20,ttC,bgC)
    draw_string("z="+str(zVal),0,200,ttC,bgC)

    px=wXDist*(xVal-xMin)/xDist+wXA
    py=wYDist*(yVal-yMin)/yDist+wYA
    pz=wZDist*(zVal-zMin)/zDist+wZA
    line_3d_opaq(px,py,pz-5,px,py,pz+5,tOpac,tC)
    line_3d_opaq(px-5,py,pz,px+5,py,pz,tOpac,tC)
    line_3d_opaq(px,py-5,pz,px,py+5,pz,tOpac,tC)

def calulateValues(f3d,xVals,yVals,zVals,steps,xDist,yDist,xMin,yMin):
    zHigh,zLow=0,0
    firstValue=True
    for s in range(steps+2):
        xVals[s]=s*xDist/(steps+1)+xMin
        yVals[s]=s*yDist/(steps+1)+yMin
    for xInd in range(steps+2):
        xVal=xVals[xInd]
        for yInd in range(steps+2):
            yVal=yVals[yInd]
            z=f3d(xVal,yVal)
            if firstValue:
                zHigh=z
                zLow=z
                firstValue=False
            else:
                if z<zLow:
                    zLow=z
                else:
                    if z>zHigh:
                        zHigh=z
            zVals[xInd][yInd]=z
    return (zLow,zHigh)

def hanleKeyPress(pressedKeys,keyToCheck):
    if pressedKeys[keyToCheck]:
        pressedKeys[keyToCheck]=False
        return True
    return False

def drawModeIcon(mode):
    modeString="m" if mode=="move" else ("t" if mode=="trace" else "?")
    draw_string(modeString,305,5,mC,mBgC)

def draw3dGraph(f3d,xRange,yRange,zRange,steps):
    xVals=[0]*(steps+2)
    yVals=[0]*(steps+2)
    zVals=[[0]*(steps+2) for k in range(steps+2)]

    # prepare values
    xMin,xMax=xRange[0],xRange[1]
    yMin,yMax=yRange[0],yRange[1]
    zMin,zMax=-1,1
    xDist,yDis,zDist=xMax-xMin,yMax-yMin,zMax-zMin
    xInd,yInd=0,0

    mode="move"
    recalculateValues,redrawGraph=True,True
    redrawTracer=False
    # okHeld,exeHeld,leftHeld,rightHeld,upHeld,downHeld=False,False,False,False,False,False
    pressed={KEY_OK:False,KEY_EXE:False,KEY_LEFT:False,KEY_RIGHT:False,KEY_UP:False,KEY_DOWN:False,KEY_PLUS:False,KEY_MINUS:False}
    handlePress={KEY_OK:False,KEY_EXE:False,KEY_LEFT:False,KEY_RIGHT:False,KEY_UP:False,KEY_DOWN:False,KEY_PLUS:False,KEY_MINUS:False}
    while True:
        if recalculateValues:
            xDist,yDist=xMax-xMin,yMax-yMin
            zOut = calulateValues(f3d,xVals,yVals,zVals,steps,xDist,yDist,xMin,yMin)
            zMin,zMax=zOut[0],zOut[1]
            if zRange!="auto":
                zMin,zMax=zRange[0],zRange[1]
            if zMin==zMax:
                zMin-=1
                zMax+=1
            zDist=zMax-zMin
            xInd,yInd=int(len(xVals)*0.5),int(len(yVals)*0.5)
            recalculateValues=False
        if redrawGraph:
            drawValues(steps,xVals,yVals,zVals,xMin,yMin,zMin,xDist,yDist,zDist)
            drawModeIcon(mode)
            redrawGraph=False
        if redrawTracer:
            drawTracer(xInd,yInd,xVals,yVals,zVals,xMin,yMin,zMin,xDist,yDist,zDist)
            redrawTracer=False

        for key, alreadyPressed in pressed.items():
            if keydown(key):
                if not alreadyPressed:
                    pressed[key]=True
                    handlePress[key]=True
            else:
                if alreadyPressed:
                    pressed[key]=False

        if hanleKeyPress(handlePress,KEY_OK) or hanleKeyPress(handlePress,KEY_EXE):
            if mode=="move":
                mode="trace"
                drawModeIcon(mode)
                redrawTracer=True
            else:
                mode="move"
                redrawGraph=True
            handlePress[KEY_LEFT]=False
            handlePress[KEY_RIGHT]=False
            handlePress[KEY_UP]=False
            handlePress[KEY_DOWN]=False
            handlePress[KEY_PLUS]=False
            handlePress[KEY_MINUS]=False
        if mode=="trace":
            if hanleKeyPress(handlePress,KEY_LEFT) and xInd>0:
                xInd-=1
                redrawGraph=True
                redrawTracer=True
            if hanleKeyPress(handlePress,KEY_RIGHT) and xInd+1<len(xVals):
                xInd+=1
                redrawGraph=True
                redrawTracer=True
            if hanleKeyPress(handlePress,KEY_UP) and yInd>0:
                yInd-=1
                redrawGraph=True
                redrawTracer=True
            if hanleKeyPress(handlePress,KEY_DOWN) and yInd+1<len(yVals):
                yInd+=1
                redrawGraph=True
                redrawTracer=True
        elif mode=="move":
            if hanleKeyPress(handlePress,KEY_LEFT):
                xMin-=xDist/8
                xMax-=xDist/8
                recalculateValues=True
                redrawGraph=True
            if hanleKeyPress(handlePress,KEY_RIGHT):
                xMin+=xDist/8
                xMax+=xDist/8
                recalculateValues=True
                redrawGraph=True
            if hanleKeyPress(handlePress,KEY_UP):
                yMin-=yDist/8
                yMax-=yDist/8
                recalculateValues=True
                redrawGraph=True
            if hanleKeyPress(handlePress,KEY_DOWN):
                yMin+=yDist/8
                yMax+=yDist/8
                recalculateValues=True
                redrawGraph=True
        if hanleKeyPress(handlePress,KEY_PLUS):
            xMin+=xDist/4
            xMax-=xDist/4
            yMin+=yDist/4
            yMax-=yDist/4
            recalculateValues=True
            redrawGraph=True
            mode="move"
        if hanleKeyPress(handlePress,KEY_MINUS):
            xMin-=xDist/2
            xMax+=xDist/2
            yMin-=yDist/2
            yMax+=yDist/2
            recalculateValues=True
            redrawGraph=True
            mode="move"

draw3dGraph(
    # lambda x,y: sin(y-x)+cos(x)+cos(y),
    # (-3,3),(-3,3),(-3,3),15
    # lambda x,y: sin(y-x)+cos(x),
    # (-3,3),(-3,3),"auto",15
    # lambda x,y: -x*x-y*y,
    # (-3,3),(-3,3),"auto",11
    # lambda x,y: -5*sin(y-x)-10*cos(x),
    # (-5,5),(-5,5),"auto",15
    lambda x,y: (x*x*sin(x))+(y*y*sin(y)),
    (-6,6),(-6,6),"auto",23
    # lambda x,y: cos(sqrt(x*x+y*y)),
    # (-3*pi,3*pi),(-3*pi,3*pi),(-6,6),23
)

