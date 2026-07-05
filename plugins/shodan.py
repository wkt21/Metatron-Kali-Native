import os
import requests

class Plugin:
    name = "shodan"

    def run(self, target):
        api_key = os.getenv("SHODAN_API_KEY")
        if not api_key:
            return "Shodan API key not set."

        url = f"https://api.shodan.io/shodan/host/{target}?key={api_key}"
        try:
            r = requests.get(url)
            return r.text
        except Exception as e:
            return str(e)
