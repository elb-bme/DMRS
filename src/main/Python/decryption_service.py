from seal import Decryptor, Plaintext

# Assuming 'secret_key' is available from Step 1
decryptor = Decryptor(context, secret_key)

# Assuming 'encrypted_total' is the aggregated encrypted total consumption
plain_total = Plaintext()
decryptor.decrypt(encrypted_total, plain_total)

total_consumption = int(plain_total.to_string())

# Now, 'total_consumption' can be used for billing calculations