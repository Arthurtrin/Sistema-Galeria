def usuarioehgerenciador(usuario):
    """
    Verifica se o usuário informado possui perfil de gerenciador.

    Parâmetros:
        usuario (User): Instância do usuário autenticado (objeto do modelo User do Django).

    Retorna:
        bool: True se o usuário for do tipo 'gerenciador', caso contrário False.
    """
    if usuario.perfil.tipo == 'gerenciador':
        return True
    else:
        return False
    
