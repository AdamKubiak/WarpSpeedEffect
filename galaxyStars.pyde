import random

class Star:
    
    def __init__(self):
        self.x = random.randrange(-5000,5000)
        self.y = random.randrange(-5000,5000)
        self.z = random.randrange(0,2000)
        
    def reset(self):
        self.x = random.randrange(-5000,5000)
        self.y = random.randrange(-5000,5000)
        self.z = 2000.0
    
    def update(self):
        self.z-=10
        if self.z<= 0.0:
            self.reset()
    
    def drawStars(self):
        offsetX = 100.0*(self.x/self.z)
        offsetY = 100.0*(self.y/self.z)
        scaleZ = 0.0001*(2000.0-self.z)
        
        pushMatrix()
        translate(offsetX,offsetY)
        scale(scaleZ)
        ellipse(0,0,20,20)
        popMatrix()


stars = []

def setup():
    size(800,800)
    smooth()
    stroke(255)
    strokeWeight(5)
    
    for i in range(400):
        stars.append(Star())
        
def draw():
    background(0)
    
    translate(0.5*width,0.5*height)
    
    for i in range(len(stars)):
        stars[i].update()
        stars[i].drawStars()
