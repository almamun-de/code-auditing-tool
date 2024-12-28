# Code Auditing Tool

This is a simple Python-based tool to audit Python and JavaScript code for common security vulnerabilities like SQL Injection, XSS, weak hashing algorithms, and hardcoded passwords.

## Features
- Detects common vulnerabilities using pattern matching.
- Scans Python (`.py`) and JavaScript (`.js`) files for security risks.
- Displays potential vulnerabilities, their descriptions, and suggested fixes.

## How It Works
The tool scans your codebase for vulnerabilities based on patterns defined in the `vulnerabilities.json` file. Each pattern corresponds to a specific security issue, such as SQL Injection or XSS.

## Requirements
- Python 3.x

## How to Use
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/code-auditing-tool.git
    ```

2. Add your project files to the directory or point the script to the correct folder.

3. Run the tool:
    ```bash
    python auditor.py
    ```

4. The tool will scan Python and JavaScript files for potential vulnerabilities and print the results to the console.

## Adding New Vulnerabilities
To add new vulnerability patterns, edit the `vulnerabilities.json` file and include new entries with the following structure:
```json
{
    "Vulnerability Name": {
        "pattern": "regex_pattern",
        "description": "Brief description of the vulnerability",
        "solution": "Suggested solution"
    }
}
```
