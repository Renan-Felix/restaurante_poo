from modelos.avaliacao import Avaliacao
class Restaurante:
    '''Representa a classe restaurante com suas caracteristicas'''
    restaurantes = []

    def __init__(self, nome, categoria):
        '''Inicializa uma instância de restaurante
        Paramêtros:
        - nome(str): O nome do restaurante
        - categoria(str): a categoria do restaurante        
        '''
        # o ".title" serve para deixar a primeira letra de cada palavra em letra maiuscula
        self._nome = nome.title()
        # o ".upper" deixa a palavra toda em maiuscula
        self._categoria = categoria.upper()
        # o "_" torna o atributo privado, que o usuario não altere o valor dele. Ele protege o atributo.
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        '''Retorna o valor em string do restaurante'''
        return f'{self._nome} | {self._categoria}'
    
    # Criando um método nosso, o "classmethod" serve para indicar que o método criado é um método da classe. Não precisou instanciar um objeto.
    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma representação formatada de todos os restaurantes'''
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}')

    # O decorator property ele pega o atributo e muda a forma de como ele vai ser lido.
    @property
    def ativo(self):
        '''Retorna um símbolo indicando o estado de atividade do restaurante'''
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        '''Alterna o estado do restaurante'''
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        '''Registra uma avaliação do restaurante
        - cliente (str): o nome do cliente que fez a avaliação
        - nota (float): a nota atribuida ao restaurente de 1 a 5)
        '''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Registra a media de avaliações do restaurante e retorna o valor'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media






