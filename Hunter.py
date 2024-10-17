import subprocess

def run_icpd():
    print("Running icpd.py...")
    subprocess.run(["python3", "icpd.py"])
    print("icpd.py completed.")

def run_Sicpd():
    print("Running Sicpd.py...")
    subprocess.run(["python3", "Sicpd.py"])
    print("Sicpd.py completed.")

def run_subfinder_runner():
    print("Running subfinder_runner.py...")
    subprocess.run(["python3", "subfinder_runner.py"])
    print("subfinder_runner.py completed.")

def run_subdomain_url_checker():
    print("Running subdomain_url_checker.py...")
    subprocess.run(["python3", "subdomain_url_checker.py"])
    print("subdomain_url_checker.py completed.")

def run_nuclei():
    print("Running nuclei.py...")
    subprocess.run(["python3", "nuclei.py"])
    print("nuclei.py completed.")

def main():
    # Run scripts in the specified order
    run_icpd()
    run_Sicpd()
    run_subfinder_runner()
    run_subdomain_url_checker()
    run_nuclei()

if __name__ == "__main__":
    main()

