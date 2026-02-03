import base64

USERNAME = "admin"
PASSWORD = "password123"


def is_authenticated(headers):
    auth_header = headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Basic "):
        return False

    try:
        encoded_credentials = auth_header.split(" ")[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
        username, password = decoded_credentials.split(":", 1)
    except Exception:
        return False

    return username == USERNAME and password == PASSWORD
