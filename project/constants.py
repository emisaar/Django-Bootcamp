# from jwt import HMACSHA256, base64UrlEncode

def encrypt_key():
    return "DbFeS#pK/r6KfkY6rsH33QybF7OVrIW/"

    # return HMACSHA256(
    #     base64UrlEncode(data.header) + "." +
    #     base64UrlEncode(data.payload)
    # )

    # return os.environ.get('SECRET_KEY').encode("utf-8")