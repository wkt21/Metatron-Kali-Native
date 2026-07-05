import subprocess

class Plugin:
    name = "nuclei"

    def run(self, target):
        cmd = ["nuclei", "-u", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
