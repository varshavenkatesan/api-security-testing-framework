# API Security Testing Framework

This project is a comprehensive and repeatable framework designed to assess REST APIs for security vulnerabilities based on the **OWASP API Security Top 10**.

It uses a combination of Postman for test case development, Newman for command-line automation, and custom scripting to create a full testing pipeline. The framework is demonstrated using the intentionally vulnerable OWASP Juice Shop API as its target.

---

### Key Components

*   **Postman Test Suite:** A collection of structured negative test cases, each designed to probe for a specific OWASP API Top 10 vulnerability.
*   **Automation Script (`run-tests.sh`):** A shell script that executes the entire test suite from the command line using Newman, generating a detailed HTML report.
*   **Compliance Matrix (`docs/compliance_matrix.md`):** A high-level dashboard that maps test results to the OWASP Top 10 categories, providing a clear, human-readable summary of the API's security posture.

### Technology Stack

*   **Postman:** For building and managing API requests.
*   **Newman:** For test automation and reporting.
*   **`newman-reporter-htmlextra`:** For generating detailed HTML reports.
*   **OWASP Juice Shop:** The target vulnerable API for demonstration.
*   **Shell Scripting / Git Bash:** For running the automation script.

---

### How to Run This Framework

1.  **Prerequisites:**
    *   Node.js and npm must be installed.
    *   Install Newman and the HTML reporter globally:
        ```bash
        npm install -g newman newman-reporter-htmlextra
        ```
    *   Git Bash (on Windows) or a standard terminal (on macOS/Linux).

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/varshavenkatesan/api-security-testing-framework.git
    cd api-security-testing-framework
    ```

3.  **Manual Setup (CRITICAL):**
    *   This repository **intentionally does not include** the Postman Environment file to protect sensitive credentials.
    *   You must create it manually in Postman:
        *   Create a new Environment named `JuiceShop_Public_API`.
        *   Add the following variables: `baseUrl` (set to `https://juice-shop.herokuapp.com`), `user_email`, and `user_password`.
        *   Fill in the `user_email` and `user_password` with the credentials you registered on the Juice Shop website.

4.  **Execute the Scan:**
    *   Run the automation script from the root of the project directory using Git Bash:
        ```bash
    sh run-tests.sh
    ```

5.  **View the Results:**
    *   A new, timestamped HTML report will be generated inside the `/reports` directory.
    *   Open this file in a web browser to see the detailed test results.