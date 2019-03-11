from scapy.all import *

MAC_ADDRESS = '68:37:e9:35:4b:cd' # enter Dash Button's MAC Address here.

def detect_button(pkt):
    if pkt.haslayer(DHCP) and pkt[Ether].src == MAC_ADDRESS:
            print("Button Press Detected")
            #Do stuff

sniff(prn=detect_button, filter="(udp and (port 67 or 68))", store=0)