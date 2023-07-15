# fyta_plants_checker
A simple program that checks on your plants using the Fyta API.

### Requirements
- **Python 3.11** (It might work in other Python versions, but is untested.)
- **Fyta API token**, which you can generate from the [Fyta Developer Dashboard](https://web.fyta.de/)
- **Google Account App Credentials**
- You can manage the virtual environment using **[Poetry](https://python-poetry.org/)**
- A **`fyta.conf` file** at the root of the project, in the following format:
```ini
[fyta_auth]
token=abc
[email_config]
email=xyz@gmail.com
password=********
to=SomeEmail@gmail.com
```