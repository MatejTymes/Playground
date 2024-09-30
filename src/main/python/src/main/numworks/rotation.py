from kandinsky import *
from math import sqrt,sin,cos,pi
from time import sleep

# center points
cx,cy=int(320/2),int(220/2)

sun=(0,0)
p0=(-50,0)
p1=(90,0)
p2=(0,150)
m2=(0,20)


bgC=(255,255,255)
shadowC=(240,240,240)
sunC=(50,50,180)
p0C=(0,180,120)
p1C=(0,180,250)
p2C=(0,250,180)
m2C=(180,50,50)

p0Rot=150
p1Rot=315
p2Rot=315
m2Rot=0

# aRot=315
# acX,acY,aOpac=280,189,60
# aXC=(50,0,140)
# aYC=(50,140,0)


# def sinCos(rot):
#     rad=-rot*pi/180
#     return (sin(rad),cos(rad))

def rotX(x,y,sinRot,cosRot):
    return int(x*cosRot-y*sinRot)

def rotY(x,y,sinRot,cosRot):
    return int((x*sinRot+y*cosRot)*0.45)

def rotatePoint(x,y,rot):
    rad=-rot*pi/180
    sinRot=sin(rad)
    cosRot=cos(rad)
    return (rotX(x,y,sinRot,cosRot),rotY(x,y,sinRot,cosRot))

# def rotatePoint2(x,y,sinRot,cosRot):
#     return (rotX(x,y,sinRot,cosRot),rotY(x,y,sinRot,cosRot))

# def line(x1,y1,x2,y2,c):
#     w=x2-x1
#     h=y2-y1
#     if abs(w)>=abs(h):
#         d=h/w
#         for i in range(0,w,(w>0)*2-1):
#             set_pixel(x1+i,y1+int(d*i+0.5),c)
#     else:
#         d=w/h
#         for i in range(0,h,(h>0)*2-1):
#             set_pixel(x1+int(d*i+0.5),y1+i,c)
# try:
#     line=draw_line
# except:
#     pass


p0R=rotatePoint(p0[0],p0[1],p0Rot)
p1R=rotatePoint(p1[0],p1[1],p1Rot)
p2R=rotatePoint(p2[0],p2[1],p2Rot)
m2R=rotatePoint(m2[0],m2[1],m2Rot)
# aSinCos=sinCos(aRot)

while True:
    # draw_string("rot="+str(rot)+"  ",0,0,textC)
    fill_rect(sun[0]+cx-10,sun[1]+cy-10,20,20,sunC)
    fill_rect(p0R[0]+cx-3,p0R[1]+cy-3,6,6,p0C)
    fill_rect(p1R[0]+cx-4,p1R[1]+cy-4,8,8,p1C)
    fill_rect(p2R[0]+cx-5,p2R[1]+cy-5,10,10,p2C)
    fill_rect(p2R[0]+cx+m2R[0]-2,p2R[1]+cy+m2R[1]-2,4,4,m2C)

    # axMin=rotatePoint2(-10,0,aSinCos[0],aSinCos[1])
    # axMax=rotatePoint2(35,0,aSinCos[0],aSinCos[1])
    # axArr1=rotatePoint2(35*2/3,-5,aSinCos[0],aSinCos[1])
    # axArr2=rotatePoint2(35*2/3,5,aSinCos[0],aSinCos[1])
    # line(axMin[0]+acX,axMin[1]+acY,axMax[0]+acX,axMax[1]+acY,aXC)
    # line(axArr1[0]+acX,axArr1[1]+acY,axMax[0]+acX,axMax[1]+acY,aXC)
    # line(axArr2[0]+acX,axArr2[1]+acY,axMax[0]+acX,axMax[1]+acY,aXC)
    # line(axArr1[0]+acX,axArr1[1]+acY,axArr2[0]+acX,axArr2[1]+acY,aXC)
    # ayMin=rotatePoint2(0,-10,aSinCos[0],aSinCos[1])
    # ayMax=rotatePoint2(0,35,aSinCos[0],aSinCos[1])
    # ayArr1=rotatePoint2(-5,35*2/3,aSinCos[0],aSinCos[1])
    # ayArr2=rotatePoint2(5,35*2/3,aSinCos[0],aSinCos[1])
    # line(ayMin[0]+acX,ayMin[1]+acY,ayMax[0]+acX,ayMax[1]+acY,aYC)
    # line(ayArr1[0]+acX,ayArr1[1]+acY,ayMax[0]+acX,ayMax[1]+acY,aYC)
    # line(ayArr2[0]+acX,ayArr2[1]+acY,ayMax[0]+acX,ayMax[1]+acY,aYC)
    # line(ayArr1[0]+acX,ayArr1[1]+acY,ayArr2[0]+acX,ayArr2[1]+acY,aYC)

    sleep(0.05)
    p0Rot+=6
    if p0Rot>=360:
        p0Rot-=360
    p1Rot+=5
    if p1Rot>=360:
        p1Rot-=360
    p2Rot+=4
    if p2Rot>=360:
        p2Rot-=360
    m2Rot+=15
    if m2Rot>=360:
        m2Rot-=360
    # aRot+=5
    # if aRot>=360:
    #     aRot-=360
    p0RN=rotatePoint(p0[0],p0[1],p0Rot)
    p1RN=rotatePoint(p1[0],p1[1],p1Rot)
    p2RN=rotatePoint(p2[0],p2[1],p2Rot)
    m2RN=rotatePoint(m2[0],m2[1],m2Rot)
    # aSinCosN=sinCos(aRot)

    # fill_rect(sun[0]+cx-10,sun[1]+cy-10,20,20,bgC)
    fill_rect(p0R[0]+cx-3,p0R[1]+cy-3,6,6,shadowC)
    fill_rect(p1R[0]+cx-4,p1R[1]+cy-4,8,8,shadowC)
    fill_rect(p2R[0]+cx-5,p2R[1]+cy-5,10,10,shadowC)
    fill_rect(p2R[0]+cx+m2R[0]-2,p2R[1]+cy+m2R[1]-2,4,4,shadowC)

    # line(axMin[0]+acX,axMin[1]+acY,axMax[0]+acX,axMax[1]+acY,bgC)
    # line(axArr1[0]+acX,axArr1[1]+acY,axMax[0]+acX,axMax[1]+acY,bgC)
    # line(axArr2[0]+acX,axArr2[1]+acY,axMax[0]+acX,axMax[1]+acY,bgC)
    # line(axArr1[0]+acX,axArr1[1]+acY,axArr2[0]+acX,axArr2[1]+acY,bgC)

    # line(ayMin[0]+acX,ayMin[1]+acY,ayMax[0]+acX,ayMax[1]+acY,bgC)
    # line(ayArr1[0]+acX,ayArr1[1]+acY,ayMax[0]+acX,ayMax[1]+acY,bgC)
    # line(ayArr2[0]+acX,ayArr2[1]+acY,ayMax[0]+acX,ayMax[1]+acY,bgC)
    # line(ayArr1[0]+acX,ayArr1[1]+acY,ayArr2[0]+acX,ayArr2[1]+acY,bgC)

    p0R,p1R,p2R,m2R=p0RN,p1RN,p2RN,m2RN
    # aSinCos=aSinCosN