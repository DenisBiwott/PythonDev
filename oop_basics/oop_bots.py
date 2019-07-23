#Biwott
class robots:
    population = 0
   
    def __init__(self,name):
        self.name = name
   
    def new_robot(self):
        print ('\nNew robot {} alert,' .format(self.name) )
       
        robots.population += 1
       
    def dead_robot(self):
        print ('\nRobot {} is done'.format(self.name))
       
        robots.population -= 1
       
       
    def rob_pop_is(self):
        print('Robot population is {}' .format(robots.population))
   
robot1 = robots('Nipsey')
robot2 = robots('Jonte')
robot3 = robots('Kevo')
robot4 = robots('Brayo')

robot1.new_robot()
robot1.rob_pop_is()
robot2.new_robot()
robot2.rob_pop_is()
robot3.new_robot()
robot3.rob_pop_is()
robot4.new_robot()
robot4.rob_pop_is()
robot1.dead_robot()
robot1.rob_pop_is()
