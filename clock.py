#!/usr/bin/env python3
"""Terminal clock that highlights seconds in red every 10 seconds."""
import time
from datetime import datetime

RESET = "\033[0m"
RED = "\033[31m"

try:
    while True:
        now = datetime.now()
        hour = now.strftime('%H')
        minute = now.strftime('%M')
        second = now.second
        if second % 10 == 0:
            sec_str = f"{RED}{second:02}{RESET}"
        else:
            sec_str = f"{second:02}"
        time_str = f"{hour}:{minute}:{sec_str}"
        print(f"\r{time_str}", end='', flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print()

