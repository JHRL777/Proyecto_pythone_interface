from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox
operador = ''
pre_comida = [20.000,10.000,15.000,12.000,14.000,35.000,27.000,19.000,17.000,18.000,11.000,16.000,17.000]
pre_bebias = [1.500,3.500,1.800,2.000,3.500,3.000,700,4.000,3.800,1.800,5.000,2.300,5.500]
pre_postres = [10.500,30.500,10.800,20.000,30.500,30.000,7.000,40.000,30.800,10.800,50.000,20.300,50.500]
def click_boto(numero):
    global operador
    operador = operador + numero
    visor_calcular.delete(0,END)
    visor_calcular.insert(END,operador)


def borrar():
    global operador
    operador = ''
    visor_calcular.delete(0,END)

def ob_resutado():
    global operador
    resultado = str(eval(operador))
    visor_calcular.delete(0, END)
    visor_calcular.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadro_comida:
        if variable_comida[x].get() ==1:
            cuadro_comida[x].config(state=NORMAL)
            if cuadro_comida[x].get() =='0':
                cuadro_comida[x].delete(0,END)
            cuadro_comida[x].focus()
        else:
            cuadro_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x +=1

    x = 0
    for c in cuadro_bebidas:
        if variable_bebida[x].get() == 1:
            cuadro_bebidas[x].config(state=NORMAL)
            if cuadro_bebidas[x].get() == '0':
                cuadro_bebidas[x].delete(0, END)
            cuadro_bebidas[x].focus()
        else:
            cuadro_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1

    x = 0
    for c in cuadro_postres:
        if variable_postres[x].get() == 1:
            cuadro_postres[x].config(state=NORMAL)
            if cuadro_postres[x].get() == '0':
                cuadro_postres[x].delete(0, END)
            cuadro_postres[x].focus()
        else:
            cuadro_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def funcion_total():
    sub_total_comida = 0
    indice = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida +(float(cantidad.get()) *pre_comida[indice])
        indice +=1


    sub_total_bebida = 0
    indice = 0
    for cantidad in texto_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * pre_bebias[indice])
        indice += 1


    sub_total_postres = 0
    indice = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * pre_postres[indice])
        indice += 1



    sub_total = sub_total_comida + sub_total_bebida +sub_total_postres
    impuesto  = sub_total *0.19
    total = sub_total + impuesto

    var_costo_comida.set(f'$ {round(sub_total_comida,2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuesto, 2)}')
    var_total.set(f'$ {round(total, 2)}')

def recibo():
    textto_recibo.delete(1.0,END)
    numero_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}: {fecha.minute}'
    textto_recibo.insert(END,f'Datos:\n{numero_recibo}\n{fecha_recibo}\n')
    textto_recibo.insert(END,f'*'*70+'\n')
    textto_recibo.insert(END, f'Items\t\t\tCant.\tCosto Items\n')
    textto_recibo.insert(END,f'-'*70+'\n')

    x=0
    for comida in texto_comida:
        if comida.get() !='0':
            textto_recibo.insert(END,f'{lista_comida[x]}\t\t\t{comida.get()}\t$ {int(comida.get())*pre_comida[x]}\n')
            x +=1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            textto_recibo.insert(END, f'{lista_bebidas[x]}\t\t\t{bebida.get()}\t$ {int(bebida.get()) * pre_bebias[x]}\n')
            x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            textto_recibo.insert(END, f'{lista_postres[x]}\t\t\t{postres.get()}\t$ {int(postres.get()) * pre_postres[x]}\n')
            x += 1


    textto_recibo.insert(END,f'-'*70+'\n')
    textto_recibo.insert(END, f'Costo de la comida:  \t{var_costo_comida.get()}\n')
    textto_recibo.insert(END, f'Costo de la Bebidas:  \t{var_costo_bebida.get()}\n')
    textto_recibo.insert(END, f'Costo de la postres:  \t{var_costo_postres.get()}\n')

    textto_recibo.insert(END, f'-' * 70 + '\n')
    textto_recibo.insert(END, f'Costo de la comida:  \t{var_subtotal.get()}\n')
    textto_recibo.insert(END, f'Costo de la Bebidas:  \t{var_impuesto.get()}\n\n')
    textto_recibo.insert(END, f'Costo total:  \t\t{var_total.get()}\n')
    textto_recibo.insert(END, f'*' * 70 + '\n')
    textto_recibo.insert(END, f'Gracias')

def guardar():
    info_recibo = textto_recibo.get(1.0, END)
    archivo  = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion','su recibo a sido guardado')
