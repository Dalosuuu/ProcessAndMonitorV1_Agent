from time import sleep


from model.model import Proccess_Collector_Decider

pc = Proccess_Collector_Decider()

while 1:
    # _ = os.system("clear")

    events = pc.poll()

    # print(events)
    for event in events:
        print(event, "\n")
    print("Total event last cycle: ", len(events))

    sleep(3)
