#!/usr/bin/env python3

import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-requ`çcired")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print('Everythiqng ok.')
    sys.exit(0)
main()
