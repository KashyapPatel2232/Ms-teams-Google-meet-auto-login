# Microsoft Teams and Google Meet Auto Login

This project automates the Microsoft Teams sign-in flow using Selenium. It is intended for local personal use and should only be used with accounts you are authorized to access.

## Overview

The repository contains:

- `Auto_login.py` - Selenium automation for logging in to Microsoft Teams
- `Credential.example.py` - template for local configuration
- `requirements.txt` - Python dependencies
- `.gitignore` - ignores local secrets and environment files

## Requirements

- Python 3.9 or later
- Google Chrome installed
- ChromeDriver available on your system PATH
- A Microsoft account with access to the target Teams environment

## Setup

1. Clone the repository.
2. Create a virtual environment.
3. Install the dependencies.
4. Create a local credential file from the example template.
5. Run the script.

### Linux and macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp Credential.example.py Credential.py
python Auto_login.py
```

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item Credential.example.py Credential.py
python .\Auto_login.py
```

## Credentials

Create `Credential.py` with your local values:

```python
username = "your_email@example.com"
passkey = "your_password"
```

Do not commit real credentials to version control.

## Project structure

```text
.
├── Auto_login.py
├── Credential.example.py
├── Credential.py
├── requirements.txt
├── .gitignore
├── README.md
```

## Notes

- This script depends on the current Microsoft Teams UI and may need updates if the login flow changes.
- Keep credentials secure and do not store them in shared environments.
- Use this only for authorized and supported workflows.

## License

This project does not currently include a license file. If you intend to share or distribute it publicly, add an appropriate open-source license.
