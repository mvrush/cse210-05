import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlCyclesAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        # The next two lines tell which direction and speed to move each cycle by default. To set their starting position, look in cycle1.py and cycle2.py
        self._direction_cycle1 = Point(0, -constants.CELL_SIZE) # Default direction was set with the '-constants.CELL_SIZE)' which is -15. So it moves 1 cell negative(up) on the y-axis causing movement by default.
        self._direction_cycle2 = Point(0, constants.CELL_SIZE) # Default direction was set with the 'constants.CELL_SIZE)' which is 15. So it moves 1 cell positive(down) on the y-axis causing movement by default.
        #self._direction = Point(0, 0) # Set this to Point(0, 0) so that the cycle will not move.

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
    ### Control cycle1
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction_cycle1 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction_cycle1 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction_cycle1 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction_cycle1 = Point(0, constants.CELL_SIZE)
        
        cycle1 = cast.get_first_actor("cycles")
        cycle1.turn_head(self._direction_cycle1)


    ### Control cycle2
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction_cycle2 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction_cycle2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction_cycle2 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction_cycle2 = Point(0, constants.CELL_SIZE)
        
        cycle2 = cast.get_second_actor("cycles")
        cycle2.turn_head(self._direction_cycle2)