from functions import decrypt,num_to_text


print("Enter your private key for decryption:")
choice = "n"
while True:
    if choice == "n":
        print("Private key")
        N = int(input("     N:"))
        d = int(input("     d:"))
    elif choice != "y":
        print("Error")
    choice = str(input("Decrypt text[1] or decrypt a number[2] ?:"))
    if choice != "1" and choice != "2":
        print("Entry is incorrect\n\n\n")
        break
    message = str(input("\nEncrypted message:"))

    if choice == "1":
        message_list = decrypt(message, d, N)
        print("Decrypted number:", message_list)
        print("\n\nDecrypted Text:", num_to_text(message_list))
    elif choice == "2":
        print("Decrypted number:", decrypt(message, d, N))
    else:
        print("Entry is incorrect\n\n\n")
        break

    choice = str(input("Decrypt a another message (y/n) ?:")).lower()
    if choice == "n":
        break
    elif choice == "y":
        choice = str(input("Keep the same private key (y/n) ?:"))
    else:
        print("Entry is incorrect\n\n\n")
        break