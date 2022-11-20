import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("cycles")
        head = snake.get_head()

    """ REMOVE FOOD BLOCK FOR CYCLE
        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()
    """
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # Get both cycles
        cycles = cast.get_actors("cycles") # loads all the cycles on the 'cycles' list
        
        #cycle1 = cast.get_first_actor("cycles")
        cycle1 = cycles[0] # pulls the cycle at index 0
        head_cycle1 = cycle1.get_segments()[0]
        segments_cycle1 = cycle1.get_segments()[1:] 

        #cycle2 = cast.get_second_actor("cycles")
        cycle2 = cycles[1] # pulls the cycle at index 1
        head_cycle2 = cycle2.get_segments()[0]
        segments_cycle2 = cycle2.get_segments()[1:]

        # Check to see if both cycles hit each other
        if head_cycle1.get_position().equals(head_cycle2.get_position()):
            self._is_game_over = True

        # Check for collisions on cycle1's trail.
        for segment in segments_cycle1:
            # Check to see if cycle1 crashes into it's own trail.
            if head_cycle1.get_position().equals(segment.get_position()):
                self._is_game_over = True
            
            # Check to see if cycle2 crashes into cycle1's trail ### THIS DOES NOT WORK ###
            if head_cycle2.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        # Check for collisions on cycle2's trail.
        for segment in segments_cycle2:
            # Check to see if cycle2 crashes into it's own trail.
            if head_cycle2.get_position().equals(segment.get_position()):
                self._is_game_over = True

            # Check to see if cycle1 crashes into cycle2's trail.
            if head_cycle1.get_position().equals(segment.get_position()):
                self._is_game_over = True        


        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle1 = cast.get_first_actor("cycles") # gets cycle1 and all it's properties
            cycle2 = cast.get_second_actor("cycles") # gets cycle2 and all it's properties
            segments_cycle1 = cycle1.get_segments() # Gets the segments for cycle1
            segments_cycle2 = cycle2.get_segments() # Gets the segments for cycle2
            

            # The next 3 lines position the 'Game Over!' message in the middle of the screen
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor() # Creates an instance of the Actor() class and calls it 'message'
            message.set_text("                                 Game Over!\nPlayers keep moving and turning but don't run into each other") # sets the text to our 'message' instance of the Actor() class
            message.set_position(position) # uses our 'position' variable a few lines above to set the position for the 'Game Over!' message.
            cast.add_actor("messages", message) # Adds the message to the "messages" group

            # The next two 'for' loops turn the already drawn segments of the cycles from their color to white.
            for segment in segments_cycle1:
                segment.set_color(constants.WHITE)
            
            for segment in segments_cycle2:
                segment.set_color(constants.WHITE)