#!/usr/bin/env python3

import socket

def find_the_ip(host_names):
    for host in host_names:
        print(socket.gethostbyname(host))


if __name__ == "__main__":
    host_names = ["google.com", "cnn.com", "pga.com"]
    find_the_ip(host_names)
