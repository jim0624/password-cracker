import hashlib

print("\n" + "="*50)
print("PASSWORD CRACKER - Educational Tool")
print("="*50 + "\n")

target_hash = "482c811da5d5b4bc6d497ffa98491e38"
print(f"Target Hash: {target_hash}\n")

passwords = ['password', '123456', 'admin', 'letmein', 'password123', 'monkey', 'dragon']

print("Testing passwords:\n")
for pwd in passwords:
    hash_result = hashlib.md5(pwd.encode()).hexdigest()
    match = "✓ MATCH FOUND!" if hash_result == target_hash else "✗"
    print(f"  {pwd:15} → {match}")

print("\n" + "="*50)
