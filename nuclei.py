import subprocess

# Paths for final subdomains and new domains
final_subdomains_file = 'final_subdomains.txt'
new_domains_file = 'new_domains.txt'
nuclei_template_path = '/home/kali/.local/nuclei-templates/'  # Adjust the path if necessary
combined_output_file = 'combined_results.txt'  # Combined output file

# Function to run Nuclei and filter results
def run_nuclei_scan(subdomains_file):
    print(f"Running Nuclei scan for {subdomains_file}...")
    subprocess.run([
        'nuclei',
        '-l', subdomains_file,
        '-t', nuclei_template_path,
        '-o', 'temp_results.txt'  # Temporary output file
    ])

    print(f"Scan completed for {subdomains_file}. Filtering results...")

    # Filter results to keep only low, medium, high, and critical vulnerabilities, skipping informational
    with open('temp_results.txt', 'r') as results_file:
        results = results_file.readlines()

    # Filter for low, medium, high, and critical vulnerabilities while skipping informational
    filtered_results = [
        line for line in results if 'info' not in line.lower()
    ]

    return filtered_results  # Return filtered results

# Function to clear subdomains file
def clear_file(subdomains_file):
    with open(subdomains_file, 'w') as f:
        f.write("")  # Clear the file
    print(f"Cleared contents of {subdomains_file}.")

# Run Nuclei scan for final_subdomains.txt and new_domains.txt
all_filtered_results = []
all_filtered_results.extend(run_nuclei_scan(final_subdomains_file))
clear_file(final_subdomains_file)

all_filtered_results.extend(run_nuclei_scan(new_domains_file))
clear_file(new_domains_file)

# Write combined results to output file
with open(combined_output_file, 'w') as combined_file:
    combined_file.writelines(all_filtered_results)

print(f"Combined results written to {combined_output_file}.")

