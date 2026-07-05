import subprocess

class Plugin:
    name = "enum4linux"

    def run(self, target):
        cmd = ["enum4linux", "-a", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
