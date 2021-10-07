import requests

def buscar_avatar( usuario ):

    """
    Busca o avatar de um usuário no GitHub

    :param usuario: str com o nome do usuário
    :return: str com o link do avatar

    zazibr
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)


    return resp.json() ['avatar_url']




print( buscar_avatar('patrickdatabsb') )

