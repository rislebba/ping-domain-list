import subprocess
import platform

def ping_domain(domain):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", domain],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error pinging {domain}: {e}")
        return False

def ping_domains_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            domains = [line.strip() for line in file if line.strip()]
        
        for domain in domains:
            status = ping_domain(domain)
            print(f"{domain}: {'Reachable' if status else 'Unreachable'}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

# This line calls the function with your domain file name
ping_domains_from_file("my_domains.txt")