def resetear():
    textto_recibo.delete(0.1,END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postres:
        cuadro.config(state=DISABLED)

    for v in variable_comida:
        v.set(0)
    for v in variable_bebida:
        v.set(0)
    for v in variable_postres:
        v.set(0)

    var_costo_bebida.set('')
    var_costo_comida.set('')
    var_costo_postres.set('')
    var_total.set('')
    var_subtotal.set('')
    var_impuesto.set('')

#inicar tkiner

aplicacion = Tk()


#Tamaño de la ventana

aplicacion.geometry('1020x720+0+0')

#evitar maximisar
aplicacion.resizable(0,0)

#titulo de la ventana
aplicacion.title("Mi restaurante - Sistema de facturacion")

#color de fondo
aplicacion.config(bg='burlywood')

#panel superior

panel_superior = Frame(aplicacion, bd=1,relief=FLAT)
panel_superior.pack(side=TOP)
#CONTENIDO PANEL SUPERIOS
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturacion", fg='azure4',
                        font=('Dosis',58),bg='burlywood', width=20)
etiqueta_titulo.grid(row=0,column=0)

#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1,relief=FLAT, bg ='azure4',padx=100)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida',font=('Dosis',18,'bold'),
                           bd=1,relief=FLAT,fg='azure4')

panel_comidas.pack(side=LEFT)

#panel BEBIDAS
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas',font=('Dosis',18,'bold'),
                           bd=1,relief=FLAT,fg='azure4')

panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres',font=('Dosis',18,'bold'),
                           bd=1,relief=FLAT,fg='azure4')

panel_postres.pack(side=LEFT)

#panel derecha
panel_derecha = Frame(aplicacion, bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel CALCULADORA
panel_calculadora = Frame(panel_derecha, bd=1,relief=FLAT,bg='burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd=1,relief=FLAT,bg='burlywood')
panel_recibo .pack()

#panel botones
panel_botones = Frame(panel_derecha, bd=1,relief=FLAT,bg='burlywood')
panel_botones .pack()

#lista de producot
lista_comida = ['pollo','cerdo','salmon','carne de res','pizza','hamburgueza','salchipapa','chorizo','pan','empanadas','burritos','tacos','seviche']
lista_bebidas = ['agua','soda','coca-cola','pepsi','jugo de naranga','te','bretaña','creveza poker','cerveza aguila','cerveza corona','vino','agua','avena']
lista_postres = ['Postre de chocolate','banna esplit','malteada de chocolate','helados','torta de queso','Frutas','flan','postre de limon','bocadillo','gelatina','flan','ensalda de frutas','brownie']




#generar items comida
variable_comida = []
cuadro_comida = []
texto_comida = []

contardor = 0
# crear un loop con un check botoon
for comida in lista_comida:

    #crer checkbutton
    variable_comida.append('')
    variable_comida[contardor] = IntVar()
    comida = Checkbutton(panel_comidas,text=comida.title(),
                         font=('Dosis',10),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_comida[contardor],
                         command=revisar_check)
    comida.grid(row=contardor,
                column=0,
                sticky=W)


    #cuadro de entrada
    cuadro_comida.append('')
    texto_comida.append('')
    texto_comida[contardor] = StringVar()
    texto_comida[contardor].set('0')
    cuadro_comida[contardor] = Entry(panel_comidas,
                                     font=('Dosis',10),
                                     width=6,
                                     bd=1,
                                     state=DISABLED,
                                     textvariable=texto_comida[contardor])
    cuadro_comida[contardor].grid(row=contardor,
                                  column=1)
    contardor += 1

#generar items bebida
variable_bebida = []
cuadro_bebidas = []
texto_bebidas = []
contardorbebida = 0
# crear un loop con un check botoon

for bebida in lista_bebidas:
    variable_bebida.append('')
    variable_bebida[contardorbebida] = IntVar()
    bebida = Checkbutton(panel_bebidas,text=bebida.title(), font=('Dosis',10),
                         onvalue=1, offvalue=0, variable=variable_bebida[contardorbebida],command=revisar_check)
    bebida.grid(row=contardorbebida,column=0,sticky=W)

    # cuadro de entrada
    cuadro_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contardorbebida] = StringVar()
    texto_bebidas[contardorbebida].set('0')
    cuadro_bebidas[contardorbebida] = Entry(panel_bebidas,
                                     font=('Dosis', 10),
                                     width=6,
                                     bd=1,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[contardorbebida])
    cuadro_bebidas[contardorbebida].grid(row=contardorbebida,
                                  column=1)
    contardorbebida +=1

#generar items postres
variable_postres = []
cuadro_postres = []
texto_postres = []
contardorpostres = 0
# crear un loop con un check botoon

for comida in lista_postres:
    variable_postres.append('')
    variable_postres[contardorpostres] = IntVar()
    bebida = Checkbutton(panel_postres,text=comida.title(), font=('Dosis',10),
                         onvalue=1, offvalue=0, variable=variable_postres[contardorpostres],command=revisar_check)
    bebida.grid(row=contardorpostres,column=0,sticky=W)

    # cuadro de entrada
    cuadro_postres.append('')
    texto_postres.append('')
    texto_postres[contardorpostres] = StringVar()
    texto_postres[contardorpostres].set('0')
    cuadro_postres[contardorpostres] = Entry(panel_postres,
                                            font=('Dosis', 10),
                                            width=6,
                                            bd=1,
                                            state=DISABLED,
                                            textvariable=texto_postres[contardorpostres])
    cuadro_postres[contardorpostres].grid(row=contardorpostres,
                                         column=1)

    contardorpostres +=1

#variable
var_costo_comida = StringVar()

#etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis',10,'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0,
                           column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida
                           )
