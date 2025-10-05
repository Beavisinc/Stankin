def fit_the_key(text, key):
    text_len = len(text)
    key_len = len(key)
    if text_len == key_len:
        return key
    elif text_len > key_len:
        repeats = text_len // key_len
        reminder = text_len % key_len
        return key * repeats + key[:reminder]
    else:
        return key[:text_len]


def EncryptDecrypt(text, key, operation):
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cypher = ''
    key_index = 0
    #key_len = len(key)
    
    if operation == 'ш':
        operation = 'encrypt'
    elif operation == 'д':
        operation = 'decrypt'
    
    for char in text:
        if char in alphabet:
            text_number = alphabet.index(char)
            key_number = alphabet.index(key[key_index])
            if operation == 'encrypt':
                cipher_number = (text_number + key_number) % len(alphabet)
            elif operation == 'decrypt':
                cipher_number = (text_number - key_number) % len(alphabet)
            cypher += alphabet[cipher_number]
            key_index += 1
    
    return cypher

key = input('Введите секретный ключ -> ')
ciphertext = input('Введите текст для шифрования / дешифрирования -> ')
key = fit_the_key(ciphertext, key).lower()
operation = input('Укажите необходимо шифрование (ш) или дешифрирование (д) -> ')

if operation == 'ш':
    encrypted_message = EncryptDecrypt(ciphertext, key, operation)
    print(f'Зашифрованное сообщение -> {encrypted_message}') 
elif operation == 'д':
    decrypted_message = EncryptDecrypt(ciphertext, key, operation)
    print(f'Дешифрированное сообщение -> {decrypted_message}') 









