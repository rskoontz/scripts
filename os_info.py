#!/usr/bin/env python3

import sys
import platform


def os_information():
    print(platform.system())
    print(platform._sys_version())
    print(platform.node())
    print(platform.machine())
    print(platform.processor())
    print(platform.mac_ver())


def main():
    os_information()


if __name__ == "__main__":
    main()
