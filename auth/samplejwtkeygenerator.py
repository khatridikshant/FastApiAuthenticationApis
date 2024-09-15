import secrets
import base64

async def generatejwtkey():

    securestring = secrets.token_bytes(32)
    print(securestring)
    secret_key = securestring.hex()
    return await secret_key

secretkey = str(generatejwtkey())
print(secretkey)
