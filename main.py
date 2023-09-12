palavra = input("Digite a palavra que será verificada: ")

def checar_palindromo(pal):
    palavra_invertida = pal[::-1]
    if palavra_invertida == pal:
        return True

ehpalindromo = checar_palindromo(palavra)

if ehpalindromo is True:
    print( f'''
    Essa palavra é um palíndromo!
    
    Palavra: {palavra}
    Palavra ao contrário: {palavra[::-1]}
    
    ''')

elif ehpalindromo is not True:
    print( f'''
    Essa palavra não é um palíndromo!
    
    Palavra: {palavra}
    Palavra ao contrário: {palavra[::-1]}
    
    ''')