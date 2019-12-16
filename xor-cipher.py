def xor_cipher(str, key):
    encript_str = ""
    for letter in str:
        encript_str += chr(ord(letter) ^ key)
    return  encript_str    
 
def xor_uncipher(str, key):
    uncript_str = ''
    for letter in str:
        uncript_str += chr(ord(letter) ^ key)
    return uncript_str
 
strg = input('Введите строку для шифрования: ')
key  = int(input('Введите ключ шифрования: '))

print( 'Оригинальная строка:\t', strg )
incr_strg = xor_cipher(strg, key)
print('Зашифрованная строка по ключу ' + str(key) + ':\t', incr_strg)
uncr_strg = xor_uncipher(incr_strg,key)
print('Расшифрованная строка по ключу ' + str(key) + ':\t', uncr_strg)