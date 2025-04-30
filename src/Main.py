from QuadTree import QuadTree
from ctypes.wintypes import POINT
from Interval import Interval2D, Interval
import os



if __name__ == "__main__":

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def wait():
        input('\n\nPressione Enter para continuar...')
        clear()




    def montar_menu():
        opções = [
            'Buscar Nodo',
            'Inserir Nodo',
            'Buscar Quadrante',
            'Mostrar Pontos',
            'Limpar Árvore',
            'Sair         '
        ]

        lista_menu = '-' * 65 + '\n' + '|' + ' ' * 63 + '|'
        
        
        for i in range(len(opções)):
            if (i+1) % 2 == 0:
                
                lista_menu += f'{i+1} - {opções[i]}\t|\n|'

                lista_menu += ' ' *63 + '|'
            else:
                opções[i] += (' ') * (15-len(opções[i]))

                lista_menu += f'\n|\t{i+1} - {opções[i]}\t|\t'
        
        lista_menu += '\n'+ '-' * 65

        return lista_menu




    def set_key(func) -> POINT:
        x = input(f'\nQual a coordenada "X" do nodo que deseja {func}?\n\n')
        if x.isnumeric() == False:
            print('\nCoordenadas podem ser apenas números\n')
            wait()
            return None
        else:
            y = input(f'\nQual a coordenada "Y" do nodo que deseja {func}?\n\n')
        if y.isnumeric() == False:
            print('\nCoordenadas podem ser apenas números\n')
            wait()
            return None
        return POINT(int(x), int(y))


    def set_interval():
        
        x1 = input(f'\nQual a coordenada "X" de início do quadrante?\n')
        if x1.isnumeric() == False:
            print('\nCoordenadas podem ser apenas números\n')
            wait()
            return None
        x1 = int(x1)

        x2 = input(f'\nQual a coordenada "X" de fim do quadrante?\n')
        if x2.isnumeric() == False:
            print('\nCoordenadas podem ser apenas números\n')
            wait()
            return None
        x2 = int(x2)

        y1 = input(f'\nQual a coordenada "Y" de início do quadrante?\n')
        if y1.isnumeric() == False:
            print('\nCoordenadas podem ser apenas números\n')
            wait()
            return None
        y1 = int(y1)

        y2 = input(f'\nQual a coordenada "Y" de fim do quadrante?\n')
        if y2.isnumeric() == False:
            print('\nCoordenadas podem ser apenas números\n')
            wait()
            return None
        
        y2 = int(y2)

        ix = Interval(x1, x2)

        iy = Interval(y1, y2)

        return Interval2D(ix, iy)


    def set_value():
        v = input(f'\nQual o valor desejado?\n\n')
        if v.isnumeric() == False:
            print('\nValores podem ser apenas números\n')
            wait()
            return 0
        else:
            return int(v)




    def menu(ops):

        clear()

        print('\tEscolha uma opção digitando o número da opção desejada\n')

        print(ops+'\n')

        o = (input())

        if o.isnumeric() == False:
                
                print('\nDigite um número presente na lista\n')

                wait()

                return 0
        
        if 0 >= int(o) or int(o) > 14:
                
                print('\nDigite um número presente na lista\n')

                wait()

                return 0
        
        return int(o)


    def main():

        qt = QuadTree()
        qt.insert(1, 1, 1)
      
        clear()

        op_menu = 0

        lista_menu = montar_menu()


        while op_menu != 'out':

            while op_menu == 0:

                op_menu = menu(lista_menu)

            #Search

            while op_menu == 1:

                clear()

                if qt.is_empty() == False:

                    value = qt.search(set_key('buscar'))

                    if value == None:

                        print('\nNenhum nodo com essa chave foi encontrado.')

                    else:

                        clear()

                        print(f'\nO nodo da chave indicada tem valor {value}.')

                    wait()

                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            #Inserir

            while op_menu == 2:

                clear()

                p = set_key('inserir')

                qt.insert(p.x, p.y, set_value())

                op_menu = menu(lista_menu)

            #Buscar Quadrante

            while op_menu == 3:

                clear()

                if qt.is_empty() == False:

                    Interval_2D = set_interval()
                    
                    if Interval_2D != None:

                        print('') 

                        qt.query_2D(Interval_2D)

                        wait()

                    else:

                        print('Quadrante Invalido.')
                    
                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            #Lista Pontos

            while op_menu == 4:

                clear()

                if qt.is_empty() == False:

                    pointlist = qt.all_points()

                    print(pointlist)

                    wait()
                    
                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)

            #Limpar Árvore

            while op_menu == 5:

                clear()

                if qt.is_empty() == False:

                    qt.clear()

                    print('Árvore limpa com sucesso.')

                    wait()

                else:

                    print('A árvore está vazia.')

                    wait()

                op_menu = menu(lista_menu)


            while op_menu == 6:

                op_menu = 'out'

                clear()

                print('Execução Terminada')
    main()

    pass