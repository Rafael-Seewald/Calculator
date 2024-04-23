from tkinter import *

# Configurado para adição, subtração, multiplicação, divisão e (potenciação usando duaz vezes o multiplicar)


# Configurar a janela do tk mais estilização do fundo, titulo, redimensionamento

root = Tk()
root.title('Calculator')
root.geometry('400x355')
root.resizable(width=False, height=False)
root.configure(background='#282828')


# Funções para ativar os botões (enter_values: para o botão selecionado aparecer no exibidor da calculadora)

all_values = ''


def enter_values(event):
    """
    -> Recebe dos botões o valor a ser exibido na telinha da calculadora
    :param event: the button' value
    :return:
    """
    global all_values
    all_values = all_values + str(event)
    text_value.set(all_values)


def calculate():
    global all_values
    try:
        outcome = eval(all_values)
        text_value.set(str(outcome))
        all_values = str(outcome)
    except ZeroDivisionError:
        text_value.set('0')
        all_values = '0'
    except SyntaxError:
        text_value.set('0')
        all_values = '0'


def clean_screen():
    global all_values
    all_values = ''
    text_value.set('0')


# Exibidor da calculadora que varia conforme botões pressionados e o resultado da conta

text_value = StringVar()

e = Entry(root, textvariable=text_value, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#889C9B',
          font=('futura', 25, 'bold'), justify=RIGHT)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)


# Desing dos botões da calculadora (Botões: de 1 a 9, 0, operadores)

one = Button(root, text='1', padx=40, pady=20, command=lambda: enter_values('1'), fg='#FFFFFF', bg='#BD2A2E',
             activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
one.grid(row=1, column=1)


two = Button(root, text='2', padx=40, pady=20, command=lambda: enter_values('2'), fg='#FFFFFF', bg='#BD2A2E',
             activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
two.grid(row=1, column=2)


three = Button(root, text='3', padx=40, pady=20, command=lambda: enter_values('3'), fg='#FFFFFF', bg='#BD2A2E',
               activeforeground='#B6B6B3',  activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
three.grid(row=1, column=3)


four = Button(root, text='4', padx=40, pady=20, command=lambda: enter_values('4'), fg='#FFFFFF', bg='#BD2A2E',
              activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
four.grid(row=2, column=1)


five = Button(root, text='5', padx=40, pady=20, command=lambda: enter_values('5'), fg='#FFFFFF', bg='#BD2A2E',
              activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
five.grid(row=2, column=2)


six = Button(root, text='6', padx=40, pady=20, command=lambda: enter_values('6'), fg='#FFFFFF', bg='#BD2A2E',
             activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
six.grid(row=2, column=3)


seven = Button(root, text='7', padx=40, pady=20, command=lambda: enter_values('7'), fg='#FFFFFF', bg='#BD2A2E',
               activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
seven.grid(row=3, column=1)

eight = Button(root, text='8', padx=40, pady=20, command=lambda: enter_values('8'), fg='#FFFFFF', bg='#BD2A2E',
               activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
eight.grid(row=3, column=2)


nine = Button(root, text='9', padx=40, pady=20, command=lambda: enter_values('9'), fg='#FFFFFF', bg='#BD2A2E',
              activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
nine.grid(row=3, column=3)


zero = Button(root, text='0', padx=90.5, pady=20, command=lambda: enter_values('0'), fg='#FFFFFF', bg='#BD2A2E',
              activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
zero.grid(row=4, column=1, columnspan=2)


clean = Button(root, text='C', padx=40, pady=20, command=clean_screen, fg='#FFFFFF', bg='#282828',
               activeforeground='#B6B6B3', activebackground='#191919', relief=FLAT, font=('futura', 12, 'bold'))
clean.grid(row=0, column=4)


result = Button(root, text='=', padx=40, pady=20, command=calculate, fg='#FFFFFF', bg='#BD2A2E',
                activeforeground='#B6B6B3', activebackground='#A01C20', relief=FLAT, font=('futura', 12, 'bold'))
result.grid(row=4, column=3)


divide = Button(root, text='÷', padx=41.4, pady=20, command=lambda: enter_values('/'), fg='#FFFFFF', bg='#3B3936',
                activeforeground='#B6B6B3', activebackground='#282828', relief=FLAT, font=('futura', 12, 'bold'))
divide.grid(row=3, column=4)


multiply = Button(root, text='x', padx=40.5, pady=20, command=lambda: enter_values('*'), fg='#FFFFFF', bg='#3B3936',
                  activeforeground='#B6B6B3', activebackground='#282828', relief=FLAT, font=('futura', 12, 'bold'))
multiply.grid(row=4, column=4)


subtract = Button(root, text='-', padx=42.6, pady=20, command=lambda: enter_values('-'), fg='#FFFFFF', bg='#3B3936',
                  activeforeground='#B6B6B3', activebackground='#282828', relief=FLAT, font=('futura', 12, 'bold'))
subtract.grid(row=1, column=4)


add = Button(root, text='+', padx=40.5, pady=20, command=lambda: enter_values('+'), fg='#FFFFFF', bg='#3B3936',
             activeforeground='#B6B6B3', activebackground='#282828', relief=FLAT, font=('futura', 12, 'bold'))
add.grid(row=2, column=4)


# Mantem a janela do tkinter funcionando

root.mainloop()
