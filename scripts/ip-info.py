#!/usr/bin/env python3
"""CLI: ip-info

IP address information CLI. Geolocation, ISP, ASN data from public APIs.
"""
import sys, json, argparse

def main():
    parser = argparse.ArgumentParser(description="IP address information CLI. Geolocation, ISP, ASN data from public APIs.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"tool": "ip-info", "ready": True}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result}")

if __name__ == "__main__":
    main()
