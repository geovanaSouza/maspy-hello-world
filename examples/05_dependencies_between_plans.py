import time
from maspy import *

HELLO_DURATION = 5

class HelloAgent(Agent):

    @pl(gain, Belief("hello"))
    def hello(self, src):
        self.print("Starting Hello!")
        time.sleep(HELLO_DURATION)
        self.print("Hello World")
        self.add(Belief("hello_done"))

    @pl(gain, Belief("hello_done"))
    def add_bye(self, src):
        self.add(Belief("bye"))

    @pl(gain, Belief("bye"), context=Belief("hello_done"))
    def bye(self, src):
        self.print("Bye World!")
        self.stop_cycle()

if __name__ == "__main__":
    ag = HelloAgent(beliefs=Belief("hello"))
    Admin().start_system()