from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

# Ping test method
c.ping()

# Real ping method
c.advanced_ping()

print(f"IP: {c.ip}, {c.port}")
