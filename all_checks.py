#!/usr/bin/env python3

import os
import shutil
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists('/run/reboot-required')

def check_disk_full(disk, mmin_absolute, min_percent):

    """Returns True if there isn’t enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    "Calculate the percentage of free space"
    percent_free = 100 * du.free / du.total

# Calculate how many free gigabytes

def main():
    if check_disk_full(disk="/",min_gb=2,min_percent=5):
        print('disk full')
        sys.exit('not Ok')
    sys.exit(0)
main()
