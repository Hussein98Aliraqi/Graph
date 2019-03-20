import turtle
a=turtle.Turtle()
a.speed(100)  
a.penup()
a.left(180)
a.fd(100)
a.right(180)
a.pendown()
k=225
k2=16
r=15
for y in range(16):
    if y==0 or y==8:
        for i in range(k2):
            a.fd(r)
            a.left(120)
            a.fd(r)
            a.left(120)
            a.fd(r)
            a.left(120)
            a.fd(r)
    elif y==1 or y==9:
        b=0
        for i1 in range(k2):
            
            if b==0:
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                b=1
            else:
                a.penup()    
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.pendown()
                b=0
    elif y==2 or y==10:               
        b2=2
        for i2 in range(k2):
            if b2>0:
                c=2
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                b2=b2-1
            else:
                a.penup()    
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.pendown()
                c=c-1
                if c==0:
                    b2=2
    elif y==3 or y==11:
        b2=1
        for i2 in range(k2):
            if b2>0:
                c=3
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                b2=b2-1
            else:
                a.penup()    
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.pendown()
                c=c-1
                if c==0:
                    b2=1
    elif y==4 or y==12:               
        b2=4
        for i2 in range(k2):
            if b2>0:
                c=4
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                b2=b2-1
            else:
                a.penup()    
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.pendown()
                c=c-1
                if c==0:
                    b2=4
    elif y==5 or y==13:               
        b3=3
        for i2 in range(k2):
            if b3>0:
                if b3%2!=0:
                    c=5
                    a.fd(r)
                    a.left(120)
                    a.fd(r)
                    a.left(120)
                    a.fd(r)
                    a.left(120)
                    a.fd(r)
                    b3=b3-1
                else:
                    a.penup()
                    c=5
                    a.fd(r)
                    a.left(120)
                    a.fd(r)
                    a.left(120)
                    a.fd(r)
                    a.left(120)
                    a.fd(r)
                    b3=b3-1
                    a.pendown()
            else:
                a.penup()    
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.pendown()
                c=c-1
                if c==0:
                    b3=3  
    elif y==6 or y==14:               
        b2=2
        for i2 in range(k2):
            if b2>0:
                c=6
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                b2=b2-1
            else:
                a.penup()    
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.pendown()
                c=c-1
                if c==0:
                    b2=2
    elif y==7 or y==15:               
        b2=1
        for i2 in range(k2):
            if b2>0:
                c=7
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                b2=b2-1
            else:
                a.penup()    
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.left(120)
                a.fd(r)
                a.pendown()
                c=c-1
                if c==0:
                    b2=1
    k2=k2-1    
    a.penup()
    a.left(180)
    a.fd(k)
    a.right(180)
    a.pendown()
    a.left(120)
    a.fd(r)
    a.right(120)
    k=k-r
turtle.done()