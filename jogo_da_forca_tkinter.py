from tkinter import *
from random import choice
# configuraçãoes da janela:
root = Tk()
root.geometry('550x297')
root.title('Jogo da Forca')
root.config(bg='#f7b736')
root.resizable(width=False, height=False)

# variáveis do jogo da forca:
palavras = ['helicoptero', 'medico', 'engenheiro', 'igreja', 'ratoeira'
            , 'constitucionamento', 'joalheria', 'triceratops', 'filosofia',
            'fonoaudiologo', 'programacao', 'cassino', 'matematica', 'brasil', 'nigeria',
            'cavalo', 'pato', 'debugar', 'ewerton', 'isaac', 'raquel', 'minutos', 
            'astronauta', 'sistemas', 'analise', 'principe', 'rainha']
nome = choice(palavras)
underlines = ('_ '*len(nome)).split()
tentativas = 6
acertos = ''

# Funções de inserir e atualizar labels:
def update_tela(oculto):
    label_dinamica.set(oculto)


def insert_letra(opc):
    global nome
    global underlines
    global acertos
    global label_t
    global tentativas
    global root
    for posicao, letra in enumerate(nome):
        if opc == letra:
            underlines[posicao] = opc
            acertos+= opc
        posicao += 1
    if not acertos:
        tentativas -=1
        label_resultado.set(f'{opc.upper()} não estava na palavra!')
    else:
        label_resultado.set(f'{opc.upper()} estava na palavra!')

    if nome == ''.join(underlines):
        label_resultado.set(f'Parabéns! Você ganhou com {tentativas} restantes!')
    if tentativas == 0:
        label_resultado.set('Zerou as tentativas! Você perdeu!')   
    elif tentativas == -1:
        root.destroy()      

    acertos = ''
    update_tela(''.join(underlines))
    label_t.set(tentativas)
  
    

# labels de texto fixo e variável
label_resultado = StringVar()
label_t = StringVar()
label_dinamica = StringVar()
label_word = Label(root, textvariable=label_dinamica, width=20, height=2, padx=8, justify=CENTER,anchor='center', bg='#fcfffd', fg='#101211', relief='flat', font='Ivy 16')
label_word.place(y=125, x=150)
label_ta = Label(root,textvariable=label_t, width=2, height=1, bg='#fcfffd', fg='#302759', relief='flat', font='Ivy 16 bold')
label_ta.place(x=520, y=0)
label_title = Label(root, text='JOGO DA FORCA', width=18, height=2, padx=6, justify=CENTER,anchor='center', bg='#f7b736', fg='#302759', relief='flat', font='Ivy 18 bold')
label_title.place(y=50, x=138)
label_attempts = Label(root, text='TENTATIVAS:', width=10, height=1, bg='#fcfffd', fg='#302759', relief='flat', font='Ivy 15 bold', padx=10)
label_attempts.place(x=378, y=0)
label_resultado2 = Label(root, textvariable=label_resultado, width=30, height=1, bg='#f7b736', fg='#101211',relief=FLAT, font='Ivy 8 bold', padx=8,anchor='w')
label_resultado2.place(x=150, y=181)
# tela inicial
update_tela(''.join(underlines))
label_t.set(tentativas)

## 26 botões:
Bq = Button(root, text='q',command=lambda: insert_letra('q'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bq.place(x=78, y=200)
Bw = Button(root, text='w',command=lambda: insert_letra('w'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bw.place(x=117, y=200)
Be = Button(root, text='e',command=lambda: insert_letra('e'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Be.place(x=156, y=200)
Br = Button(root, text='r',command=lambda: insert_letra('r'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Br.place(x=195, y=200)
Bt = Button(root, text='t',command=lambda: insert_letra('t'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bt.place(x=234, y=200)
By = Button(root, text='y',command=lambda: insert_letra('y'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
By.place(x=273, y=200)
Bu = Button(root, text='u',command=lambda: insert_letra('u'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bu.place(x=312, y=200)
Bi = Button(root, text='i',command=lambda: insert_letra('i'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bi.place(x=351, y=200)
Bo = Button(root, text='o',command=lambda: insert_letra('o'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bo.place(x=390, y=200)
Bp = Button(root, text='p',command=lambda: insert_letra('p'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bp.place(x=429, y=200)
#row2
Ba = Button(root, text='a',command=lambda: insert_letra('a'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Ba.place(x=79, y=232)
Bs = Button(root, text='s',command=lambda: insert_letra('s'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bs.place(x=118, y=232)
Bd = Button(root, text='d',command=lambda: insert_letra('d'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bd.place(x=157, y=232)
Bf = Button(root, text='f',command=lambda: insert_letra('f'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bf.place(x=196, y=232)
Bg = Button(root, text='g',command=lambda: insert_letra('g'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bg.place(x=235, y=232)
Bh = Button(root, text='h',command=lambda: insert_letra('h'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bh.place(x=274, y=232)
Bj = Button(root, text='j',command=lambda: insert_letra('j'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bj.place(x=313, y=232)
Bk = Button(root, text='k',command=lambda: insert_letra('k'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bk.place(x=352, y=232)
Bl = Button(root, text='l',command=lambda: insert_letra('l'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bl.place(x=391, y=232)
Bç = Button(root, text='ç',command=lambda: insert_letra('ç'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bç.place(x=430, y=232)
#row3
Bz = Button(root, text='z',command=lambda: insert_letra('z'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bz.place(x=119, y=264)
Bx = Button(root, text='x',command=lambda: insert_letra('x'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bx.place(x=158, y=264)
Bc = Button(root, text='c',command=lambda: insert_letra('c'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bc.place(x=197, y=264)
Bv = Button(root, text='v',command=lambda: insert_letra('v'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bv.place(x=236, y=264)
Bb = Button(root, text='b',command=lambda: insert_letra('b'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bb.place(x=275, y=264)
Bn = Button(root, text='n',command=lambda: insert_letra('n'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bn.place(x=314, y=264)
Bm = Button(root, text='m',command=lambda: insert_letra('m'),  width=3, height=1, relief=RAISED, overrelief=SUNKEN, font= 'Ivy 12 bold')
Bm.place(x=353, y=264)
root.mainloop()
