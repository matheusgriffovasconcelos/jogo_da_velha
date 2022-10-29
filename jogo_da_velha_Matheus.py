import time
from tkinter import *
from tkinter import messagebox
import random

class Placar:
    def __init__(self):
        self.vitorias_x = 0
        self.vitorias_o = 0

    def inf_vitoria_x(self):
        self.vitorias_x += 1

    def inf_vitoria_o(self):
        self.vitorias_o += 1

    def obtem_placar(self):
        return self.vitorias_x, self.vitorias_o

    def obtem_vitorias_x(self):
        return self.vitorias_x

    def obtem_vitorias_o(self):
        return self.vitorias_o


matrizBtn = []
l_placar = []
placar = Placar()
matrizJogo = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
jogador = ['X']

def atualizaPlacar():
    contVitoriasX, contVitoriasO = placar.obtem_placar()
    l_placar[0]["text"] = "X: " + str(contVitoriasX) + " \t O: " + str(contVitoriasO)

def encontra_coluna_de_vitoria_iminente_do_O_na_linha(linha):
    cont_O = 0
    coluna_vazia = -1
    for c in range(3):
        if matrizJogo[linha][c] == 1:
            cont_O += 1
        elif matrizJogo[linha][c] == 0:
            coluna_vazia = c
    if cont_O == 2:
        return coluna_vazia
    else:
        return -1

def encontra_posicao_de_vitoria_iminente_do_O_em_linhas():
    for l in range(3):
        c = encontra_coluna_de_vitoria_iminente_do_O_na_linha(l)
        if c != -1:
            return l, c
    return -1, -1

def encontra_posicao_de_vitoria_iminente_do_O_em_colunas():
    return -1, -1
def encontra_posicao_de_vitoria_iminente_do_O_em_diagonais():
    return -1, -1

def posicao_de_vitoria_iminente_do_O():
    linha, coluna = encontra_posicao_de_vitoria_iminente_do_O_em_linhas()
    if linha == -1:
        linha, coluna = encontra_posicao_de_vitoria_iminente_do_O_em_colunas()
        if linha == -1:
            return encontra_posicao_de_vitoria_iminente_do_O_em_diagonais()
        else:
            return linha, coluna
    else:
        return linha, coluna
        
def encontra_coluna_de_vitoria_iminente_do_x_na_linha(linha):
    cont_x = 0
    coluna_vazia = -1
    for c in range(3):
        if matrizJogo[linha][c] == 1:
            cont_x += 1
        elif matrizJogo[linha][c] == 0:
            coluna_vazia = c
    if cont_x == 2:
        return coluna_vazia
    else:
        return -1

def encontra_posicao_de_vitoria_iminente_do_x_em_linhas():
    for l in range(3):
        c = encontra_coluna_de_vitoria_iminente_do_x_na_linha(l)
        if c != -1:
            return l, c
    return -1, -1

def encontra_linha_de_vitoria_iminente_do_x_na_coluna(coluna):
    cont_x = 0
    linha_vazia = -1
    for l in range(3):
        if matrizJogo[l][coluna] == 1:
            cont_x += 1
        elif matrizJogo[l][coluna] == 0:
            linha_vazia = l
    if cont_x == 2:
        return linha_vazia
    else:
        return -1

def encontra_posicao_de_vitoria_iminente_do_x_em_colunas():
    for c in range(3):
        l = encontra_linha_de_vitoria_iminente_do_x_na_coluna(c)
        if l != -1:
            return l, c
    return -1, -1

def encontra_vitoria_iminente_do_x_em_diagonais():
    cont_x = 0
    posicao_vazia_L = -1
    posicao_vazia_c = -1
    for i in range(3):
        if matrizJogo[i][i] == 0:
            posicao_vazia_L = i
            posicao_vazia_c = i
        if matrizJogo[i][i] == 1:
            cont_x +=1
    if cont_x == 2:
        return posicao_vazia_L, posicao_vazia_c

    for i in range(3):
        if matrizJogo[2-i][i] == 0:
            posicao_vazia_L = i
            posicao_vazia_c = i
        if matrizJogo[2-i][i] == 1:
            cont_x +=1
    if cont_x == 2:
        return posicao_vazia_L, posicao_vazia_c
           
def encontra_posicao_de_vitoria_iminente_do_x_em_diagonais():
    #for i in range(3):
       # for j in range(3):
            #linha = encontra_vitoria_iminente_do_x_em_diagonais(i)
            #coluna = encontra_vitoria_iminente_do_x_em_diagonais(j)
            #if linha != -1 and coluna != -1:
                #return linha, coluna
    return -1, -1


def posicao_de_vitoria_iminente_do_x():
    linha, coluna = encontra_posicao_de_vitoria_iminente_do_x_em_linhas()
    if linha == -1:
        linha, coluna = encontra_posicao_de_vitoria_iminente_do_x_em_colunas()
        if linha == -1:
            return encontra_posicao_de_vitoria_iminente_do_x_em_diagonais()
        else:
            return linha, coluna
    else:
        return linha, coluna




def executaJogadaAutomatica():
    if jogador[0] == 'X':
        return
    linha, coluna = posicao_de_vitoria_iminente_do_x()
    if linha == -1:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
    while matrizJogo[linha][coluna] != 0:
        if coluna < 2:
            coluna = coluna + 1
        else:
            coluna = 0
            linha = (linha + 1) % 3
    executaJogada(linha, coluna)

