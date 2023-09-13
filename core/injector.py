from scapy.all import *

def force_reauthentication(iface, client_mac):

    # send an EAPOL-Start broadcast from client's mac,
    #packet = Ether(src=client_mac, dst="01:80:c2:00:00:03")/EAPOL(version=2, type=0, len=5)/EAP(code=1, type=1)
    packet = Ether(src=client_mac, dst="01:80:c2:00:00:03")/EAPOL(type=1)
    #packet = Ether(src=client_mac, dst="ec:01:d5:b5:5a:24e")/EAPOL(type=1)
    packet.show()
    print iface
    sendp(packet, iface=iface)
