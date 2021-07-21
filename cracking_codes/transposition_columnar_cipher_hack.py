import detect_english
import transposition_columnar_cipher


def main():
    encrypted_text = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hacked_message = hack_transposition_columnar_cipher(encrypted_text)

    if hacked_message is None:
        print("Failed to hack encryption.")
    else:
        print()
        print("Hacked message:")
        print()
        print(hacked_message)
        print()


def hack_transposition_columnar_cipher(encrypted_text):
    print("Hacking...")

    # Brute-force by looping through every possible key.
    for key in range(1, len(encrypted_text)):
        print(f"Trying key #{key}")

        decrypted_text = transposition_columnar_cipher.decrypt_message(encrypted_text, key)

        if detect_english.is_english(decrypted_text):
            # Ask user if this is the correct decryption.
            print()
            print("Possible encryption hack:")
            print(f"Key #{key}: {decrypted_text[:100]}")
            print()
            print("Enter D if done, anything else to continue hacking:")
            response = input("> ")

            if response.strip().upper().startswith("D"):
                return decrypted_text

    return None


if __name__ == "__main__":
    main()
