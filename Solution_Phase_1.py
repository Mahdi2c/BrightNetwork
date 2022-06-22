import time
class Obstacle_Coordinate:
    def __init__(self, obstacle_x, obstacle_y):
        #CHECK OBSTACLE IN X BOUNDS
        if ((obstacle_x > 9) | (obstacle_y > 9)):
            return print("Out of bounds")
        else:
            self.obstacle_x = obstacle_x
            self.obstacle_y = obstacle_y

    def __str__(self):
        return str((self.obstacle_x, self.obstacle_y))

class Finish_Coordinate:
    def __init__(self, finish_x, finish_y):
        #CHECK FINISH IN BOUNDS
        if ((finish_x > 9) | (finish_y > 9)):
            return print("Out of bounds")
        else:
            self.finish_x = finish_x
            self.finish_y = finish_y
    
    def __str__(self):
        return str((self.finish_x, self.finish_y))

class Starting_Coordinate:
    def __init__(self):
        self.x = 3
        self.y = 2

    def move(self, add_x, add_y):
        #MOVE COORDINATE
        if (((self.x + add_x) > 9) | ((self.y + add_y) > 9) & ((self.x < 0) | (self.y < 0))):
            print("Out of Bounds")
            return False
        else:
            self.x += add_x
            self.y += add_y
        return True
    
    def reach_dest(self, Obstacles, Finish):
        blocked = False
        checkObstacle = True

        while (str(self) != str(Finish)): #CHECK THAT START ISNT AT THE FINISH YET
            time.sleep(0.1)
            while(checkObstacle): #CHECK OBSTACLE
                print(self , Finish)
                if str(self) == str(Finish):
                    checkObstacle = False
                time.sleep(0.1)

                #CHECK IF YOU CAN MOVE ONE RIGHT
                if self.y < Finish.finish_y: 
                    if self.move(0,1):
                        if str(self) in Obstacles:
                            self.move(0,-1)
                            checkObstacle = False
                    else:
                        checkObstacle = False

                #CHECK IF YOU CAN MOVE ONE LEFT
                elif self.y > Finish.finish_y:
                    if self.move(0,-1):
                        if str(self) in Obstacles:
                            self.move(0,1)
                            checkObstacle = False
                    else:
                        checkObstacle = False
                
                #IF YOU CANT MOVE LEFT OR RIGHT, THEN MOVE DOWN OR UP
                else:
                    if self.x < Finish.finish_x:
                        if self.move(1,0):
                            #REDUNDANT, BUT IT WORKS SO WHY NOT
                            self.move(-1,0)
                            self.move(1,0)
                        else:
                            self.move(-1,0)
        return print("Successfully reached destination")

    def __str__(self):
        return str((self.x, self.y))

#CREATE STARTING POINT
Start = Starting_Coordinate()

#CREATE FINISH POINT
Finish = Finish_Coordinate(9,9)

#CREATE OBSTACLES
Obstacles = []
Obstacles.append(Obstacle_Coordinate(9,7))
Obstacles.append(Obstacle_Coordinate(8,7))
Obstacles.append(Obstacle_Coordinate(6,7))
Obstacles.append(Obstacle_Coordinate(6,8))
Obstacles.append(Obstacle_Coordinate(6,8))

for i in range(len(Obstacles)):
    print("Obstacle " , (i+1) ,  ": ", Obstacles[i])

print("Starting point: ", Start , " ------ Finish Point: " ,Finish)
Start.reach_dest(Obstacles, Finish)




