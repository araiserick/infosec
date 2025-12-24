import sys
import base64
if len(sys.argv) != 3:
    print("Ошибка: необходимо указать ровно два параметра.")
    sys.exit(1)
mode = sys.argv[1]
text = sys.argv[2]
if mode == "crypt":
    print("Encrypting...")
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    print(encoded_bytes.decode("utf-8"))
elif mode == "decrypt":
    print("Decrypting...")
    decoded_bytes = base64.b64decode(text.encode("utf-8"))
    print(decoded_bytes.decode("utf-8"))
else:
    print("Ошибка: неизвестный режим. Используйте 'crypt' или 'decrypt'.")
    sys.exit(1)
