key = int(input('Введите секретный ключ (десятичное число) -> '))
ciphertext = input('Введите текст для шифрования / дешифрирования -> ')

codepoints = [ord(ch) for ch in ciphertext]

decoded_chars = [chr(cp ^ key) for cp in codepoints]

decoded_text = "".join(decoded_chars)
print(f'Зашифрованное / дешифрированное сообщение -> {decoded_text}') 