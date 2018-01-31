import pickle

usuarios = {}

def save_data(data):
    with open("foo.pickle", "wb") as outfile:
        pickle.dump(data, outfile)

def load_data():
    try:
        with open("foo.pickle", "rb") as infile:
            return pickle.load(infile)
    except FileNotFoundError:
        return {}


def menu():
    global usuarios
    usuarios = load_data()
    
    while True:
        print("1. Adicionar usuário")
        print("2. Consultar usuário")
        print("3. Sair")
        option = input("Digite uma opção: ")

        if option == "1":
            adicionar_usuario()
        elif option == "2":
            consultar_usuario()
        elif option == "3":
            save_data(usuarios)
            break

def adicionar_usuario():
    nome = input("Nome: ")
    email = input("E-mail: ")
    usuarios[nome] = email

def consultar_usuario():
    nome = input("Nome: ")
    if nome in usuarios:
        email = usuarios[nome]
        print("E-mail: {}".format(email))
    else:
        print("Não achei")
        
if __name__ == "__main__":
    menu()
