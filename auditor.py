
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
