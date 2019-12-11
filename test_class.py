class ball():
    m=0
    Vx=0
    Vy=0
    Vz=0

class my_ball(ball):
    m=100

    def momentum_x(self):
        return self.m*self.Vx
    
apple=my_ball()
apple.Vx=50

print(apple.m,apple.Vx,apple.Vy,apple.Vz,apple.momentum_x())
