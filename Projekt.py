from gamegrid import *
from random import randint


#####class#####

####C:\Users\Rebecca\Downloads\Bilder\zombie2.jpg

####C:\Users\Rebecca\Downloads\Bilder\zombie1.jpg

####C:\Users\Rebecca\Downloads\Bilder\guywithgun.gif

####C:\Users\Rebecca\Downloads\Bilder\tomato.png

####C:\Users\Rebecca\Downloads\Bilder\Orb.gif


class collider:
    objects = []
    def add(self, obj):
        self.objects.append(obj)
        return
    
    def check(self, p_obj):
        colliders = []
        p_pos = p_obj.getPos()
        left = p_pos[0]-p_obj.half_size[0]
        right = p_pos[0]+p_obj.half_size[0]
        top = p_pos[1]-p_obj.half_size[1]
        bottom = p_pos[1]+p_obj.half_size[1]
        for idx, obj in enumerate(self.objects):
            obj_pos = obj.getPos()
            left2 = obj_pos[0]-obj.half_size[0]
            right2 = obj_pos[0]+obj.half_size[0]
            top2 = obj_pos[1]-obj.half_size[1]
            bottom2 = obj_pos[1]+obj.half_size[1]
            if left <= right2 and right >= left2 and top <= bottom2 and bottom >= top2:
                colliders.append(obj)
        return colliders

m_collider = collider()



class Zombie(Actor):
    def __init__(self, path):
        Actor.__init__(self, path)
        colliders = m_collider.check(self)
        len_col = len(colliders)
        if len_col > 1:
            print("ERROR")
        
    def act(self):
        self.move()
    
    def getPos(self):
        return [self.getX(), self.getY()]

        
        
        
class Human(Actor):
    def __init__(self):
        Actor.__init__(self,"C:\Users\Rebecca\Downloads\Bilder\guywithgun.gif")
        self.half_size[0] = self.getWidth(0)/2
        self.half_size[1] = self.getHeight(0)/2
    
    half_size = [0,0]
    def getPos(self):
        return [self.getX(), self.getY()]
        
class Bullet(Actor):
    def __init__(self):
        Actor.__init__(self, "C:\Users\Rebecca\Downloads\Bilder\Orb.gif" )
        half_size = [0,0]
        colliders = m_collider.check(self)
        len_col = len(colliders)
        if len_col > 1:
            print("ERROR")
        
    def act(self):
        self.move()
    
    def getPos(self):
        return self.pos
    



def initZombies():
    for i in range(20):   
        for i in range(2):
            zombie = Zombie("C:\Users\Rebecca\Downloads\Bilder\zombie" + str(i) + ".jpg")
            Y = randint(0, 600)
            addActor(zombie, Location(800, Y), 180)
            m_collider.add(zombie)
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
        m_collider.add(bullet)
        addActor(bullet, Location(human.getX(), human.getY()), 0)
            
        
makeGameGrid(800, 600, 1, None, "sprites/lane.gif", False, keyRepeated = onKeyRepeated)
setSimulationPeriod(50)
#initZombies()
human = Human()
addActor(human, Location(0, 300), 0)
show()
doRun()
    