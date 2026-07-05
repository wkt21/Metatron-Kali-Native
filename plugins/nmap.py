import subprocess

class Plugin:
    name = "nmap"

    def run(self, target):
        cmd = ["nmap", "-sV", "-Pn", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
