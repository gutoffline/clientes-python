# View - o que vai para o usuário
def formulario_login():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("Informe sua senha: ")
    usuario_completo = [usuario_digitado, senha_digitado]
    return usuario_completo
    
def exibir_mensagem(texto):
    print("\n\n")
    print("============================")
    print(texto)
    print("============================")
    print("\n\n")


