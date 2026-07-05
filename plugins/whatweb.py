import subprocess

class Plugin:
    name = "whatweb"

    def run(self, target):
        cmd = ["whatweb", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