def reiniciaJogo():
    for i in range(3):
        for j in range(3):
            matrizJogo[i][j] = 0
    for i in range(3):
        for j in range(3):
            matrizBtn[i][j]["text"] = ""
    jogador[0] = "X"


def executaJogada(linha, coluna):
    if matrizJogo[linha][coluna] == 0:
        matrizBtn[linha][coluna]['text'] = jogador[0]
        if jogador[0] == 'X':
            matrizJogo[linha][coluna] = 1
            jogador[0] = 'O'
        elif jogador[0] == 'O':
            matrizJogo[linha][coluna] = 2
            jogador[0] = 'X'
        if verificaJogo() == 0:
            executaJogadaAutomatica()

def verificaLinha(linha):
    if matrizJogo[linha][0] == 0:
        return 0
    for i in range(3):
        if matrizJogo[linha][i] != matrizJogo[linha][0]:
            return 0
    return matrizJogo[linha][0]


def verificaColuna(coluna):
    if matrizJogo[0][coluna] == 0:
        return 0
    for i in range(3):
        if matrizJogo[i][coluna] != matrizJogo[0][coluna]:
            return 0
    return matrizJogo[0][coluna]


def verificaDiagonais():
    if matrizJogo[1][1] == 0:
        return 0
    if (matrizJogo[1][1] == matrizJogo[0][0] and matrizJogo[1][1] == matrizJogo[2][2]) or (
            matrizJogo[1][1] == matrizJogo[0][2] and matrizJogo[1][1] == matrizJogo[2][0]):
        return matrizJogo[1][1]
    else:
        return 0


def verificaJogo():
    resultadoDiagonais = verificaDiagonais()
    if resultadoDiagonais != 0:
        if resultadoDiagonais == 1:
            messagebox.showinfo(title="Resultado", message="X venceu")
            placar.inf_vitoria_x()
        else:
            messagebox.showinfo(title="Resultado", message="O venceu")
            placar.inf_vitoria_o()
        atualizaPlacar()
        reiniciaJogo()
        return 1
    else:
        for ind in range(3):
            resultadoLinha = verificaLinha(ind)
            resultadoColuna = verificaColuna(ind)
            if resultadoLinha != 0 or resultadoColuna != 0:
                vitorioso = ""
                if resultadoLinha != 0:
                    vitorioso = "X" if resultadoLinha == 1 else "O"
                else:
                    vitorioso = "X" if resultadoColuna == 1 else "O"
                if vitorioso == "X":
                    placar.inf_vitoria_x()
                else:
                    placar.inf_vitoria_o()
                mensagem = vitorioso + " venceu"
                messagebox.showinfo(title="Resultado", message=mensagem)
                atualizaPlacar()
                reiniciaJogo()
                return 1
        # verifica empate
        contZero = 0
        for l in range(3):
            for c in range(3):
                if matrizJogo[l][c] == 0:
                    contZero = contZero + 1
        if contZero == 0:
            messagebox.showinfo(title="Resultado", message="Deu Velha!")
            reiniciaJogo()
            return 1
        return 0

def executaJogada1():
    executaJogada(0, 0)


def executaJogada2():
    executaJogada(0, 1)


def executaJogada3():
    executaJogada(0, 2)


def executaJogada4():
    executaJogada(1, 0)


def executaJogada5():
    executaJogada(1, 1)


def executaJogada6():
    executaJogada(1, 2)


def executaJogada7():
    executaJogada(2, 0)


def executaJogada8():
    executaJogada(2, 1)


def executaJogada9():
    executaJogada(2, 2)


root = Tk()
root.title("JOGO DA VELHA")
# root.geometry('300x300')

btn1 = Button()
btn1["font"] = ("Arial", "16")
btn1["width"] = 10
btn1["height"] = 4
btn1['command'] = executaJogada1

btn2 = Button()
btn2["font"] = ("Arial", "16")
btn2["width"] = 10
btn2["height"] = 4
btn2['command'] = executaJogada2

btn3 = Button()
btn3["font"] = ("Arial", "16")
btn3["width"] = 10
btn3["height"] = 4
btn3['command'] = executaJogada3

btn4 = Button()
btn4["font"] = ("Arial", "16")
btn4["width"] = 10
btn4["height"] = 4
btn4['command'] = executaJogada4

btn5 = Button()
btn5["font"] = ("Arial", "16")
btn5["width"] = 10
btn5["height"] = 4
btn5['command'] = executaJogada5

btn6 = Button()
btn6["font"] = ("Arial", "16")
btn6["width"] = 10
btn6["height"] = 4
btn6['command'] = executaJogada6

btn7 = Button()
btn7["font"] = ("Arial", "16")
btn7["width"] = 10
btn7["height"] = 4
btn7['command'] = executaJogada7

btn8 = Button()
btn8["font"] = ("Arial", "16")
btn8["width"] = 10
btn8["height"] = 4
btn8['command'] = executaJogada8

btn9 = Button()
btn9["font"] = ("Arial", "16")
btn9["width"] = 10
btn9["height"] = 4
btn9['command'] = executaJogada9

labelPlacar = Label(text="X: 0 \t O: 0")
labelPlacar["font"] = ("Arial", "20")
labelPlacar["height"] = 2
labelPlacar["background"] = 'gray'
labelPlacar["foreground"] = 'black'

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
labelPlacar.grid(row=3, column=0, columnspan=3)

matrizBtn = [[btn1, btn2, btn3],
             [btn4, btn5, btn6],
             [btn7, btn8, btn9]]
l_placar = [labelPlacar]
atualizaPlacar()
root.mainloop()
