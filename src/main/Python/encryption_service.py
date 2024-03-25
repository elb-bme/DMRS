from seal import Encryptor, Plaintext, Ciphertext

# Assuming 'public_key' is available from Step 1
encryptor = Encryptor(context, public_key)

# Simulate a meter reading
meter_reading = 100  # This would be dynamically obtained in a real scenario

# Encrypt the meter reading
plain_meter_reading = Plaintext(str(meter_reading))
encrypted_meter_reading = Ciphertext()
encryptor.encrypt(plain_meter_reading, encrypted_meter_reading)

# The encrypted_meter_reading can now be safely stored on the blockchain