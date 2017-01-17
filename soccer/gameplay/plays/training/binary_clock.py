import robocup
import constants
import play
import enum
import behavior
import main
import skills.move
import plays.testing.line_up
import time


class BinaryClock(play.Play):
    class State(enum.Enum):
        # Define your states here.
        # eg: some_state = 0
        display = 0
        transition = 1
        # -----------------------
        # remove this once you have put in your states

    def __init__(self):
        super().__init__(continuous=True)

        # This is a local variable of this class
        # Refer to it with self.current_time
        self.current_time = time.localtime().tm_min
        self.add_state(BinaryClock.State.display,behavior.Behavior.State.running)
        self.add_state(BinaryClock.State.transition,behavior.Behavior.State.running)
        # Register the states you defined using 'add_state'.
        # eg: self.add_state(WhichHalf.State.<???>,
        #                    behavior.Behavior.State.running)
        # ----------------------------------------------------
        self.add_transition(behavior.Behavior.State.start, self.State.display, lambda: True, "immediately")
        self.add_transition(self.State.display,self.State.transition, lambda: self.current_time != time.localtime().tm_min, "immediately")
        self.add_transition(self.State.transition, self.State.display, lambda: True, "immediately")
        # Add your state transitions using 'add_transition'.
        # eg: self.add_transition(behavior.Behavior.State.start,
        #                         self.State.<???>, lambda: True,
        #                         'immediately')
        # eg: self.add_transition(self.State.<???>, self.State.<???>,
        #                         lambda: <???>,
        #                         'state change message')
        # ------------------------------------------------------------

        # EXAMPLE TRANSITION, YOU MAY WANT TO REPLACE THIS
        

    # Define your own 'on_enter' and 'execute' functions here.
    # eg: def on_enter_<???>(self):
    #         print('Something?')
    # eg: def execute_<???>(self):
    #         print('Something?')
    # ---------------------------------------------------------
    def on_enter_display(self):
        numrobot = 1
        binary = format(self.current_time,"06b")
        print(binary)
        index = -constants.Field.Width/6
        for x in binary:
            if x == "1":
                move_point = robocup.Point(index, constants.Field.Length / 2)
                print(move_point)
                self.add_subbehavior(skills.move.Move(move_point), "Robot"+ str(numrobot))
                numrobot += 1
            index += constants.Field.Width/12
        self.add_subbehavior(plays.testing.line_up.LineUp(), "line up")
    def on_exit_display(self):
        self.current_time = time.localtime().tm_min
        self.remove_all_subbehaviors()
    # Demo of moving to a point.
    # def on_enter_running(self):
    #   move_point = robocup.Point(0, constants.Field.Length / 2)
    #   self.add_subbehavior(skills.move.Move(move_point), 'test move')
