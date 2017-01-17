import robocup
import constants
import play
import enum
import behavior
import main


# Maintains the state of the ball's position by keeping track of which
# half the ball is on and prints on both entering a given state and
# continously during the execution of a given state.
class WhichHalf(play.Play):
    class State(enum.Enum):
          ourSide = 0
          theirSide = 1

    def __init__(self):
        super().__init__(continuous=True)
        self.add_state(WhichHalf.State.ourSide, behavior.Behavior.State.running)
        self.add_state(WhichHalf.State.theirSide, behavior.Behavior.State.running)
        # Register the states you defined using 'add_state'.
        # eg: self.add_state(WhichHalf.State.<???>,
        #                    behavior.Behavior.State.running)
        # ----------------------------------------------------
        self.add_transition(behavior.Behavior.State.start, self.State.ourSide,lambda: main.ball().pos.y < constants.Field.Length/2, "ball has entered our side")
        self.add_transition(behavior.Behavior.State.start, self.State.theirSide,lambda: main.ball().pos.y > constants.Field.Length/2, "ball has entered their side")
        self.add_transition(self.State.theirSide, self.State.ourSide,lambda: main.ball().pos.y < constants.Field.Length/2, "ball has entered our side")
        self.add_transition(self.State.ourSide, self.State.theirSide,lambda: main.ball().pos.y > constants.Field.Length/2, "ball has entered their side")


        # Add your state transitions using 'add_transition'.
        # eg: self.add_transition(behavior.Behavior.State.start,
        #                         self.State.<???>, lambda: True,
        #                         'immediately')
        # eg: self.add_transition(self.State.<???>, self.State.<???>,
        #                         lambda: <???>,
        #                         'state change message')
        # ------------------------------------------------------------

    # Define your own 'on_enter' and 'execute' functions here.
    def on_enter_ourSide(self):
        print("ball has entered our side")
    def on_enter_theirSide(self):
        print("ball has entered their side")
    # ---------------------------------------------------------
