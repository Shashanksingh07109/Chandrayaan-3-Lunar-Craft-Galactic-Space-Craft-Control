import unittest
class Chandrayaan3:
    def __init__(self, initial_position, initial_direction):
        self.position = initial_position
        self.direction = initial_direction
        
        
    def move_forward(self):
        if self.direction == "N":
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == "S":
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == "E":
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == "W":
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == "Up":
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
        elif self.direction == "Down":
            self.position = (self.position[0], self.position[1], self.position[2] - 1)
            
            
    def move_backward(self):
        if self.direction == "N":
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == "S":
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == "E":
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == "W":
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == "Up":
            self.position = (self.position[0], self.position[1], self.position[2] - 1)
        elif self.direction == "Down":
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
           
        
    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "Up":
            self.direction = "W"
        elif self.direction == "Down":
            self.direction = "E"
        

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "W":
            self.direction = "N"
        elif self.direction == "Up":
            self.direction = "E"
        elif self.direction == "Down":
            self.direction = "W"

    def turn_up(self):
        if self.direction in ["N", "S", "E", "W"]:
            self.direction = "Up"
            

    def turn_down(self):
        if self.direction in ["N", "S", "E", "W"]:
            self.direction = "Down"
            

    def execute_commands(self, commands):
        for command in commands:
            if command == "f":
                self.move_forward()
            elif command == "b":
                self.move_backward()
            elif command == "l":
                self.turn_left()
            elif command == "r":
                self.turn_right()
            elif command == "u":
                self.turn_up()
            elif command == "d":
                self.turn_down()
        return self.position, self.direction
            
            
class TestChandrayaan3(unittest.TestCase):
    
    def test_move_forward(self):
        craft1 = Chandrayaan3((0, 0, 0), "N")
        craft1.move_forward()
        self.assertEqual(craft1.position, (0, 1, 0))
        
        craft1 = Chandrayaan3((1, 1, 1), "E")
        craft1.move_forward()
        self.assertEqual(craft1.position, (2, 1, 1))
        
    def test_move_backward(self):
        craft1 = Chandrayaan3((0, 0, 0), "N")
        craft1.move_backward()
        self.assertEqual(craft1.position, (0, -1, 0))
        
        craft1 = Chandrayaan3((1, 1, 1), "E")
        craft1.move_backward()
        self.assertEqual(craft1.position, (0, 1, 1))
        
        
    def test_turn_left(self):
        craft1 = Chandrayaan3((0, 0, 0), "N")
        craft1.turn_left()
        self.assertEqual(craft1.direction, "W")
        
        craft1 = Chandrayaan3((0, 0, 0), "E")
        craft1.turn_left()
        self.assertEqual(craft1.direction, "N")
        
        craft1 = Chandrayaan3((0, 0, 0), "W")
        craft1.turn_left()
        self.assertEqual(craft1.direction, "S")
        
        craft1 = Chandrayaan3((0, 0, 0), "S")
        craft1.turn_left()
        self.assertEqual(craft1.direction, "E")
        
        
    def test_turn_right(self):
        craft1 = Chandrayaan3((0, 0, 0), "N")
        craft1.turn_right()  
        self.assertEqual(craft1.direction, "E")
        
        craft1 = Chandrayaan3((0, 0, 0), "E")
        craft1.turn_right()
        self.assertEqual(craft1.direction, "S")
        
        craft1 = Chandrayaan3((0, 0, 0), "S")
        craft1.turn_right()
        self.assertEqual(craft1.direction, "W")
        
        craft1 = Chandrayaan3((0, 0, 0), "W")
        craft1.turn_right()
        self.assertEqual(craft1.direction, "N")
        
    def test_turn_up(self):
        craft1 = Chandrayaan3((0, 0, 0), "N")
        craft1.turn_up()
        self.assertEqual(craft1.direction, "Up")
        
        craft1 = Chandrayaan3((0, 0, 0), "E")
        craft1.turn_up()
        self.assertEqual(craft1.direction, "Up")
        
        craft1 = Chandrayaan3((0, 0, 0), "W")
        craft1.turn_up()
        self.assertEqual(craft1.direction, "Up")
        
        craft1 = Chandrayaan3((0, 0, 0), "S")
        craft1.turn_up()
        self.assertEqual(craft1.direction, "Up")
        
    def test_turn_down(self):
        craft1 = Chandrayaan3((0, 0, 0), "N")
        craft1.turn_down()
        self.assertEqual(craft1.direction, "Down")
        
        craft1 = Chandrayaan3((0, 0, 0), "E")
        craft1.turn_down()
        self.assertEqual(craft1.direction, "Down")
        
        craft1 = Chandrayaan3((0, 0, 0), "W")
        craft1.turn_down()
        self.assertEqual(craft1.direction, "Down")
        
        craft1 = Chandrayaan3((0, 0, 0), "S")
        craft1.turn_down()
        self.assertEqual(craft1.direction, "Down")
        
    def test_execute_commands(self):
        craft1 = Chandrayaan3((0, 0, 0), "N")
        commands = ["f", "r", "u", "b", "l"]
        craft1.execute_commands(commands)
        self.assertEqual(craft1.position, (0, 1, -1))
        self.assertEqual(craft1.direction, "W")
        
unittest.main(argv=[' '] , verbosity=2 , exit=False)