import os
import datetime
# ARP SPOOFER DETECTOR

def arp_table_extract():
    arp_table = os.popen('arp -a').read()
    arp_table_lines = arp_table.splitlines()
    ip_mac_addr = {}

    for line in arp_table_lines:
        if "ff-ff-ff-ff-ff-ff" in line:
            break
        if arp_table_lines.index(line) > 2:
            ip, mac, _type = line.split()
            ip_mac_addr[ip] = mac

    duplicate_mac_address(ip_mac_addr)


def duplicate_mac_address(ip_mac_addr):
    mac_addr = []
    for mac in ip_mac_addr.values():
        if mac in mac_addr:
            print("ARP SPOOF DETECTED!!")
            create_log_file(mac)
            break
        mac_addr.append(mac)


def create_log_file(mac):
    date = datetime.now()
    with open("spoof_log.txt", "a") as log_file:
        log_file.write("ARP SPOOF!!\n THE ADDRESS MAC IS {}/"
                       "DETECTED ON {} ".format(mac, date))


if __name__ == "__main__":
    arp_table_extract()
