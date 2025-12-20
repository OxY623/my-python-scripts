#!/usr/bin/env python3
import argparse
import subprocess
import re
import platform


def get_arguments():
    parser = argparse.ArgumentParser(
        description="The Changer MAC address", prog="The Changer MAC address"
    )
    parser.add_argument(
        "-i",
        "--interface",
        dest="interface",
        help="Interface to change its MAC address",
        required=True,
    )
    parser.add_argument(
        "-m",
        "--mac",
        dest="new_mac",
        help="New MAC address",
        default="02:22:33:44:55:66",
    )
    return parser.parse_args()


def mac_changer(interface, new_mac):
    try:
        print(f"[+] Changing MAC address for {interface} to {new_mac}")
        subprocess.run(["ip", "link", "set", "dev", interface, "down"], check=True)
        subprocess.run(
            ["ip", "link", "set", "dev", interface, "address", new_mac], check=True
        )
        subprocess.run(["ip", "link", "set", "dev", interface, "up"], check=True)
        print(f"[+] MAC-адрес {interface} изменён на {new_mac}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Ошибка: {e}")



def get_current_mac_address(interface):
    if not interface:
        print("Invalid arguments")
        return None

    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode()
    except subprocess.CalledProcessError:
        print("Could not execute ifconfig")
        return None

    mac_address_search_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result
    )

    if mac_address_search_result:
        mac_address = mac_address_search_result.group(0)
        print(f"Your MAC ADDRESS is {mac_address}")
        return mac_address
    else:
        print("Could not read MAC ADDRESS")
        return None



def get_cur_OS():
    os_name = platform.system()
    return os_name


if __name__ == "__main__":
    args = get_arguments()
    print("Start")
    print("Work only Linux OS")
    os_name = get_cur_OS()
    if os_name != "Linux":
        print("Curent OS isn't Linux OS")
        exit(-1)
    print(f"You working {os_name}. Good...")

    cur_mac_id = get_current_mac_address(args.interface)
    mac_changer(args.interface, args.new_mac)
    new_mac_id = get_current_mac_address(args.interface)
    if cur_mac_id != new_mac_id:
        if new_mac_id == args.new_mac:
            print(f"[+] MAC ADDRESS was sucessfully chandeg to {new_mac_id}")
        else:
            print("[-] MAC ADRESS didn't get changed")
    else:
        print("Something went wrong")
        if new_mac_id == args.new_mac:
            print(f"[+] MAC ADDRESS was sucessfully chandeg to {new_mac_id}")
        else:
            print("[-] MAC ADRESS didn't get changed")
