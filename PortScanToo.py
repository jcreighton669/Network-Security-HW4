import random
import re
import socket
import time
from ipaddress import *


def draw_port_line2(arr, line_num):
    line_arr = []
    port_arr = arr
    pv = ': '
    for port_num in port_arr:
        if port_num < line_num:
            index = (port_num // 256) + 1
            line_arr.append(index)
    for i in range(16):
        if i in line_arr:
            for j in range(line_arr.count(i)):
                pv += "!"
        else:
            pv += "."
    while pv.count('.') != 16:
        if pv.count('.') < 16:
            pv += '.'

    print(str(line_num) + pv)


def draw_port_line(arr):
    line_arr = []
    port_arr = arr
    pv = ': '
    for port_num in port_arr:
        index = (port_num // 256) + 1
        line_arr.append(index)
    for i in range(16):
        if i in line_arr:
            for j in range(line_arr.count(i)):
                pv += "!"
        else:
            pv += "."
    while pv.count('.') != 16:
        if pv.count('.') < 16:
            pv += '.'

    print("0" + pv)


def get_target():
    target = input()
    while re.match("([0-9]{1,3}.){3}[0-9]{1,3}$", target) is None:
        print("Please enter a correctly formatted IP address.")
        target = input()
    target = ip_address(target)
    return target


def get_ports():
    ports = []
    for i in range(1, 65536):
        ports.append(i)
    return ports


def scan():
    socket.setdefaulttimeout(0.00001)
    target = str(get_target())
    start_time = time.time()
    ports = get_ports()
    open_ports = {}
    open_port_arr_0 = []
    open_port_arr_4096 = []
    open_port_arr_8192 = []
    open_port_arr_12288 = []
    open_port_arr_16384 = []
    open_port_arr_20480 = []
    open_port_arr_28672 = []
    open_port_arr_32768 = []
    open_port_arr_36864 = []
    open_port_arr_40960 = []
    open_port_arr_45056 = []
    open_port_arr_49152 = []
    open_port_arr_53248 = []
    open_port_arr_57344 = []
    open_port_arr_61440 = []

    print("Scanning", target)
    print("-------------------------")
    while len(ports) != 0:
        num = random.choice(ports)
        ports.remove(num)

        try:
            conn_skt = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            result = conn_skt.connect_ex((target, num))
            # print(str(num) + " " + str(result))
            if result == 0:
                open_ports[num] = socket.getservbyport(num)
                conn_skt.close()
                if num > 61440:
                    open_port_arr_61440.append(num - 61440)
                elif num > 57344:
                    open_port_arr_57344.append(num - 57344)
                elif num > 53248:
                    open_port_arr_53248.append(num - 53248)
                elif num > 49152:
                    open_port_arr_49152.append(num - 49152)
                elif num > 45056:
                    open_port_arr_45056.append(num - 45056)
                elif num > 40960:
                    open_port_arr_40960.append(num - 40960)
                elif num > 36864:
                    open_port_arr_36864.append(num - 36864)
                elif num > 32768:
                    open_port_arr_32768.append(num - 32768)
                elif num > 28672:
                    open_port_arr_28672.append(num - 28672)
                elif num > 20480:
                    open_port_arr_20480.append(num - 20480)
                elif num > 16384:
                    open_port_arr_16384.append(num - 16384)
                elif num > 12288:
                    open_port_arr_12288.append(num - 12288)
                elif num > 8192:
                    open_port_arr_8192.append(num - 8192)
                elif num > 4096:
                    open_port_arr_4096.append(num - 4096)
                else:
                    open_port_arr_0.append(num)

            else:
                pass
        except socket.error as error:
            pass

    end_time = time.time()
    draw_port_line(open_port_arr_0)
    draw_port_line2(open_port_arr_4096, 4096)
    draw_port_line2(open_port_arr_8192, 8192)
    draw_port_line2(open_port_arr_12288, 12288)
    draw_port_line2(open_port_arr_16384, 16384)
    draw_port_line2(open_port_arr_20480, 20480)
    draw_port_line2(open_port_arr_28672, 28672)
    draw_port_line2(open_port_arr_32768, 32768)
    draw_port_line2(open_port_arr_40960, 40960)
    draw_port_line2(open_port_arr_45056, 45056)
    draw_port_line2(open_port_arr_49152, 49152)
    draw_port_line2(open_port_arr_53248, 53248)
    draw_port_line2(open_port_arr_57344, 57344)
    draw_port_line2(open_port_arr_61440, 61440)

    print("Scan Finished!")

    print("-------------------------")
    print(len(open_ports), "ports found")
    print(round(end_time - start_time, 2), "seconds elapsed")
    print(round(65536/len(open_ports), 2), "ports per second")
    print("-------------------------")

    for key in sorted(open_ports):
        print(str(key) + ":\t" + open_ports[key])


scan()
