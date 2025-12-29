import random

# Bilangan prima besar (modulo)
P = 208351617316091241234326746312124448251235562226470491514186331217050270460481

# Membuat polinomial dengan a0 = secret
def generate_polynomial(secret, k):
    coefficients = [secret]
    for _ in range(k - 1):
        coefficients.append(random.randint(1, P - 1))
    return coefficients

# Menghitung nilai f(x)
def evaluate_polynomial(coeffs, x):
    result = 0
    for i, coeff in enumerate(coeffs):
        result = (result + coeff * pow(x, i, P)) % P
    return result

# Membagi secret menjadi n shares
def split_secret(secret, k, n):
    poly = generate_polynomial(secret, k)
    shares = []
    for i in range(1, n + 1):
        shares.append((i, evaluate_polynomial(poly, i)))
    return shares

# Interpolasi Lagrange
def lagrange_interpolation(x, points):
    total = 0
    for i, (xi, yi) in enumerate(points):
        li = 1
        for j, (xj, _) in enumerate(points):
            if i != j:
                li *= (x - xj) * pow(xi - xj, -1, P)
                li %= P
        total = (total + yi * li) % P
    return total

# Rekonstruksi secret
def recover_secret(shares):
    return lagrange_interpolation(0, shares)

# ================= MAIN =================
secret = 123456789
k = 3
n = 5

shares = split_secret(secret, k, n)
print("Shares:")
for s in shares:
    print(s)

recovered = recover_secret(shares[:k])
print("\nRecovered Secret:", recovered)