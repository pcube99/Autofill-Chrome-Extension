
import rncryptor
data = '123'
password = '123'

# rncryptor.RNCryptor's methods
# cryptor = rncryptor.RNCryptor()
# encrypted_data = cryptor.encrypt(data, password)
# decrypted_data = cryptor.decrypt(encrypted_data, password)
# assert data == decrypted_data
# print(encrypted_data)
# print(decrypted_data)
# # rncryptor's functions
encrypted_data = rncryptor.encrypt(data, password)
decrypted_data = rncryptor.decrypt(encrypted_data, password)
assert data == decrypted_data
print(encrypted_data)
print(decrypted_data)