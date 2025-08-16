# CodeAlpha_Task1: Python Network Packet Sniffer

**Author:** Akşin Abdullayev  
**Internship:** CodeAlpha Cyber Security Internship (10 Aug 2025 - 10 Sep 2025)  
**GitHub:** [https://github.com/Aksin528/CodeAlpha_Task1](https://github.com/Aksin528/CodeAlpha_Task1)  

---

## 📌 Project Overview
This project is a **Python-based network packet sniffer** that captures network traffic in real-time, analyzes packet structures, and displays essential information such as:

- Source and destination IP addresses
- Protocol type (TCP, UDP, ICMP, etc.)
- Packet payload (first 16 bytes preview)
- Hostnames for known IPs

It is designed as a practical project for learning network traffic analysis and understanding how data flows through the network.

---

## 🛠️ Features
- Real-time packet capture using **Scapy**
- Displays packet information in human-readable format
- Saves captured packets to a **PCAP file** for later analysis
- Supports graceful stopping with **CTRL+C** or **CTRL+Z**
- Highlights known hosts (e.g., Google DNS, Cloudflare DNS)

---

## ⚙️ Requirements
- Python 3.x
- Scapy library

Install Scapy using pip:

```bash
python3 -m pip install scapy
