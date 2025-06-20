# API Security Compliance Matrix (OWASP API Top 10)

**Target:** OWASP Juice Shop (`https://juice-shop.herokuapp.com`)
**Date:** (Update this with today's date)

| OWASP ID      | Vulnerability Category                      | Test Case in Postman                                     | Automation Status | Last Result | Notes                                           |
|---------------|---------------------------------------------|----------------------------------------------------------|-------------------|-------------|-------------------------------------------------|
| **API1:2023** | Broken Object Level Authorization (BOLA)    | `(FAIL) Try to access another user's basket`             | Automated         | ❌ FAIL     | Vulnerable! API returned 200 OK when a 403 was expected. |                                                 |
| **API2:2023** | Broken Authentication                       | `(FAIL) Access protected endpoint (Basket) with NO token`| Automated         | ✅ PASS     | Secure. Endpoint correctly blocked access with a 401 status. |                                            
| **API5:2023** | Broken Function Level Authorization (BFLA)  | `(FAIL) Try to access admin-only metrics endpoint`       | Automated         | ⚠️ TBD      |                                                 |
| **API7:2023** | Server Side Request Forgery (SSRF)          | `(FAIL) Try to make server request file from internal URL` | Automated         | ⚠️ TBD      |                                                 |
| **API8:2023** | Security Misconfiguration                   | `(FAIL) Check for revealing X-Powered-By header`         | Automated         | ⚠️ TBD      |                                                 |
| **API9:2023** | Improper Inventory Management               | `(FAIL) Access exposed FTP folder`                       | Automated         | ⚠️ TBD      |                                                 |
| **API10:2023**| Unsafe Consumption of APIs                  | `(FAIL) Test for Open Redirect`                          | Automated         | ⚠️ TBD      |                                                 |

**Legend:**
- ✅ **PASS:** The API correctly blocked the attack.
- ❌ **FAIL:** The test failed, indicating a vulnerability.
- ⚠️ **TBD:** Test to be determined or needs manual verification.