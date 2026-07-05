import subprocess

class Plugin:
    name = "sslscan"

    def run(self, target):
        cmd = ["sslscan", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
