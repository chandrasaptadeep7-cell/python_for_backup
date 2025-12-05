# import socket

# target = input("Enter target IP: ")

# print(f"Scanning {target}...")

# for port in range(1, 1025):   # scan first 1024 ports
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # s.settimeout(0.5)
    
#     result = s.connect_ex((target, port))  # returns 0 if open
    
#     if result == 0:
#         print(f"Port {port} OPEN")
    
#     s.close()



import socket
import threading
from queue import Queue
import time

# Configuration
target = input("Enter the IP address: ")  # Change this to your local Router or ESP32 IP
queue = Queue()
open_ports = []

# To prevent threads from printing over each other
print_lock = threading.Lock()

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Shorter timeout for speed
        result = s.connect_ex((target, port))
        s.close()
        if result == 0:
            return True
        return False
    except:
        return False

# The Threader Function
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            with print_lock:
                print(f"Port {port} is OPEN")
                open_ports.append(port)
        queue.task_done()

# Main Execution
def run_scanner(threads=100):
    print(f"Scanning {target} with {threads} threads...")
    start_time = time.time()

    # 1. Create the range of ports to scan (1 to 1000)
    for port in range(1, 1001):
        queue.put(port)

    # 2. Create and start threads
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=worker)
        thread_list.append(t)
        t.start()

    # 3. Wait for all threads to finish their queues
    for t in thread_list:
        t.join()

    end_time = time.time()
    print(f"\nScan completed in {end_time - start_time:.2f} seconds")

# Run it
if __name__ == "__main__":
    run_scanner()