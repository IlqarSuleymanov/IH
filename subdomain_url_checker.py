import subprocess

# Define the input and output file names
input_file = 'subdomains_results.txt'
output_file = 'final_subdomains.txt'

def get_working_urls(input_file, output_file):
    # Clear the output file before writing new data
    with open(output_file, 'w') as f:
        pass  # Just opening in write mode clears the file

    # Open the input file and read subdomains
    with open(input_file, 'r') as f:
        subdomains = f.read().splitlines()

    working_urls = []

    # Iterate through each subdomain
    for subdomain in subdomains:
        print(f"Processing {subdomain}...")  # Log the subdomain being processed
        # Use Waybackurls to get the URLs for each subdomain
        try:
            result = subprocess.run(['waybackurls', subdomain], capture_output=True, text=True, check=True)
            urls = result.stdout.splitlines()

            # Filter out 404 errors or any unwanted URLs (optional)
            for url in urls:
                if '404 Not Found' not in url and url:
                    working_urls.append(url)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {subdomain}: {e}")

    # Write the working URLs to the output file
    with open(output_file, 'a') as f:  # Append mode to add results
        for url in working_urls:
            f.write(f"{url}\n")

    # Clear the input file after processing to avoid reusing the same subdomains
    with open(input_file, 'w') as f:
        pass  # This clears the file

# Run the function
get_working_urls(input_file, output_file)

