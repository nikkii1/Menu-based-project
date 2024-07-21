#!/usr/bin/env python3

import cgi
import cgitb
import json
import psutil

cgitb.enable()  # Enable debugging

def get_total_ram():
    mem = psutil.virtual_memory()
    total_ram_gb = mem.total / (1024 ** 3)  # Convert bytes to gigabytes
    return total_ram_gb

def main():
    print("Content-Type: application/json")
    print()  # End of headers

    try:
        total_ram = get_total_ram()
        response = {"total_ram": round(total_ram, 2)}  # Round to 2 decimal places for readability
    except Exception as e:
        response = {"error": str(e)}

    print(json.dumps(response))

if __name__ == "__main__":
    main()
