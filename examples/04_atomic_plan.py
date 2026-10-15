import time
from maspy import *

class HelloAgent(Agent):
    # Atomic is required when we are not setting the max_intentions to agent to make sure that hello will be executed before bye
    @pl(gain, Belief("hello"), plan_type=atomic)
    def hello(self, src):
        self.print("Starting Hello!")
        time.sleep(5)
        self.print("Hello World!")
    @pl(gain, Belief("bye"))
    def bye(self, src):
        self.print("Bye World!")
        self.stop_cycle()

if __name__ == "__main__":
    ag = HelloAgent(beliefs=[Belief("hello"), Belief("bye")])
    Admin().start_system()