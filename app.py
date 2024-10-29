
from modelos.restaurante import Restaurante
'''Representa as instancias das classes e os métodos atribuidos'''

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_praca.receber_avaliacao('Gui',5)

restaurante_praca.receber_avaliacao('Renan', 3)

restaurante_praca.receber_avaliacao('Gustavo', 5)

restaurante_praca.alternar_estado()

def main():
    '''Lista os restaurante e suas formatações dentro da função main(principal)'''
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()