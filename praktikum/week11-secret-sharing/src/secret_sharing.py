from secretsharing import SecretSharer

# secret asli
secret_text = "KriptografiUPB2025"

# ubah ke hex (WAJIB)
secret_hex = secret_text.encode().hex()

shares = SecretSharer.split_secret(secret_hex, 3, 5)
print("Shares:", shares)

# rekonstruksi
recovered_hex = SecretSharer.recover_secret(shares[:3])

# balikin ke string asli
recovered_text = bytes.fromhex(recovered_hex).decode()

print("Recovered secret:", recovered_text)