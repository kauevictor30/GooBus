# *****************************************************************
# APRESENTAÇÃO DE TAINÁ E KAUÊ: DIAGRAMA DE CLASSE DO APP GOOBUS!!!
# *****************************************************************

class TelaInicial:
    def __init__(self, nome_app: str, logo: str):
        self.nome_app = nome_app
        self.logo = logo

    def tela_inicial(self) -> None:
        pass


class LoginCadastro:
    def __init__(self, nome: str, email: str, telefone: int, cep: int, senha: int):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__cep = cep
        self.__senha = senha

    def fazer_login(self) -> bool:
        pass

    def cadastrar(self) -> bool:
        pass


class MapaTempoReal:
    def __init__(self, icones: list, filtros: list, localizacao: str):
        self.icones = icones
        self.filtros = filtros
        self.__localizacao = localizacao

    def exibir_mapa(self) -> None:
        pass

    def aplicar_filtros(self) -> None:
        pass


class RotasItinerarios:
    def __init__(self, linhas: list, pontos: list, horarios: list):
        self.__linhas = linhas
        self.__pontos = pontos
        self.__horarios = horarios

    def listar_rotas(self) -> None:
        pass

    def exibir_detalhes_rotas(self) -> None:
        pass


class PrevisoesDeChegada:
    def __init__(self, ponto_parada: str, horarios_proximos: list):
        self.__ponto_parada = ponto_parada
        self.__horarios_proximos = horarios_proximos

    def verificar_previsao(self) -> None:
        pass


class NotificacoesAlertas:
    def __init__(self, atrasos: list, desvios: list, mensagens: list):
        self.__atrasos = atrasos
        self.__desvios = desvios
        self.__mensagens = mensagens

    def exibir_alertas(self) -> None:
        pass


class Favoritos:
    def __init__(self, paradas: list, rotas: list):
        self.__paradas = paradas
        self.__rotas = rotas

    def acessar_favoritos(self) -> None:
        pass

    def adicionar_favorito(self) -> None:
        pass

    def remover_favorito(self) -> None:
        pass


class Feedback:
    def __init__(self, sugestoes: str, denuncias: str, faq: list):
        self.__sugestoes = sugestoes
        self.__denuncias = denuncias
        self.__faq = faq

    def enviar_feedback(self) -> None:
        pass

    def acessar_faq(self) -> None:
        pass


class PerfilConfiguracoes:
    def __init__(self, notificacoes: bool, idioma: str, acessibilidade: bool, permissoes: list):
        self.notificacoes = notificacoes
        self.idioma = idioma
        self.acessibilidade = acessibilidade
        self.__permissoes = permissoes

    def editar_perfil(self) -> None:
        pass

    def alterar_configuracoes(self) -> None:
        pass


# ******************************
# OBRIGADO PELA OPORTUNIDADE!!!!
# ******************************