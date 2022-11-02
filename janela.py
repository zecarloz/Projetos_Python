from tkinter import *
from tkinter import Tk, ttk
# cores =========================================
co0 = "#f0f3f5"  # preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra

# criando janelas=================================
janela = Tk()
janela.title('')
janela.geometry('310x310')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# dividindo a janela
frame_cima = Frame(janela, width=310, height=50, bg=co1,relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co1,relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configurando o frame cima==========================
l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
# posiciona label
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275 ,anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

# Configurando o frame baixo
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid' )
# posiciona Entry
e_nome.place(x=14, y=50)



janela.mainloop()

