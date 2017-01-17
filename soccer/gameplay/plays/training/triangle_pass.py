import play
import behavior
import tactics.coordinated_pass
import tactics.behavior_sequence
import robocup
import constants
import main
import plays.testing.line_up


## Continually runs a coordinated pass to opposite sides of the field
class Triangle_Pass(play.Play):

    ReceiveXCoord = 1
    ReceiveYCoord = constants.Field.Length / 2.0 * 1.0 / 3.0

    def __init__(self):
        super().__init__(continuous=True)

        self.add_transition(behavior.Behavior.State.start,
                            behavior.Behavior.State.running, lambda: True,
                            'immediately')

        pass_bhvr = tactics.coordinated_pass.CoordinatedPass()
        self.add_subbehavior(pass_bhvr, 'pass')
        #self.add_subbehavior(plays.testing.line_up.LineUp(), "line up")

    def reset_receive_point(self):
        pass_bhvr = self.subbehavior_with_name('pass')
        if main.ball().pos.x < 0 and main.ball().pos.y < Triangle_Pass.ReceiveYCoord +1:
            x = Triangle_Pass.ReceiveXCoord
            y = Triangle_Pass.ReceiveYCoord
        elif main.ball().pos.y > Triangle_Pass.ReceiveYCoord +1:
            x = -Triangle_Pass.ReceiveXCoord
            y = Triangle_Pass.ReceiveYCoord
        elif main.ball().pos.x > 0:
            x = 0
            y = Triangle_Pass.ReceiveYCoord + 2
        pass_bhvr.receive_point = robocup.Point(x,y)

    def execute_running(self):
        pass_bhvr = self.subbehavior_with_name('pass')

        if pass_bhvr.is_done_running():
            pass_bhvr.restart()
            self.reset_receive_point()

        if pass_bhvr.receive_point == None:
            self.reset_receive_point()
