#!/usr/bin/env python3
"""
URL Status Checker Script
Extracts all gitbookUrl values from a JSON sitemap and checks their HTTP status codes.

## Python Script Overview

**Main Functions:**

1. **`extract_urls_from_json(json_file)`**
   - Reads the JSON sitemap file
   - Recursively searches through the JSON structure
   - Extracts all `gitbookUrl` values into a list

2. **`check_url_status(url, timeout=10)`**
   - Uses `curl` command to check HTTP status codes
   - Returns the status code (e.g., '200', '404')
   - Handles errors gracefully

3. **`categorize_status_code(status_code)`**
   - Categorizes status codes into:
     - `2xx` (Success)
     - `4xx` (Client Error)
     - `other` (Redirects, Server Errors, etc.)

4. **`main()`**
   - Orchestrates the entire process
   - Displays progress for each URL
   - Generates formatted summary report

## How to Use

```bash
# Make it executable
chmod +x curl_status.py

# Run it
python3 curl_status.py
```

**Requirements:**
- Python 3.x
- `curl` command-line tool (usually pre-installed on Linux/Mac)
- JSON file path: `/full-path/filename.json`
"""

import json
import subprocess
from collections import defaultdict

def extract_urls_from_json(json_file):
    """
    Extract all gitbookUrl values from the JSON file recursively.
    
    Args:
        json_file: Path to the JSON file
        
    Returns:
        List of URL strings
    """
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    urls = []
    
    def extract_urls(obj):
        """Recursively search for gitbookUrl in JSON objects"""
        if isinstance(obj, dict):
            if 'gitbookUrl' in obj:
                urls.append(obj['gitbookUrl'])
            for value in obj.values():
                extract_urls(value)
        elif isinstance(obj, list):
            for item in obj:
                extract_urls(item)
    
    extract_urls(data)
    return urls


def check_url_status(url, timeout=10):
    """
    Check HTTP status code of a URL using curl.
    
    Args:
        url: URL to check
        timeout: Request timeout in seconds
        
    Returns:
        Status code as string, or 'ERROR' if request fails
    """
    try:
        result = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', url],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error checking {url}: {str(e)}")
        return 'ERROR'


def categorize_status_code(status_code):
    """
    Categorize HTTP status code.
    
    Args:
        status_code: Status code string
        
    Returns:
        Category: '2xx', '4xx', 'other'
    """
    if status_code.startswith('2'):
        return '2xx'
    elif status_code.startswith('4'):
        return '4xx'
    else:
        return 'other'


def main():
    """Main function to run the URL status checker"""
    
    # Get JSON file path from user input
    json_file = input("Enter the path to your JSON sitemap file: ").strip()
    
    # Validate file exists and is readable
    try:
        with open(json_file, 'r') as f:
            pass  # Just checking if file is readable
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        return
    except IOError as e:
        print(f"Error: Unable to read file '{json_file}': {e}")
        return
    
    print(f"\nExtracting URLs from JSON file: {json_file}")
    try:
        urls = extract_urls_from_json(json_file)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON file. {e}")
        return
    
    if not urls:
        print("No URLs found in the JSON file.")
        return
    
    # Check status codes
    status_results = defaultdict(list)
    print(f"Checking {len(urls)} URLs...\n")
    
    for idx, url in enumerate(urls, 1):
        status_code = check_url_status(url)
        print(f"[{idx:3d}] Status {status_code} - {url}")
        status_results[status_code].append(url)
    
    # Generate summary
    print("\n" + "="*70)
    print("URL STATUS CHECK SUMMARY")
    print("="*70)
    print(f"\nTotal URLs: {len(urls)}")
    
    # Count 2xx and 4xx
    count_2xx = sum(len(urls_list) for code, urls_list in status_results.items() if code.startswith('2'))
    count_4xx = sum(len(urls_list) for code, urls_list in status_results.items() if code.startswith('4'))
    count_other = len(urls) - count_2xx - count_4xx
    
    print(f"2XX Status Codes: {count_2xx}")
    print(f"4XX Status Codes: {count_4xx}")
    print(f"Other Status Codes: {count_other}")
    
    # Print detailed results for 2XX
    print("\n" + "-"*70)
    print("URLs with 2XX Status (Successful):")
    print("-"*70)
    for code in sorted([k for k in status_results.keys() if k.startswith('2')]):
        print(f"\n{code}:")
        for url in status_results[code]:
            print(f"  ✓ {url}")
    
    # Print detailed results for 4XX
    print("\n" + "-"*70)
    print("URLs with 4XX Status (Client Errors):")
    print("-"*70)
    four_xx_codes = sorted([k for k in status_results.keys() if k.startswith('4')])
    if four_xx_codes:
        for code in four_xx_codes:
            print(f"\n{code}:")
            for url in status_results[code]:
                print(f"  ✗ {url}")
    else:
        print("None - All URLs are accessible!")
    
    # Print detailed results for other status codes
    other_codes = sorted([k for k in status_results.keys() if not k.startswith(('2', '4'))])
    if other_codes:
        print("\n" + "-"*70)
        print("URLs with Other Status Codes:")
        print("-"*70)
        for code in other_codes:
            print(f"\n{code}:")
            for url in status_results[code]:
                print(f"  ? {url}")


if __name__ == "__main__":
    main()