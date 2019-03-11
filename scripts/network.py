from scapy.all import *
import socket

from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
import subprocess
from subprocess import check_output

### Sample Mac Addresses
macs = {
          "68:37:e9:35:4b:cd" : "elements",
          "b4:7c:9c:db:85:e6" : "basics" 
}

### Wifi Network
network_map = {}
last_ip = None

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 4" if system_name().lower()=="windows" else "-c 2"

    # Pinging
    f = open(os.devnull, 'w')
    p = subprocess.Popen(["ping",
                    parameters,
                    host,
                    ], shell=False, stdout=subprocess.PIPE, stderr=f)
    output = p.stdout.read()
    p = subprocess.Popen(["ping",
                    parameters,
                    host,
                    ], shell=False, stdout=subprocess.PIPE, stderr=f)
    output = p.stdout.read()

    return system_call("ping " + parameters + " " + host) == 0
    #return "100.0% packet loss" not in output

def arp_monitor_callback(pkt):
    global last_ip
    global macs

    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        mac_addr = pkt.sprintf("%ARP.hwsrc%")
        if (mac_addr in macs):
              print(macs[mac_addr])
        else:
            ip_addr = pkt.sprintf("%ARP.psrc%")
            #print pkt.show()            
            
            if mac_addr in network_map:
                a = True
                if network_map[mac_addr] < 4:
                    if last_ip:
                        a = ping(last_ip)
                    if not a:
                        macs[mac_addr] = "new_button"
                network_map[mac_addr] += 1
            else:
                network_map[mac_addr] = 1

            last_ip = ip_addr
        return pkt.sprintf("%ARP.hwsrc%")


if __name__ == "__main__":
    sniff(prn=arp_monitor_callback, filter="arp", store=0)