from seal import KeyGenerator, SEALContext, EncryptionParameters

# Initialize encryption parameters
params = EncryptionParameters(scheme_type=BFV)
poly_modulus_degree = 4096
params.set_poly_modulus_degree(poly_modulus_degree)
params.set_coeff_modulus(seal.coeff_modulus_128(poly_modulus_degree))
params.set_plain_modulus(256)

context = SEALContext.Create(params)

# Generate keys
keygen = KeyGenerator(context)
public_key = keygen.public_key()
secret_key = keygen.secret_key()

# For this example, we print the keys. In a real system, you'd securely store these.
print(f"Public Key: {public_key}")
print(f"Secret Key: {secret_key}")