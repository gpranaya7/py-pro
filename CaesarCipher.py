
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(msg,shift):
    emsg=''
    for Letter in msg:
        if Letter in alphabet:
            emsg+=alphabet[(alphabet.index(Letter)+shift )% len(alphabet)]
        else:
            emsg+=Letter
    return emsg

def decrypt(msg,shift):
    decryptedtext = ''
    for ch in msg:
        if ch in alphabet :
            decryptedtext += alphabet[alphabet.index(ch) - shift]
        else:
            decryptedtext+=ch
    return decryptedtext

cont='yes'
while cont!='no':
    choice = input('select encode ,decode or decrypt')
    msg = input('type ur msg:')
    shift = int(input('enter the shift number:'))
    def caesar(choice):
        if choice=='encode':
            print(encrypt(msg,shift))
        else :
            print(decrypt(msg ,shift))
    caesar(choice)
    cont = input('if you want to continue type yes')



