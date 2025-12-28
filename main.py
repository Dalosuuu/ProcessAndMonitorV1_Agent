import os
from datetime import datetime

import psutil

from model.model import count_open_connections, p_key


def main():
    # agent1 = EventModel()
    # agent1.printall()
    from time import sleep

    previous_proc_list = []

    while 1:
        _ = os.system("clear")
        print("\n\n")
        count: int = count_open_connections()
        print(f"total open connections: {count}")

        processes = psutil.process_iter()
        proc_name_list: list[dict[str, int | str]] = []

        for proc in processes:
            try:
                # print(proc.name(), proc.status(), sep=" |")
                # print(f"Raw proc: {proc}")
                # print(f"Info proc: {proc.pid}")
                create_time = datetime.fromtimestamp(proc.create_time()).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                # print(proc.ppid(), proc.pid, proc.name(), create_time, sep=" || ")

                proc_name_list.append(
                    {
                        "ppid": proc.ppid(),
                        "pid": proc.pid,
                        "proc_name": proc.name(),
                        "ct": create_time,
                        "exe_path": proc.exe(),
                        "cmd_line": " ".join(proc.cmdline()),
                        "uid": ", ".join(str(v) for v in proc.uids()),
                        "uname": proc.username(),
                        "w_dir": proc.cwd(),
                    }
                )
            except psutil.NoSuchProcess:
                print(
                    "Zombie parent found for process with PID:",
                    proc.pid,
                    "and name:",
                    proc.name(),
                )

        if previous_proc_list == []:
            previous_proc_list = proc_name_list.copy()
            continue

        old_k = {p_key(d) for d in previous_proc_list}
        new_k = {p_key(d) for d in proc_name_list}
        process_exit = old_k - new_k
        process_start = new_k - old_k

        print()
        print(f"{process_start = }")
        print(f"{len(process_start) = }")
        print()
        print(f"{process_exit = }")
        print(f"{len(process_exit) = }")
        print()

        # print(EventType(1))
        # print(proc_name_list[300])
        print(f"total processes: {len(proc_name_list)}")

        previous_proc_list = proc_name_list.copy()
        sleep(5)


if __name__ == "__main__":
    main()
