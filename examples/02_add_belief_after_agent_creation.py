from maspy import *
import time

class HelloAgent(Agent):
    @pl(gain,Belief("hello"))
    def hello(self, struct):
        time.sleep(5)
        self.print("Hello World!")
    @pl(gain, Belief("bye"))
    def bye(self, struct):
        self.print("Bye World!")
        self.stop_cycle()

if __name__ == "__main__":
    ag = HelloAgent(max_intentions=1)
    ag.add(Belief("hello"))
    ag.add(Belief("bye"))
    Admin().start_system()
