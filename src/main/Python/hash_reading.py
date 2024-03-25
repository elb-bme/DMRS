import hashlib
import json

def generate_commitment(reading, nonce):
    # Combine the reading and nonce
    combined = json.dumps({'reading': reading, 'nonce': nonce})
    # Generate a hash (commitment)
    commitment = hashlib.sha256(combined.encode()).hexdigest()
    return commitment