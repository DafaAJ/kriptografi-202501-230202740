import hashlib

password = input("Masukkan password: ")

hash_md5 = hashlib.md5(password.encode()).hexdigest()

print("Hash MD5:", hash_md5)