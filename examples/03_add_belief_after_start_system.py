import threading
import time

from maspy import *

class HelloAgent(Agent):
    @pl(gain, Belief("hello"))
    def hello(self, src):
        self.print("Executing planning hello")
        time.sleep(5)
        self.print(f"Hello World received from {src}!")
    @pl(gain, Belief("bye"))
    def bye(self, src):
        self.print(f"Bye World received from {src}!")
        self.stop_cycle()

if __name__ == "__main__":
    ag = HelloAgent(max_intentions=1)

    def delayed_add():
        time.sleep(2)
        print("Adding belief hello")
        ag.add(Belief("hello", source="delayed_thread"))
        print("Adding belief bye")
        ag.add(Belief("bye", source="delayed_thread"))

    threading.Thread(target=delayed_add, daemon=True).start()
    Admin().start_system()