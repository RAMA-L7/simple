value=input('enter the message: ')
#FOR ENCODING
morse_code = {' ':'_','A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
              'F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
              'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
              'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----'}
#FOR DECODING
alpha_code ={y:x for x,y in morse_code.items()}

print('1 - for ENCODING')
print('2 - for DECODING')
option = int(input('enter your option: '))
if option==1:
    string = value.upper()
    for element in range(0,len(string)):
        print(morse_code.get(string[element]),end=' ')
elif option==2:
    alpha_code ={y:x for x,y in morse_code.items()}
    code = value.split()
    for element in range(0,len(code)):
        print(alpha_code.get(code[element]),end='')
else:
    print('choose correct option')
