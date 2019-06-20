#builtin methods ADD type float max ...etc

def main():

    #big=max('Helloworld','Hello','tiny')
    big=max('Helloworldz')
    small=min('helloworldz')


    print(big,small)


main()


def greet(lang):

    if lang == 'en':
        print('English')
    elif lang == 'es':
        print('Spanish')
    else:
        print('Hello')


greet('en')
greet('es')
greet('nn')
greet(9)


def wish():
    return "Hello"


print(wish(),'chakri')
