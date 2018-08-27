from gamegrid import *
from random import randint


#####class#####

####C:\Users\Rebecca\Downloads\Bilder\zombie2.jpg

####C:\Users\Rebecca\Downloads\Bilder\zombie1.jpg

####C:\Users\Rebecca\Downloads\Bilder\guywithgun.gif

####C:\Users\Rebecca\Downloads\Bilder\tomato.png

####C:\Users\Rebecca\Downloads\Bilder\Orb.gif

class Zombie(Actor):
    def __init__(self, path):
        Actor.__init__(self, path)
        
    def act(self):
        self.move()
        #direction = Zombie(Human.getX(), Human.getY())
        #Zombie.setHeading(Zombie.towards(Human))
        #Zombie.forward(10)
        
        
        
class Human(Actor):
    def __init__(self):
        Actor.__init__(self,"C:\Users\Rebecca\Downloads\Bilder\guywithgun.gif")
        
class Bullet(Actor):
    def __init__(self):
        Actor.__init__(self, "C:\Users\Rebecca\Downloads\Bilder\Orb.gif" )
        self.setCollisionCircle(Point(0, 0), 10)
        
    def act(self):
        self.move()
    
    def collide(self, zombie):
        self.clear()
        return 0


def initZombies():
    for i in range(20):   
        for i in range(2):
            zombie = Zombie("C:\Users\Rebecca\Downloads\Bilder\zombie" + str(i) + ".jpg")
            Y = randint(0, 600)
            addActor(zombie, Location(800, Y), 180)
        doPause()
        
            
    
def onKeyRepeated(keyCode):
    if keyCode == 37: # left
        human.setX(human.getX() - 5)
    elif keyCode == 38: # up
        human.setY(human.getY() - 5)
    elif keyCode == 39: # right
        human.setX(human.getX() + 5)
    elif keyCode == 40: # down
        human.setY(human.getY() + 5)
    elif keyCode == 32:#shoot
        bullet = Bullet()
        addActor(bullet, Location(human.getX(), human.getY()), 0)
            
        
makeGameGrid(800, 600, 1, None, "sprites/lane.gif", False, keyRepeated = onKeyRepeated)
setSimulationPeriod(50)
initZombies()
#Zombie.addCollisionActor(Bullet)
human = Human()
addActor(human, Location(0, 300), 0)
show()
doRun()
    