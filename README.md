# QA Automation Admin App

UI automation framework for the Admin application using Python, Pytest, and Playwright.

## Tech Stack

- Python
- Pytest
- Playwright (sync API)
- PyJWT

## Project Structure

- `auth/`: token/session handling and local storage injection
- `configs/`: environment-based config files (`qa.json`, `dev.json`, `prod.json`)
- `pages/`: page objects, locators, and reusable UI components
- `tests/`: test suites (`UI` and `api` folders)
- `utils/`: shared utilities (config loader)
- `data/`: persisted auth storage

## Prerequisites

- Python 3.10+
- pip

## Installation

1. Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install -r requirements.txt
```

3. Install Playwright browser binaries.

```powershell
python -m playwright install chromium
```

## Configuration

Configuration is loaded by environment name from `configs/<ENV>.json`.

- Default: `ENV=qa`
- Supported values: `qa`, `dev`, `prod`

Example (PowerShell):

```powershell
$env:ENV = "qa"
```

## Run Tests

Run all tests:

```powershell
pytest -s
```

Run only UI tests:

```powershell
pytest -s tests/UI
```

## Notes

- The framework caches auth storage in `data/auth_storage.json` and reuses it when token is still valid.
- Browser runs headless in CI when `CI=true`, otherwise headed mode is used.