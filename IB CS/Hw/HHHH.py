import turtle as t
t.speed(5)
def Draw(size,center):
    t.goto(center)
    t.pendown()
    t.setheading(0)
    t.fd(size/4)
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.penup()
    t.fd(size/2)
    t.pendown()
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.penup()
    t.fd(size/2)
    t.pendown()
    t.rt(90)
    t.fd(size/2)
    t.rt(90)
    t.fd(size/2)
    t.penup()
    

def endpoints(length,center):
    endpoint1 = (center[0] + length / 4, center[1] + length / 2)
    endpoint2 = (center[0] + length / 4, center[1] - length / 2)
    endpoint3 = (center[0] - length / 4, center[1] + length / 2)
    endpoint4 = (center[0] - length / 4, center[1] - length / 2)
    endpoint = [endpoint1, endpoint2, endpoint3, endpoint4]
    return endpoint

def repeat(times,length,center):
    if times == 0:
        pass
    else:
        Draw(length, center)
        times-=1
        repeat(times,length/2,endpoints(length,center)[0])
        repeat(times,length/2,endpoints(length,center)[1])
        repeat(times,length/2,endpoints(length,center)[2])
        repeat(times,length/2,endpoints(length,center)[3])
def loop(times,length,center):
    Draw(length, center)
    for i in range(times):
        Draw(length/2,endpoints(length,center)[0])
        Draw(length/2,endpoints(length,center)[1])
        Draw(length/2,endpoints(length,center)[2])
        Draw(length/2,endpoints(length,center)[3])
        length=length/2

repeat(3,100,(0,0))


#loop(3,100,(0,0))      
t.mainloop()
