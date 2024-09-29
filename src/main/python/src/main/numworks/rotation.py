from kandinsky import *
from math import sqrt,sin,cos,pi
from time import sleep

# center points
cx,cy=int(320/2),int(220/2)

rot=315


def rotX(x,y,sinRot,cosRot):
    return int(x*cosRot-y*sinRot)
def rotY(x,y,sinRot,cosRot):
    return int((x*sinRot+y*cosRot)*0.4)

def rotatePoint(x,y,rot):
    rad=-rot*pi/180
    sinRot=sin(rad)
    cosRot=cos(rad)
    return (rotX(x,y,sinRot,cosRot),rotY(x,y,sinRot,cosRot))


sun=(0,0)
p1=(90,0)
m1=(0,30)
p2=(0,150)


sunC=(50,50,180)
p1C=(0,180,250)
m1C=(180,50,50)
p2C=(0,250,180)
bgC=(255,255,255)

p1Rot=315
m1Rot=0
p2Rot=315
p1R=rotatePoint(p1[0],p1[1],p1Rot)
m1R=rotatePoint(m1[0],m1[1],m1Rot)
p2R=rotatePoint(p2[0],p2[1],p2Rot)

while True:
    # draw_string("rot="+str(rot)+"  ",0,0,textC)
    fill_rect(sun[0]+cx-10,sun[1]+cy-10,20,20,sunC)
    fill_rect(p1R[0]+cx-4,p1R[1]+cy-4,8,8,p1C)
    fill_rect(p1R[0]+cx+m1R[0]-2,p1R[1]+cy+m1R[1]-2,4,4,m1C)
    fill_rect(p2R[0]+cx-5,p2R[1]+cy-5,10,10,p2C)

    sleep(0.05)
    p1Rot+=3
    if p1Rot>=360:
        p1Rot-=360
    m1Rot+=10
    if m1Rot>=360:
        m1Rot-=360
    p2Rot+=5
    if p2Rot>=360:
        p2Rot-=360
    p1RN=rotatePoint(p1[0],p1[1],p1Rot)
    m1RN=rotatePoint(m1[0],m1[1],m1Rot)
    p2RN=rotatePoint(p2[0],p2[1],p2Rot)

    fill_rect(sun[0]+cx-10,sun[1]+cy-10,20,20,bgC)
    fill_rect(p1R[0]+cx-4,p1R[1]+cy-4,8,8,bgC)
    fill_rect(p1R[0]+cx+m1R[0]-2,p1R[1]+cy+m1R[1]-2,4,4,bgC)
    fill_rect(p2R[0]+cx-5,p2R[1]+cy-5,10,10,bgC)

    p1R,m1R,p2R=p1RN,m1RN,p2RN