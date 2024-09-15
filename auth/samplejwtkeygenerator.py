import secrets
import base64

def generatejwtkey():

    securestring = secrets.token_bytes(32)
    print(securestring)
    secret_key = securestring.hex()
    return secret_key

secretkey = generatejwtkey()
print(secretkey)
