import socket, sys
SERVICES = {"ssh": 22, "http": 80, "https": 443, "rdp": 3389, "dns": 53, "smtp": 25}
def check(host, service):
    port = SERVICES[service.lower()]
    s = socket.socket(); s.settimeout(1.0)
    try: return s.connect_ex((host, port)) == 0
    finally: s.close()
if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    for svc in (sys.argv[2:] or ["http", "https"]):
        print(f"{svc}: {'UP' if check(host, svc) else 'DOWN'}")
