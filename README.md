# Windows active system

## Instructions

- Create a environment with `python -m venv venv`
- Activate the environment `./venv/scripts/activate.ps1`
- Install dependency `python -m pip install -r requirements.txt`
- Install Make `choco install make`
- Create executable `make build`

Create a JSON file with name `keys.json` and put the keys you need (find some on internet), put the file with `activator.exe`

```json
{
  "windows10": {
    "pro": {
      "normal": [],
      "pro_education": [],
      "pro_education_n": [],
      "pro_n": [],
      "pro_serial": []
    },
    "home": {
      "normal": [],
      "home_single_language": [],
      "education": [],
      "education_n": []
    },
    "enterprise": {
      "normal": [],
      "enterprise_g": [],
      "enterprise_gn": [],
      "enterprise_n": []
    }
  }
}
```
