# Security Policy

## Supported Versions

Currently, the `main` branch of Startup-Global is supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of Startup-Global and the data of founders and investors extremely seriously. 

If you discover any security vulnerabilities, please do NOT report them through public GitHub issues. Instead, please email our security team directly:

**Email:** support@buygit.com

Please include the following information in your report:
- Type of vulnerability (e.g., XSS, SQLi, IDOR, etc.)
- Steps to reproduce the issue
- Potential impact
- Any relevant code snippets or screenshots

We will acknowledge your report within 48 hours and provide an estimated timeline for resolution and disclosure.

## Security Practices
- Automated Dependency Scanning is enforced via GitHub Actions.
- Admin APIs require a highly-secure `X-Admin-Key` header to interact with Crawler and Refresh endpoints.
- Database operations are executed using parameterized queries via SQLAlchemy to prevent SQL injection.
