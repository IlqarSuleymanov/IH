IH Project - README
Project Overview
The IH Project is a comprehensive subdomain enumeration and vulnerability detection tool designed for bug bounty hunters and security researchers. The tool integrates multiple scanning methods and tools to automate the process of discovering subdomains, checking their availability, and identifying vulnerabilities.

The project is driven by Hunter.py, a master script that coordinates the execution of various sub-scripts to deliver an efficient, automated security scanning workflow.

How It Works
The tool runs several scripts in sequence to discover subdomains, check for live URLs, and scan for vulnerabilities. Here's a breakdown of the process:

Subdomain Discovery:

Scripts: icpd.py, sicpd.py, subfinder_runner.py
Tools Used: Subfinder, Waybackurls
The tool begins by fetching a list of domains from external sources (like bounty targets) and then uses Subfinder to enumerate subdomains. It checks if these subdomains are still live and functional before moving to the next stage.
URL Checking:

Script: subdomain_urlchecker.py
Tools Used: Waybackurls
This script verifies the validity of the discovered subdomains by checking if they are live. It generates a list of functional subdomains to be used for vulnerability scanning.
Vulnerability Scanning:

Script: nuclei.py
Tools Used: Nuclei
Once live subdomains are confirmed, the tool scans them using Nuclei for potential vulnerabilities, including low and critical vulnerabilities (excluding informational ones). Any vulnerabilities found are logged.
Notification System:

Script: notify.py
Tool: Telegram Bot (scopehunter_bot)
Whenever a new vulnerability is found and logged in combined_results.txt, the tool sends an alert through a Telegram bot, notifying the user of the findings in real time.
Master Control:

Script: Hunter.py
This script runs the entire workflow by executing all the steps above sequentially, ensuring that the process is fully automated.
Manual Configuration Changes
Before running the tool, certain settings and files need to be configured manually:

Target List (domains.txt):

The tool relies on a target list located in domains.txt (or wildcards.txt). Manually populate this file with the domains or wildcard entries you want to target.
The file should be placed in the correct location (in the project root or assets/ if following the organized structure).
Telegram Bot Token:

You need to set up a Telegram bot and retrieve the bot token to enable notifications.
Steps:
Create a bot using BotFather.
Copy the token provided by BotFather.
Paste the token in the notify.py script where the bot token is required.
python
Copy code
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
Additionally, update the chat ID to send messages to your Telegram account:
python
Copy code
chat_id = 'YOUR_TELEGRAM_CHAT_ID'
File Paths:

If you move any files (such as wildcards.txt, domains.txt, or output files), make sure to update the paths in the relevant scripts.
Example:
python
Copy code
with open('assets/wildcards.txt', 'r') as file:
Nuclei Templates:

Make sure you have the right Nuclei templates installed. You can download the latest Nuclei templates with:
bash
Copy code
nuclei -ut
Customize the template path in nuclei.py if you are using custom templates.
Subfinder Configuration:

Subfinder uses various APIs for subdomain discovery. Ensure you have your API keys set up in ~/.config/subfinder/provider-config.yaml.
Usage
To start the tool, run the master script Hunter.py. This script will automatically manage all the sub-scripts and tools in the correct order.

bash
Copy code
python3 Hunter.py
Make sure you have installed all the necessary dependencies for each tool (Subfinder, Nuclei, Waybackurls, etc.). Follow the individual tool installation instructions for setup.

Toolchain Overview
Subfinder: Enumerates subdomains from various sources.
Waybackurls: Gathers archived URLs for identified subdomains.
Nuclei: Scans URLs for vulnerabilities using pre-built templates.
Telegram Bot: Sends notifications for any critical vulnerabilities found.
Files and Scripts
icpd.py: Fetches domains and starts subdomain enumeration.
sicpd.py: Supplementary script for fetching wildcards and additional domains.
subfinder_runner.py: Runs Subfinder to find subdomains.
subdomain_urlchecker.py: Checks which subdomains are live and saves the working ones.
nuclei.py: Runs Nuclei to scan subdomains for vulnerabilities.
notify.py: Sends notifications through Telegram if vulnerabilities are found.
Hunter.py: The main script that orchestrates the execution of all the above scripts.
Output Files
subdomains_results.txt: Contains the results of the subdomain enumeration.
final_subdomains.txt: Contains the live subdomains for vulnerability scanning.
combined_results.txt: Contains the results of vulnerability scans.
new_domains.txt: Contains newly discovered domains for future scans.
Dependencies
Before running the tool, ensure you have the following tools installed:

Subfinder
Nuclei
Waybackurls
Python 3.x
Telegram bot (for notifications)
Future Updates
The tool can be updated and maintained via GitHub, and users can download the latest version using the provided instructions. If any updates are made after the initial release, simply clone or pull the latest version from the repository.
