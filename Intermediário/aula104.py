# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores sao usados para fazer o Python
# usar as funções decoradoras em outras funções
# Decoradores são 'Syntax suggar' (Açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        resultado += ' Qualquer coisa'
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao # faz com que a função seja executada junto
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')

# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')  
invertida = inverte_string('123')
print(invertida)