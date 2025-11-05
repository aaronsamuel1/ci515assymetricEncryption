# rsa implementation

import math

# defining a function to perform RSA approach
def myRSA(p: int, q: int, message: int):

    # calculating n
    n = p * q
    print("n = ", n)

    # calculating phi
    phi = (p - 1) * (q - 1)
    print("phi = ", phi)

    # selecting public key, e
    for i in range(2, phi):
        if math.gcd(i, phi) == 1:
            e = i
            break
    print("e = ", e)

    # selecting private key, d
    j = 1
    while True:
        if (j * e) % phi == 1:
            d = j
            break
        j += 1
    print("d = ", d)

    # performing encryption
    ct = (message ** e) % n
    print(f"Encrypted message is {ct}")

    # performing decryption
    mes = (ct ** d) % n
    print(f"Decrypted message is {mes}")

if __name__ == "__main__":
    
    myRSA(3, 7, 18)