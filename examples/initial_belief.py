from maspy import *
import time

class HelloAgent(Agent):
    @pl(gain,Belief("hello"))
    def hello(self, src):
        time.sleep(5)
        self.print(f"Hello World!")
    @pl(gain,Belief("bye"))
    def bye(self, src):
        self.print(f"Goodbye World!")
        self.stop_cycle()

if __name__ == "__main__":
    print("This is an example of how to use the maspy library.")
    # Using max_intentions to make sure that hello will be executed before bye because only one intention will be executed per time.
    ag = HelloAgent(beliefs=[Belief("hello"), Belief("bye")],max_intentions=1)
    Admin().start_system()