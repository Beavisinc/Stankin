def CaesarCipher(text, key, operation):
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cypher = ''

    if operation == 'д':
        key = -key

    for char in text:
        if char in alphabet:
            text_number = alphabet.index(char)
            cipher_number = (text_number + key) % len(alphabet)
            cypher += alphabet[cipher_number]
        else:
            cypher += char

    return cypher

text = input('Введите текст для шифрования / дешифрования -> ')
key = int(input('Введите ключ (число сдвига) -> '))
operation = input('Укажите необходимо шифрование (ш) или дешифрирование (д) -> ')

result = CaesarCipher(text, key, operation)

if operation == 'ш':
    print(f'Зашифрованный текст -> {result}')
elif operation == 'д':
    print(f'Дешифрованный текст -> {result}')
