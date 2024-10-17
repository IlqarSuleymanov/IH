import subprocess
import re

def clean_input_file(input_file):
    """Remove asterisk symbols and ensure proper domain formatting."""
    try:
        with open(input_file, 'r') as file:
            # Read domains and remove leading asterisks and dots
            domains = file.readlines()
            cleaned_domains = []

            for domain in domains:
                # Remove leading asterisks and dots, then strip whitespace
                cleaned_domain = domain.lstrip('*').lstrip('.').strip()

                # Check if it ends with a valid TLD; if not, add ".com" (or handle as needed)
                if not re.search(r'\.(com|org|net|edu|gov|io|co|info|biz)$', cleaned_domain):
                    cleaned_domain += '.com'  # Default to .com; modify as needed

                cleaned_domains.append(cleaned_domain)

        # Write the cleaned domains back to the input file
        with open(input_file, 'w') as file:
            file.write('\n'.join(cleaned_domains))

        print(f"Removed asterisk symbols and formatted domains in {input_file}.")
        
    except Exception as e:
        print(f"An error occurred while cleaning the input file: {e}")

def run_subfinder(input_file, output_file):
    try:
        # Clean the input file before processing
        clean_input_file(input_file)
        
        # Read domains from new_subdomains.txt
        with open(input_file, 'r') as file:
            domains = file.read().strip()

        # Check if there are domains to process
        if domains:
            # Run Subfinder
            command = f"subfinder -d \"{domains}\" -o {output_file}"
            subprocess.run(command, shell=True, check=True)
            print(f"Subfinder has processed the domains and saved results to {output_file}.")
        else:
            print("No domains found in the input file.")

    except subprocess.CalledProcessError as e:
        print(f"Error running Subfinder: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clear new_subdomains.txt after processing
        with open(input_file, 'w') as file:
            file.write("")  # Empty the file
        print(f"Cleared contents of {input_file}.")
        
if __name__ == "__main__":
    input_file = 'new_subdomains.txt'
    output_file = 'subdomains_results.txt'
    
    run_subfinder(input_file, output_file)