texto_costo_comida.grid(row=0,
                        column=1)



#variable
var_costo_comida = StringVar()

#etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis',10,'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0,
                           column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida
                           )
texto_costo_comida.grid(row=0,
                        column=1,padx=41)


#variable
var_costo_bebida = StringVar()

#etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo bebida',
                              font=('Dosis',10,'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_bebida.grid(row=1,
                           column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida
                           )
texto_costo_bebida.grid(row=1,
                        column=1,padx=41)



#variable
var_costo_postres = StringVar()

#etiquetas de costo y campos de entrada
etiqueta_costo_postres = Label(panel_costos,
                              text='Costo postres',
                              font=('Dosis',10,'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_postres.grid(row=2,
                           column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres
                           )
texto_costo_postres.grid(row=2,
                        column=1,padx=41)

#variable
var_subtotal = StringVar()

#etiquetas de costo y campos de entrada
etiqueta_costo_subtotal = Label(panel_costos,
                              text='Costo Subtotal',
                              font=('Dosis',10,'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_subtotal.grid(row=0,
                           column=2)

texto_costo_subtotal = Entry(panel_costos,
                           font=('Dosis', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal
                           )
texto_costo_subtotal.grid(row=0,
                        column=3,padx=41)


#variable
var_impuesto = StringVar()

#etiquetas de costo y campos de entrada
etiqueta_costo_Inpuestos = Label(panel_costos,
                              text='Costo Impuestos',
                              font=('Dosis',10,'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_Inpuestos.grid(row=1,
                           column=2)

texto_costo_Inpuestos = Entry(panel_costos,
                           font=('Dosis', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto
                           )
texto_costo_Inpuestos.grid(row=1,
                        column=3,padx=41)

#variable
var_total = StringVar()

#etiquetas de costo y campos de entrada
etiqueta_costo_Total = Label(panel_costos,
                              text='Total',
                              font=('Dosis',10,'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_Total.grid(row=2,
                           column=2)

texto_costo_Total = Entry(panel_costos,
                           font=('Dosis', 10, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total
                           )
texto_costo_Total.grid(row=2,
                        column=3,padx=41)


# botones
botones = ['total','recibo','guardar','resetear']
columnas = 0
botones_creado = []

for boton in botones:
    boton = Button(panel_botones,
                   font=('Dosis', 9, 'bold'),
                   text=boton.title(),
                   fg = 'white',
                   bd=1,
                   width=9,
                   bg='azure4'
                   )
    botones_creado.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas +=1

botones_creado[0].config(command=funcion_total)
botones_creado[1].config(command=recibo)
botones_creado[2].config(command=guardar)
botones_creado[3].config(command=resetear)

#area del recibo
textto_recibo = Text(panel_recibo,
                     font=('Dosis', 7, 'bold'),
                     bd=1,
                     width=100,
                     height=20
                     )
textto_recibo.grid(row=0,
                   column=0)

#calculadora
visor_calcular = Entry(panel_calculadora,
                       font=('Dosis', 16, 'bold'),
                       bd=1,
                       width=25,
                       )
visor_calcular.grid(row=0,
                    column=0,
                    columnspan=4)

#lista botones a caluclar
botones_calculadora = ['7','8','9','+',
                       '4','5','6','-',
                       '1','2','3','x',
                       '=','C','0','/']
fila =1
columma = 0
botone_gurdado = []

for b in botones_calculadora:
    b = Button(panel_calculadora,
               font=('Dosis', 16, 'bold'),
               text=b.title(),
               fg='white',
               bd=1,
               width=5,
               bg='azure4'
               )

    botone_gurdado.append(b)

    b.grid(row=fila,
           column = columma)
    if columma == 3:
        fila +=1

    columma +=1
    if columma ==4:
        columma =0

botone_gurdado[0].config(command=lambda :click_boto(('7')))
botone_gurdado[1].config(command=lambda :click_boto(('8')))
botone_gurdado[2].config(command=lambda :click_boto(('9')))
botone_gurdado[3].config(command=lambda :click_boto(('+')))
botone_gurdado[4].config(command=lambda :click_boto(('4')))
botone_gurdado[5].config(command=lambda :click_boto(('5')))
botone_gurdado[6].config(command=lambda :click_boto(('6')))
botone_gurdado[7].config(command=lambda :click_boto(('-')))
botone_gurdado[8].config(command=lambda :click_boto(('1')))
botone_gurdado[9].config(command=lambda :click_boto(('2')))
botone_gurdado[10].config(command=lambda :click_boto(('3')))
botone_gurdado[11].config(command=lambda :click_boto(('*')))
botone_gurdado[12].config(command=ob_resutado)
botone_gurdado[13].config(command=borrar)
botone_gurdado[14].config(command=lambda :click_boto(('0')))
botone_gurdado[15].config(command=lambda :click_boto(('/')))

#evitar que la pantalal se cierre

aplicacion.mainloop()