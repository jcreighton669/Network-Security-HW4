import re
import sys
import time
from ipaddress import *
from scapy import *

TIME_WINDOW = 5


def get_ports():
    ports = []
    for i in range(1, 65536):
        ports.append(i)
    return ports


def get_target():
    target = input()
    while re.match("([0-9]{1,3}.){3}[0-9]{1,3}$", target) is None:
        print("Please enter a correctly formatted IP address.")
        target = input()
    target = ip_address(target)
    return target


def counter_scan(arr):
    ports = get_ports()
    try:
        while True:
            for num in ports:
                break
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            pass
