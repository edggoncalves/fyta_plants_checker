# fyta_plants_checker
A simple program that checks on your plants using the Fyta API.

### Requirements
1. Fyta API token, which you can generate from the [Fyta Developer Dashboard](https://web.fyta.de/)
2. Google Account App Credentials
3. A `fyta.conf` file at the root of the project, in the following format:
```ini
[fyta_auth]
token=abc
[email_config]
email=xyz@gmail.com
password=********
to=SomeEmail@gmail.com
```