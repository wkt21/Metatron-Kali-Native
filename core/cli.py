from core.session import Session
from core.loader import load_plugins
from core.analysis import analyse_target
from utils.helpers import prompt, info, success, warn

class WKT12CLI:
    def __init__(self):
        self.plugins = load_plugins()

    def run(self):
        while True:
            print("\n[1] New Scan")
            print("[2] Exit")
            choice = prompt("wkt12> ")

            if choice == "1":
                self.new_scan()
            elif choice == "2":
                print("Exiting WKT12.")
                break
            else:
                warn("Invalid choice.")

    def new_scan(self):
        target = prompt("Enter target: ")
        session = Session(target)

        info("Running recon plugins...")
        for plugin in self.plugins:
            info(f"Running {plugin.name}...")
            output = plugin.run(target)
            session.add_recon(plugin.name, output)

        info("Running AI analysis...")
        analysis = analyse_target(target, session.recon)
        session.add_analysis(analysis)

        success("Scan complete.")
        print(session.to_dict())
