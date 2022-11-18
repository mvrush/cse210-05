import constants
from game.casting.actor import Actor
from game.casting.cycle1 import Cycle1
from game.shared.point import Point


class Cycle2(Cycle1):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__() # This gives us access to all variables and methods in the Actor() class
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, cast, number_of_segments): # Receives the instance of 'cast' and 'number_of_segments' values from 'snake.grow_tail(cast, 1)' found in draw_actors_action.py
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            message = cast.get_first_actor("messages") # uses the instance of 'cast' to pull the message
            #print(message) # used for testing to see what I got for a message

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            if message == None: # checks for a message object. If 'None' writes segments in LIGHT_BLUE
                segment.set_color(constants.LIGHT_YELLOW)
            else:
                segment.set_color(constants.WHITE) # if there is a message object, writes segments in WHITE. You only get a message object when game over.
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y) # Looks at the value of x, subtracts the index position for each length of the snake, multiplies it by the CELL_SIZE for the X position, just gives the y value for Y position
            velocity = Point(1 * constants.CELL_SIZE, 0) # Sets the velocity to 1 times the CELL_SIZE(15) for X and 0 for Y.
            text = "8" if i == 0 else "#" # Says draw an "8" in index position '0' for the snake head. Every other index position is a "#"
            color = constants.YELLOW if i == 0 else constants.LIGHT_YELLOW # Says draw index position 0 as "YELLOW", everything else "LIGHT_BLUE"
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)