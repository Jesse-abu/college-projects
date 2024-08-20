import copy
import random
#Recommended modules for the script

class Hat:
    #create a list that stores the arguments n number of times
    def __init__(self, **kwargs):
        self.contents = [ball for ball ,num in kwargs.items() for _ in range(num)]
    
    #remove n number of balls at random from self.contents and return them as a list
    def draw(self, pull):
        if pull >= len(self.contents):
            return [self.contents.pop(0) for _ in range(len(self.contents) - 1)]
        return [self.contents.pop(random.randint(0, (len(self.contents)-1))) for _ in range(pull)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        ball_list = copy.deepcopy(hat)
        balls_needed = [ball for ball, num in expected_balls.items() for _ in range(num)]
        drawn = list(map(str, ball_list.draw(num_balls_drawn)))
        if all(drawn.count(ball) >= balls_needed.count(ball) for ball in balls_needed):
            m += 1
    return m / num_experiments

