from time import sleep
import argparse
from typing import cast


from model.model import Proccess_Collector_Decider

pc = Proccess_Collector_Decider()

# Parser
parser: argparse.ArgumentParser = argparse.ArgumentParser()
_ = parser.add_argument(
    "-c", "--cycle", help="set cycle loop speed used in sleep", default=5, type=int
)

args = parser.parse_args()

while 1:
    # _ = os.system("clear")

    cycleT = cast(int, args.cycle)

    events = pc.poll()

    for event in events:
        print(event, "\n")
    print("Total event last cycle: ", len(events))
    sleep(cycleT)
