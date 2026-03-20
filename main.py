from time import sleep
import os


from model.model import Proccess_Collector_Decider

pc = Proccess_Collector_Decider()

while 1:
    # _ = os.system("clear")

    events = pc.poll()

    print(events)
    print(len(events))

    sleep(3)
