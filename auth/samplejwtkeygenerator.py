import secrets
import base64

def generatejwtkey():

    securestring = secrets.token_bytes(32)
    print(securestring)
    secret_key = securestring.hex()
    return secret_key
secretkey = "88f6f562a7bada53023f1bf103965c877acea3901b52b3dead41dc830f974b99"
print(secretkey)
