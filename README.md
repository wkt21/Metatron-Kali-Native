# Metatron-Kali-Native
plugin‑driven WKT12 scanning framework
<img width="1536" height="1024" alt="IMG_1961" src="https://github.com/user-attachments/assets/b9e90c24-f55b-4250-b128-fedf03d560b7" />


WKT12 Pentest Framework (Kali Edition)

A modular, plugin‑driven penetration testing framework designed for Kali Linux.
WKT12 provides a clean architecture for recon, AI‑assisted analysis, session management, and export capabilities.
It is built for extensibility, SOC workflows, and OSINT/pentest automation.

---

Overview

WKT12 is a lightweight but powerful scanning engine that loads recon tools as plugins, executes them against a target, and feeds the results into an AI analysis module.
It is designed for:

• Kali Linux operators
• Red‑teamers
• OSINT analysts
• SOC automation pipelines
• Cybersecurity researchers


The framework is fully modular. Adding new recon tools requires only dropping a new plugin file into the plugins/ directory.

---

Features

• Plugin‑based recon system
• Auto‑loading of all recon modules
• Unified session object for recon + analysis
• AI‑driven vulnerability summarization
• Clean CLI interface
• Structured JSON‑ready output
• Kali‑native tool integration (Nmap, WhatWeb, WAFW00F, Nuclei, etc.)


---

Repository Structure

wkt12/
│
├── core/
│   ├── cli.py              # Main CLI interface
│   ├── session.py          # Session object
│   ├── analysis.py         # AI analysis engine
│   ├── database.py         # (Optional) DB persistence layer
│   └── loader.py           # Plugin auto-loader
│
├── plugins/
│   ├── __init__.py
│   ├── nmap.py             # Nmap plugin
│   ├── whatweb.py          # WhatWeb plugin
│   ├── wafw00f.py          # WAFW00F plugin
│   └── nuclei.py           # Nuclei plugin
│
├── export/
│   └── exporter.py         # Export utilities (JSON, Markdown, etc.)
│
├── utils/
│   ├── banner.py           # ASCII banner
│   ├── colors.py           # Color helpers
│   └── helpers.py          # Prompt + logging helpers
│
└── main.py                 # Entry point


---

Installation

Requirements

Kali Linux with the following tools installed:

• nmap
• whatweb
• wafw00f
• nuclei


Python 3.8+ is required.

Clone the repository

git clone https://github.com/yourname/wkt12.git
cd wkt12


Run the framework

python3 main.py


---

Usage

Main Menu

[1] New Scan
[2] Exit


Running a Scan

Enter a target:

wkt12> 1
Enter target: example.com


The framework will:

1. Load all plugins
2. Execute each recon tool
3. Store results in a session object
4. Run AI analysis
5. Print structured output


Example output:

[INFO] Running nmap...
[INFO] Running whatweb...
[INFO] Running wafw00f...
[INFO] Running nuclei...
[INFO] Running AI analysis...
[OK] Scan complete.
{ ... JSON session data ... }


---

Plugin System

How Plugins Work

Each plugin is a Python module containing a Plugin class with:

• name attribute
• run(target) method


Example:

class Plugin:
    name = "nmap"

    def run(self, target):
        ...


Adding a New Plugin

Drop a new file into plugins/:

plugins/mytool.py


With:

class Plugin:
    name = "mytool"

    def run(self, target):
        return "output"


It will be auto‑loaded at runtime.

---

AI Analysis Engine

The analysis engine receives all recon output and produces:

• risk score
• vulnerability list
• exploit suggestions
• summary
• raw recon data


This module is fully customizable.

---

Exporting Results

The export/ module provides utilities for converting session data into:

• JSON
• Markdown
• API‑ready dictionaries


This allows integration with dashboards, SIEMs, and SOC pipelines.

---

Roadmap

• Database persistence (SQLite/PostgreSQL)
• Web dashboard
• TUI interface
• Additional recon plugins
• CVSS scoring
• MITRE ATT&CK mapping
• Shodan integration
• Dockerized microservice version
