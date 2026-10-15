import threading
import time

from maspy import *

class HelloAgent(Agent):
    @pl(gain, Belief("hello"))
    def hello(self, src):
        self.print("Executing planning hello")
        time.sleep(5)
        self.print("Hello World!")
    @pl(gain, Belief("bye"))
    def bye(self, src):
        self.print("Bye World!")
        self.stop_cycle()

if __name__ == "__main__":
    ag = HelloAgent(max_intentions=1)

    def delayed_add():
        time.sleep(2)
        print("Adding belief hello")
        ag.add(Belief("hello"))
        print("Adding belief bye")
        ag.add(Belief("bye"))

    threading.Thread(target=delayed_add, daemon=True).start()
    Admin().start_system()