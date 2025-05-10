# *****************************************************************
# APRESENTAÇÃO DE TAINÁ E KAUÊ: DIAGRAMA DE CLASSE DO APP GOOBUS!!!
# *****************************************************************

class tela_inicial:
    def __init__(self, nome_app, logo):
        self.nome_app = nome_app[str]
        self.logo = logo[str]

    def tels_inicial(self) -> None:
        pass

class login_cadastro:
    def __init__(self, nome, email, telefone, cep, senha):
        self.__nome[str]
        self.__email[str]
        self.__telefone[int]
        self.__cep[int]
        self.__senha[int]

    def fazer_login(self) -> bool:
        pass

    def cadastrar(self) -> bool:
        pass

class mapa_tempo_real:
    def __init__(self, icones, filtros, localisacao):
        self.icones[list]
        self.filtros[list]
        self.__localizacao[str]
        
    def exibir_mapa(self) -> None:
        pass

    def aplicar_filtros(self) -> None:
        pass

class rotasItinerarios:
    def __init__(self, linhas, pontos, horarios):
        self.__linhas[list]
        self.__pontos[list]
        self.__horarios[list]

    def listar_rotas(self) -> None:
        pass

    def exibir_detalhes_rotas(self) -> None:
        pass

class previsoes_de_chegada:
    def __init__(self, ponto_parada, horarios_proximos):
        self.__ponto_parada[str]
        self.__horarios_proximos[list]
        

    def verificar_previsao(self) -> None:
        pass

class notificacoes_alertas:
    def __init__(self, atrasos, desvios, mensagens):
        self.__atrasos[list]
        self.__desvios[list]
        self.__mensagens[list]

    def exibir_alertas(self) -> None:
        pass

class favoritos:
    def __init__(self, paradas, rotas):
        self.__paradas[list]
        self.__rotas[list]

    def acessar_favoritos(self) -> None:
        pass

    def adicionar_favorito(self) -> None:
        pass

    def remover_favorito(self) -> None:
        pass

class feedback:
    def __init__(self, sugestoes, denuncias, faq):
        self.__sugestoes[str]
        self.__denuncias[str]
        self.__faq[list]

    def enviar_feedback(self) -> None:
        pass

    def acessar_faq(self) -> None:
        pass

class perfol_configurações:
    def __init__(self, notificações, idioma, acessibilidade, permissoes):
        self.notificacoes[bool]
        self.idioma[str]
        self.acessibilidade[bool]
        self.__permissoes[list]

    def editar_perfil(self) -> None:
        pass

    def alterar_configuracoes(self) -> None:
        pass

# ******************************
# OBRIGADO PELA OPORTUNIDADE!!!!
# ******************************