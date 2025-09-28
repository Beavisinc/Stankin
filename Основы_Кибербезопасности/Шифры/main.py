import subprocess as sp

while True:
    cypher_option = input('Выберите шифр: Cesar(C) / XOR(X) / Vijinere(V) -> ').lower()
    
    if cypher_option in ('c', 'cesar', 'ц', 'цезаря'):
        sp.run(['python', 'cesar.py'])
        break
    elif cypher_option in ('xor', 'x'):
        sp.run(['python', 'XOR.py'])
        break
    elif cypher_option in ('v', 'vijinere', 'вижинера', 'в'):
        sp.run(['python', 'Vijenere.py'])
        break
    else:
        print('Такого шифра не существует, укажите шифр заново')
