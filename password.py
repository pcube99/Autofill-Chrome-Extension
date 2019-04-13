from cryptography.fernet import Fernet
key = Fernet.generate_key() #this is your "password"
cipher_suite = Fernet(key)
def encrypt(password):
    encoded_text = cipher_suite.encrypt(bytes(password, "utf-8"))
    return str(encoded_text).split("'")[1]

def decrypt(password):
    password = bytes(password, "utf-8")
    decoded_text = cipher_suite.decrypt(password)
    return (str(decoded_text).split("'")[1])