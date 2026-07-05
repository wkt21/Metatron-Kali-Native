import subprocess

class Plugin:
    name = "gobuster"

    def run(self, target):
        cmd = ["gobuster", "dir", "-u", target, "-w", "/usr/share/wordlists/dirb/common.txt"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
