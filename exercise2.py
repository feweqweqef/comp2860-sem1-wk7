from exercise1 import ShiftCipher

def main():
    ciphertext = "GurPnrfnepvcurevfernyylrnflgboernx"

    for shift in range(26):
        cipher = ShiftCipher(shift)
        candidate = cipher.decrypt(ciphertext)
        print(shift, candidate)

if __name__ == "__main__":
    main()
