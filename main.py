#!/usr/bin/env python3
import sys
from core.cli import WKT12CLI
from utils.banner import banner

def main():
    banner()
    cli = WKT12CLI()
    cli.run()

if __name__ == "__main__":
    main()
