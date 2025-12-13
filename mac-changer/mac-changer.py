#!/usr/bin/env python3
import argparse
import subprocess

def get_arguments():
    parser = argparse.ArgumentParser(description='The Changer MAC address', prog='The Changer MAC address')
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address", required=True)
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address", default="02:22:33:44:55:66")
    return parser.parse_args()

def mac_changer(interface, new_mac):
    try:
        print(f"[+] Changing MAC address for {interface} to {new_mac}")
        subprocess.run(["ip", "link", "set", "dev", interface, "down"], check=True)
        subprocess.run(["ip", "link", "set", "dev", interface, "address", new_mac], check=True)
        subprocess.run(["ip", "link", "set", "dev", interface, "up"], check=True)
        print(f"[+] MAC-адрес {interface} изменён на {new_mac}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Ошибка: {e}")

if __name__ == "__main__":
    args = get_arguments()
    mac_changer(args.interface, args.new_mac)

