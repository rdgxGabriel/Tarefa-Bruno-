nome = []
cpf = []
senha = []

while True:
    escolha = int(input('''[1] IR PARA REGISTRO
[2] IR PARA LOGIN\n
Escolha uma Opção:'''))
        
    def registrar():
        while True:
            nome_reg = input(f'\033[mDigite seu nome: ')
            nome_no_space = nome_reg.replace(' ', '')
            if not nome_no_space.isalpha():
                print ('\033[0;31mERRO! Digite um nome valido\033[m')
            else:
                nome.append(nome_reg)
                break
        while True:
            senha_reg = input(f'\033[mDigite uma senha: ')
            if len(senha_reg) == 0:
                print ('\033[0;31mERRO! Digite uma senha válido\033[m')
            else:
                senha.append(senha_reg)
                break
        while True:
            try:
                cpf_reg = int(input(f'\033[mRegistre seu CPF: '))
            except ValueError:
               print ('\033[0;31mERRO! Digite um CPF valido\033[m')
            else:
                cpf.append(cpf_reg)
                break
     
    def leiaInt(msg):
        ok = False
        valor = 0
        while True:
            n = str(input(msg))
            if n.isnumeric():
                 valor = int(n)
                 ok = True
            else:
                print ('\033[0;31mERRO! Digite numeros inteiros validos\033[m')
            if ok:
                break
        return valor 
    n = leiaInt("Digite sua idade: ") 
    

        
    def login():
        senha_login = input('Informe sua senha: ')
        cpf_login = int(input('Informe seu CPF: '))
        if cpf_login in cpf and senha_login in senha:
            print('\033[0;31m\n\nERRO! já existe um cliente com esse CPF! Tente novamente.\n\33[m')
        else:
            print('\033[0;31m\n\nERRO! Usuario não encontrado, tente novamente ou crie uma conta.\n\033[m')
    if escolha == 1:
        registrar()
    if escolha == 2:
        login()





































def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print ('\033[0;31mERRO! Digite uma idade valida\033[m')
        if ok:
            break
    
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print ('\033[0;31mERRO! Digite um CPF valido\033[m')
        if ok:
            break

    while True:
            nome_reg = input(f'\033[mRegistre seu nome: ')
            nome_no_space = nome_reg.replace(' ', '')
            if not nome_no_space.isalpha():
                print(f'\033[31mESCREVA UM NOME VÁLIDO')
            else:
                nome.append(nome_reg)
                break
   

nome = []
n = leiaInt("digite sua idade: ")
print(n)
p= leiaInt("digite sua CPF: ")
print (p)