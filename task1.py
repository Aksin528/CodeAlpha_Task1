from scapy.all import sniff, IP, TCP, UDP, ICMP, wrpcap
from collections import defaultdict
import signal
import sys
import os

# Captured packets
packets = []

# Known hosts dictionary
known_hosts = defaultdict(str)
known_hosts['8.8.8.8'] = 'google-dns'
known_hosts['1.1.1.1'] = 'cloudflare-dns'

# Flag to control sniffing loop
running = True

# Function to generate next available pcap filename
def get_next_filename(base="capture", ext=".pcap"):
    i = 1
    while True:
        filename = f"{base}{i}{ext}"
        if not os.path.exists(filename):
            return filename
        i += 1

def signal_handler(sig, frame):
    global running
    running = False
    print("\nSniffer stopped. Do you want to save the hosts and packets to a file? (y/n)")
    choice = input().strip().lower()
    if choice == 'y':
        filename = get_next_filename()
        wrpcap(filename, packets)
        print(f"Packets saved to {filename}")
        print("Captured hosts:")
        for ip, host in known_hosts.items():
            print(f"Host {ip} -> {host}")
    else:
        print("Hosts and packets were not saved.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)  # CTRL+C
signal.signal(signal.SIGTSTP, signal_handler) # CTRL+Z

def packet_callback(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        proto = ''
        if TCP in pkt:
            proto = 'TCP'
        elif UDP in pkt:
            proto = 'UDP'
        elif ICMP in pkt:
            proto = 'ICMP'
        else:
            proto = str(pkt[IP].proto)

        src_host = known_hosts.get(src_ip, src_ip)
        dst_host = known_hosts.get(dst_ip, dst_ip)

        payload = bytes(pkt[IP].payload)
        payload_preview = payload[:16]  # first 16 bytes

        print(f"[+] {src_ip} ({src_host}) -> {dst_ip} ({dst_host}) | Proto: {proto} | Length: {len(pkt)} bytes | Payload: {payload_preview.hex()}")

        packets.append(pkt)

# Start sniffing
print("[*] Sniffing network packets... Press CTRL+C to stop.")
sniff(prn=packet_callback, store=False)
