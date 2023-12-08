import math
import hashlib
import struct

def leftrotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md5(message):
    r = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
         5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
         4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
         6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
    
    k = [math.floor(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476

    message = bytearray(message, 'utf-8')
    ancienne_taille = len(message) * 8  # En bits
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    message += ancienne_taille.to_bytes(8, byteorder='little')

    # Traitement par blocs de 512 bits
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        a, b, c, d = h0, h1, h2, h3
        # Conversion du bloc en une liste de 16 mots de 32 bits
        w = [0] * 16
        for j in range(0, 64, 4):
            word = block[j:j+4]
            w[j//4] = int.from_bytes(word, byteorder='little')

        for j in range(64):
            if 0 <= j <= 15:
                f = (b & c) | ((~b) & d)
                g = j
            elif 16 <= j <= 31:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif 32 <= j <= 47:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            elif 48 <= j <= 63:
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            aa, bb, cc, dd = a, b, c,d
            
            temp = d
            d = c
            c = b
            b = (leftrotate((a + f + k[j] + w[g]), r[j]) + b) & 0xFFFFFFFF
            a = temp
            if j >= 0 and j < 20:
                print(f"Iteration {j}: a={a}, b={b}, c={c}, d={d}")
                print(f"Pseudo-code:   a={aa}, b={bb}, c={cc}, d={dd}")
                print()

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF

    digest = h0.to_bytes(4, byteorder='little') + \
             h1.to_bytes(4, byteorder='little') + \
             h2.to_bytes(4, byteorder='little') + \
             h3.to_bytes(4, byteorder='little')

    return digest

message = "Hello World"
expected_result = hashlib.md5(message.encode()).hexdigest()

result = md5(message).hex()
print("Résultat calculé:", result)

print("Résultat attendu:", expected_result)

if result.lower() == expected_result.lower():
    print("Le résultat est correct.")
else:
    print("Le résultat est incorrect.")


