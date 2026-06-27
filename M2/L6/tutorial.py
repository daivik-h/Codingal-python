import time
import random
import sys

lines = [
    "Initializing hack sequence...",
    "Bypassing firewall...",
    "Accessing secure server...",
    "Decrypting passwords...",
    "Injecting malware...",
    "Downloading classified data...",
    "Accessing webcam...",
    "Tracking IP address...",
    "Almost there...",
]

def type_writer(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.05))
    print()

# Green text effect
print("\033[92m")

for i in range(20):
    type_writer(random.choice(lines))
    time.sleep(random.uniform(0.2, 0.6))

print("\nACCESS GRANTED")
time.sleep(1)

# Fake loading bar
for i in range(101):
    sys.stdout.write(f"\rUploading data: {i}%")
    sys.stdout.flush()
    time.sleep(0.03)

print("\n\n💀 SYSTEM BREACHED 💀")
time.sleep(1)

print("\nJust kidding... you're safe 😄")