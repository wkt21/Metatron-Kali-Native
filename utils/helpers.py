def prompt(text):
    return input(f"{text} ").strip()

def info(text):
    print(f"[INFO] {text}")

def success(text):
    print(f"[OK] {text}")

def warn(text):
    print(f"[WARN] {text}")
