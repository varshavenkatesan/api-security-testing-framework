#!/bin/bash

# --- Configuration ---
COLLECTION_FILE="postman/collections/JuiceShop_API_Security_Tests.postman_collection.json"
ENVIRONMENT_FILE="postman/environments/JuiceShop_Public_API.postman_environment.json"
REPORT_DIR="reports"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
REPORT_FILE="$REPORT_DIR/juice_shop_security_report_$TIMESTAMP.html"

# --- Create report directory if it doesn't exist ---
mkdir -p $REPORT_DIR

# --- Run Newman ---
echo "Starting API Security Scan on OWASP Juice Shop..."

newman run "$COLLECTION_FILE" \
    -e "$ENVIRONMENT_FILE" \
    -r htmlextra \
    --reporter-htmlextra-export "$REPORT_FILE" \
    --reporter-htmlextra-title "Juice Shop API Security Report" \
    --suppress-exit-code

echo "Scan complete. Report generated at: $REPORT_FILE"