import constants

from game.casting.cast import Cast
#from game.casting.food import Food
from game.casting.score import Score
from game.casting.cycle1 import Cycle1
from game.casting.cycle2 import Cycle2
from game.scripting.script import Script
from game.scripting.control_cycles_action import ControlCyclesAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    #cast.add_actor("foods", Food())
    cast.add_actor("cycles", Cycle1()) # Creates the "cycles" group and adds cycle1 to cast using the methods found in Cycle1() class
    cast.add_actor("cycles", Cycle2()) # Finds the "cycles" group and adds cycle2 to cast using the methods found in Cycle2() class
    cast.add_actor("scores", Score())
    # print(cast.get_actors("cycles")) # For troubleshooting, shows in the console that we have 2 cycles in the "cycles" group now.
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlCyclesAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()