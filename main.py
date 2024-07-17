# Importando as bibliotecas
from tkinter import *
import tkinter
from datetime import datetime
import pyglet

# Usando a fonte digital-7
pyglet.font.add_file('digital-7.ttf')

# Criando uma janela vazia com o tkinter
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1
cor = cor3

janela = Tk()
janela.title("")
janela.geometry('440x180')
janela.resizable(width=False, height=False)
janela.configure(background=fundo)

# Obtendo a hora, o dia da semana, o mês e o ano
tempo = datetime.now()

hora = tempo.strftime("%H:%M:%S")
dia_semana = tempo.strftime("%A")
dia = tempo.day
mes = tempo.strftime("%b")
ano = tempo.strftime("%Y")

# Criando um label para mostrar a hora
l1 = Label(janela, text="00:00:00", font=('digital-7 80'), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

# Criando um label para mostrar os outros valores
l2 = Label(janela, font=('digital-7 20'), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

# Passando o valor da hora para o label e executando a função
def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l2.config(text=dia_semana + "   " + str(dia) + "/" + str(mes) + "/" + (ano))
    
    # Tornando a função dinâmica
    l1.after(1000, relogio)

# Executando a função
relogio()

janela.mainloop()

# Projeto de estudo!
