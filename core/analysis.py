import re

class Vulnerability:
    def __init__(self, name, severity, description, port=None, service=None, fix=None):
        self.name = name
        self.severity = severity
        self.description = description
        self.port = port
        self.service = service
        self.fix = fix

    def to_dict(self):
        return {
            "name": self.name,
            "severity": self.severity,
            "description": self.description,
            "port": self.port,
            "service": self.service,
            "fix": self.fix
        }


def extract_from_nmap(nmap_output):
    vulns = []

    for line in nmap_output.splitlines():
        if "ssl" in line.lower() and "deprecated" in line.lower():
            vulns.append(Vulnerability(
                name="Deprecated SSL Protocol",
                severity="HIGH",
                description="Service supports deprecated SSL/TLS versions.",
                port=re.findall(r"(\d+)/", line)[0] if "/" in line else None,
                service="ssl",
                fix="Disable SSLv2/SSLv3 and enforce TLS 1.2+"
            ))

        if "apache" in line.lower() and "2.2" in line.lower():
            vulns.append(Vulnerability(
                name="Outdated Apache Version",
                severity="MEDIUM",
                description="Apache 2.2 is outdated and contains known vulnerabilities.",
                port=re.findall(r"(\d+)/", line)[0] if "/" in line else None,
                service="http",
                fix="Upgrade Apache to a supported version"
            ))

    return vulns


def extract_from_whatweb(output):
    vulns = []

    if "WordPress" in output and "4." in output:
        vulns.append(Vulnerability(
            name="Outdated WordPress",
            severity="HIGH",
            description="WordPress 4.x contains multiple known vulnerabilities.",
            service="http",
            fix="Upgrade WordPress to the latest stable version"
        ))

    return vulns


def extract_from_wafw00f(output):
    vulns = []

    if "No WAF detected" in output:
        vulns.append(Vulnerability(
            name="No Web Application Firewall",
            severity="LOW",
            description="Target does not appear to use a WAF.",
            fix="Deploy a WAF such as ModSecurity or Cloudflare"
        ))

    return vulns


def extract_from_nuclei(output):
    vulns = []

    for line in output.splitlines():
        if "critical" in line.lower():
            vulns.append(Vulnerability(
                name="Critical Nuclei Finding",
                severity="CRITICAL",
                description=line.strip(),
                fix="Review the finding and apply vendor patches"
            ))

    return vulns


def analyse_target(target, recon_data):
    all_vulns = []

    if "nmap" in recon_data:
        all_vulns.extend(extract_from_nmap(recon_data["nmap"]))

    if "whatweb" in recon_data:
        all_vulns.extend(extract_from_whatweb(recon_data["whatweb"]))

    if "wafw00f" in recon_data:
        all_vulns.extend(extract_from_wafw00f(recon_data["wafw00f"]))

    if "nuclei" in recon_data:
        all_vulns.extend(extract_from_nuclei(recon_data["nuclei"]))

    return {
        "target": target,
        "risk": "HIGH" if any(v.severity in ("CRITICAL", "HIGH") for v in all_vulns) else "MEDIUM",
        "vulner
