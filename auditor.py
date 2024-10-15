import re
import os
import json

# Load vulnerability patterns from the JSON file
def load_vulnerabilities():
    with open('vulnerabilities.json') as f:
        return json.load(f)

# Function to scan a file for vulnerabilities
def scan_file(file_path, vulnerabilities):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Check each line against vulnerability patterns
        for line_num, line in enumerate(lines, start=1):
            for vuln_name, vuln_data in vulnerabilities.items():
                pattern = vuln_data['pattern']
                if re.search(pattern, line):
                    print(f"Potential {vuln_name} vulnerability found in {file_path} at line {line_num}:")
                    print(f"    {line.strip()}")
                    print(f"    Description: {vuln_data['description']}")
                    print(f"    Solution: {vuln_data['solution']}\n")

# Function to scan a directory for files with specific extensions (Python, JavaScript)
def scan_directory(directory, vulnerabilities):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js')):  # Scan Python and JavaScript files
                file_path = os.path.join(root, file)
                print(f"Scanning {file_path}...")
                scan_file(file_path, vulnerabilities)

if __name__ == "__main__":
    vulnerabilities = load_vulnerabilities()
    target_directory = "./"  # Scan the current directory by default
    scan_directory(target_directory, vulnerabilities)
