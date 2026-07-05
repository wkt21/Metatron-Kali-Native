def analyse_target(target, recon_data):
    return {
        "target": target,
        "risk": "MEDIUM",
        "vulnerabilities": [],
        "exploits": [],
        "summary": f"Analysis for {target} completed.",
        "raw": recon_data
    }
