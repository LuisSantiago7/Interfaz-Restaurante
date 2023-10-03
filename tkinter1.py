from tkinter import *
import random, datetime
from tkinter import filedialog, messagebox

price_food = [2.5, 20.5, 20.5, 2.5, 2.5, 2.5, 3, 15, 15]
price_drink = [10, 11, 30, 50, 32, 3, 5, 4, 3]
price_desserts = [6, 5, 3, 4,7, 3, 10, 5, 3]

#operador
operator = ''
def press_operator(number):
    global operator
    operator = operator + number
    viewfinder_calculator.delete(0, END)
    viewfinder_calculator.insert(END, operator)

#borrar
def delete_calculator():
    global operator
    operator = ''
    viewfinder_calculator.delete(0, END)
    
#Resultado Calculadora
def reslut_calculator():
    global operator
    result = str(eval(operator))
    viewfinder_calculator.delete(0, END)
    viewfinder_calculator.insert(0,  result)
    operator = ''

#Revisar check
def review_check():
    f = 0
    for food in cuadros_food:
        if list_var_food[f].get() == 1:
            cuadros_food[f].config(state=NORMAL)
            if cuadros_food[f].get()=='0':
                cuadros_food[f].delete(0, END)
            cuadros_food[f].focus()
        else:
            cuadros_food[f].config(state=DISABLED)
            text_food[f].set('0')
        f+=1
    
    dr = 0
    for drink in cuadros_drink:
        if list_var_drink[dr].get()==1:
            cuadros_drink[dr].config(state=NORMAL)
            if cuadros_drink[dr].get()== '0':
                cuadros_drink[dr].delete(0,END)
            cuadros_drink[dr].focus()
        else:
            cuadros_drink[dr].config(state=DISABLED)
            text_drink[dr].set('0')
        dr+=1
        
    dess = 0
    for dessert in cuadro_desserts:
        if list_var_desserts[dess].get() == 1:
            cuadro_desserts[dess].config(state=NORMAL)
            if cuadro_desserts[dess].get()=='0':
                cuadro_desserts[dess].delete(0,END)
            cuadro_desserts[dess].focus()
        else:
            cuadro_desserts[dess].config(state=DISABLED)
            text_desserts[dess].set('0')
        dess+=1
        
def total():
    #subtotales de categoria
    sub_total_food = 0
    sub_total_drink = 0
    sub_total_desserts= 0
    
    #calculo de subtotal comida
    p_f = 0
    for cant in text_food:
        sub_total_food = sub_total_food + (float(cant.get()) * price_food[p_f])
        p_f+=1    
    
    #calculo de subtotal bebidas
    p_d = 0
    for cant in text_drink:
        sub_total_drink = sub_total_drink + (float(cant.get()) * price_drink[p_d])
        p_d+=1    
        
    #calculo de subtotal postres
    p_dr = 0
    for cant in text_desserts:
        sub_total_desserts = sub_total_desserts + (float(cant.get()) * price_desserts[p_dr])
        p_dr+=1    
        
    subtotal = sub_total_food + sub_total_drink + sub_total_desserts
    iva = subtotal * 0.16
    total = subtotal+iva
    
    var_cost_food.set(f'${round(sub_total_food, 2)} USD')
    var_cost_drink.set(f'${round(sub_total_drink, 2)} USD')
    var_cost_desserts.set(f'${round(sub_total_desserts, 2)} USD')
    var_subtotal.set(f'${round(subtotal,2)} USD')
    var_iva.set(f'${round(iva,2)} USD')
    var_total.set(f'${round(total,2)} USD')
    
    
#Recibo
def receipt():
    text_receipt.delete(1.0, END)
    num_receipt = f'N#-{random.randint(23456723, 98765432)}'
    date_today = datetime.datetime.now()
    date_receipt = f'{date_today.day}/{date_today.month}/{date_today.year} - {date_today.hour}:{date_today.minute}:{date_today.second}'
    text_receipt.insert(END, f'Datos: \t{num_receipt}\t {date_receipt}\n')   
    text_receipt.insert(END, f'-'*75+'\n') 
    text_receipt.insert(END, 'Items\t\tCant.\t     Costo Items\n')
    text_receipt.insert(END, f'-'*75+'\n') 
    
    x=0
    for food in text_food:
        if food.get() != '0':
            text_receipt.insert(END, f'{list_food[x]}\t\t {food.get()}\t     $ {int(food.get()) * price_food[x]}\n')
        x+=1    
        
    x_drink = 0
    for drink in text_drink:
        if drink.get() != '0':
            text_receipt.insert(END, f'{list_drink[x_drink]}\t\t {drink.get()}\t    $ {int(drink.get()) * price_drink[x_drink]}\n')
        x_drink+=1
        
    x_dess = 0
    for dess in text_desserts:
        if dess.get() !='0':
            text_receipt.insert(END, f'{list_desserts[x_dess]}\t\t {dess.get()}\t    $ {int(dess.get()) * price_desserts[x_dess]} \n')
        x_dess+=1
        
    
    
    text_receipt.insert(END, f'-'*75+'\n') 
    text_receipt.insert(END, f'Costo de la Comida:\t\t{var_cost_food.get()}\n')
    text_receipt.insert(END, f'Costo de la Bebidas:\t\t{var_cost_drink.get()}\n')
    text_receipt.insert(END, f'Costo de la Postres:\t\t{var_cost_desserts.get()}\n')
    text_receipt.insert(END, f'-'*75+'\n') 
    text_receipt.insert(END, f'Sub-Total: {var_subtotal.get()}\n')
    text_receipt.insert(END, f'IVA: {var_iva.get()}\n')
    text_receipt.insert(END, f'TOTAL = {var_total.get()}')
        

def save():
    receipt_save = text_receipt.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt')
    archivo.write(receipt_save)
    archivo.close()
    messagebox.showinfo('Notificacion', 'Archivo guardado correctamente')
    
    


def clear():
    text_receipt.delete(1.0, END)
    for text in text_food:
        text.set('0')
    for text in text_drink:
        text.set('0')
    for text in text_desserts:
        text.set('0')
    
    for cuadro in cuadros_food:
        cuadro.config(state =DISABLED)
    for cuadro in cuadros_drink:
        cuadro.config(state =DISABLED)
    for cuadro in cuadro_desserts:
        cuadro.config(state =DISABLED)
        
    for v in list_var_food:
        v.set(0)
    for v in list_var_drink:
        v.set(0)
    for v in list_var_desserts:
        v.set(0)
        
    var_cost_food.set('')
    var_cost_drink.set('')
    var_cost_desserts.set('')
    var_subtotal.set('')
    var_iva.set('')
    var_total.set('')
        
#CONFIGURAR LA VENTANA DE TKINTER

#iniciar TKAINTER
app = Tk()

#tamaño de la ventana con app.geometry, que tiene como parametros el ancho y alto + posicion en eje de x + posicion en eje de y
app.geometry('1020x630+420+225')

#en este proyecto tendremos un diseño muy especifico, es por eso que vamos a bloquear el maximizar la ventana, lo hacemos con el metodo app.resizable() que tiene como parametros los pixelees modficables en eje x y eje y 
app.resizable(False, False)

#cambiar el titulo de la ventana
app.title('Sistema Facturacion')

#color de fondo
app.config(bg= 'salmon')


'''AGREGAR PANELES A LA VENTANA'''


#Panel SUPERIOR, lo creamos con una instancia de tkinter.Frame() cuyos parametros sera: su ubicacion (en este caso dentro de la ventana 'app'), el grosor de la linea y su textura
top_panel = Frame(app, 
                  bd=1, 
                  relief='flat')
#agregamos su ubicacion dentro de la ventana
top_panel.pack(side='top')

#Si lo ejecutamos asi, no nos mostrara nada... bueno, si, pero sera un pixel en blanco, ya que no le hemos ingresado nada
label_title = Label(top_panel, 
                    text= 'Sistema de Facturación', 
                    fg= 'grey', 
                    font=('Dosis', 47), 
                    bg= 'salmon', 
                    width= 27)
label_title.grid(row=0, 
                 column=0)


#panel IZQUIERDO
left_panel = Frame(app, 
                   bd=1, 
                   relief='flat')
left_panel.pack(side='left')


    #Panel COSTOS
costs = Frame(left_panel, 
              bd= 1, 
              relief= 'flat',
              bg = 'azure4',
              padx = 66)
costs.pack(side='bottom')

    #Panel MENUS
panel_menu_food = LabelFrame(left_panel, 
                             text='COMIDA',
                             font=('Dosis', 19, 'bold'),
                             bg='salmon', 
                             bd=1, 
                             relief='flat', 
                             fg='grey')
panel_menu_food.pack(side='left')

panel_menu_drink = LabelFrame(left_panel, 
                              text='BEBIDAS',
                              font=('Dosis', 19, 'bold'),
                              bg='salmon', 
                              bd=1, 
                              relief='flat', 
                              fg='grey')
panel_menu_drink.pack(side='left')

panel_menu_desserts = LabelFrame(left_panel, 
                                 text='Postres',
                                 font=('Dosis', 19, 'bold'),
                                 bg='salmon', bd=1, 
                                 relief='flat', 
                                 fg='grey')
panel_menu_desserts.pack(side='left')


#panel DERECHO
right_panel = Frame(app, bd=1, 
                    relief='flat')
right_panel.pack(side='right')

    #panel BOTONES
buttoms_panel = Frame(right_panel, 
                     bd=1, 
                     relief='flat') 
buttoms_panel.pack(side='bottom')

    #Panel RECIBOS
receipt_panel = Frame(right_panel, 
                      bd=1, 
                      relief='flat') 
receipt_panel.pack(side='bottom')

    #panel Calculadora
calculator_panel = Frame(right_panel, 
                         bd=1, 
                         relief='flat') 
calculator_panel.pack(side='bottom')


#lista de productos
list_food = ['Rib Eye', 'Tomahak', 'Cawboy', 'Picaña', 'NewYork', 'Sirloin', 'T-bone', 'Entrecot', 'Salmon']
list_drink = ['Paloma', 'Mojito', 'Vino', 'Blue Label', 'Jose Cuervo', 'Corona', 'Heineken', 'Indio', 'Victoria']
list_desserts = ['Pastel Chocolate', 'Moffin', 'Yogurth Griego', 'Carlota', 'Late', 'brownies', 'helado', 'Pastel Bruce', 'Musse']

#generar intem comida
list_var_food = []
cuadros_food = []
text_food = []
count_food = 0
for food in list_food:
    #chechbutton
    list_var_food.append('')
    list_var_food[count_food] = IntVar()
    food = Checkbutton(panel_menu_food, 
                       text = food.title(), 
                       bg= 'salmon',
                       font=('Dosis', 18, 'bold'), 
                       onvalue= 1, 
                       offvalue=0, 
                       variable=list_var_food[count_food],
                       command=review_check)
    food.grid(row= count_food,
              column= 0 , 
              sticky=W)
    
    #cuadros de entrada
    cuadros_food.append('')
    text_food.append('')
    text_food[count_food] = StringVar()
    text_food[count_food].set(0)
    cuadros_food[count_food] = Entry(panel_menu_food, 
                                     font=('Dosis', 14, 'bold'),
                                     bd=1, 
                                     width= 3,
                                     state= DISABLED,
                                     textvariable=text_food[count_food])
    cuadros_food[count_food].grid(row = count_food, column = 1)
    count_food+=1


#generar item Bebidas
list_var_drink = []
cuadros_drink = []
text_drink = []
count_drink = 0
for drink in list_drink:
    list_var_drink.append('')
    list_var_drink[count_drink] = IntVar()
    drink = Checkbutton(panel_menu_drink, 
                        text= drink.title(), 
                        bg= 'salmon', 
                        font=('Dosis', 18, 'bold'),
                        onvalue=1, 
                        offvalue=0, 
                        variable= list_var_drink[count_drink],
                        command=review_check)
    drink.grid(row= count_drink,
               column=0, 
               sticky=W)
    
    #cuadros de entrada
    cuadros_drink.append('')
    text_drink.append('')
    text_drink[count_drink] = StringVar()
    text_drink[count_drink].set(0)
    cuadros_drink[count_drink] = Entry(panel_menu_drink,
                                    font=('Dosis', 14, 'bold'),
                                    bd=1, 
                                    width= 3,
                                    state= DISABLED,
                                    textvariable= text_drink[count_drink])
    cuadros_drink[count_drink].grid(row = count_drink, column = 1,)
    count_drink +=1
    

#generar items postres
list_var_desserts = []
cuadro_desserts = []
text_desserts = []
count_desserts = 0
for dess in list_desserts:
    list_var_desserts.append('')
    list_var_desserts[count_desserts] = IntVar()
    dess = Checkbutton(panel_menu_desserts,
                       text= dess.title(), 
                       bg= 'salmon', 
                       font=('Dosis', 18, 'bold'),
                       onvalue=1, 
                       offvalue=0, 
                       variable=list_var_desserts[count_desserts],
                       command=review_check)
    dess.grid(row=count_desserts, 
              column=0, 
              sticky=W)
    
    #cuadros de entrada
    cuadro_desserts.append('')
    text_desserts.append('')
    text_desserts[count_desserts] = StringVar()
    text_desserts[count_desserts].set(0)
    cuadro_desserts[count_desserts] = Entry(panel_menu_desserts,
                                    font=('Dosis', 14, 'bold'),
                                    bd=1, 
                                    width= 3,
                                    state= DISABLED,
                                    textvariable= text_desserts[count_desserts])
    cuadro_desserts[count_desserts].grid(row = count_desserts, column =1)

    count_desserts +=1




'''ETIQUETAS DE COSTOS Y PANEL DE ENTRADA'''
   #variables
var_cost_food = StringVar()
var_cost_drink = StringVar()
var_cost_desserts = StringVar()
var_subtotal = StringVar()
var_iva = StringVar()
var_total = StringVar()

#Costos Comida
label_cost_food = Label(costs, 
                        text= 'Costos Comida',
                        font=('Dosis', 12, 'bold'),
                        bg = 'azure4',
                        fg= 'white')
label_cost_food.grid(row=0, column=0)

text_cost_food = Entry(costs,
                       font=('Dosis', 12, 'bold'),
                       bd=1, 
                       width=10,
                       state= 'readonly',
                       textvariable= var_cost_food)

text_cost_food.grid(row=0, column=1 , padx = 35)

#costos BEBIDAS
label_cost_drink = Label(costs,
                        text= 'Costos Bebidas',
                        font=('Dosis', 12, 'bold'),
                        bg = 'azure4',
                        fg= 'white')
label_cost_drink.grid(row=1, column=0)

text_cost_drink = Entry(costs, 
                       font=('Dosis', 12, 'bold'),
                       bd=1, 
                       width=10,
                       state= 'readonly',
                       textvariable= var_cost_drink)
text_cost_drink.grid(row = 1, column=1, padx = 35)

                        
#costos Postres
label_cost_desserts = Label(costs,
                        text= 'Costos Postres',
                        font=('Dosis', 12, 'bold'),
                        bg = 'azure4',
                        fg= 'white')
label_cost_desserts.grid(row=2, column=0)
text_cost_desserts = Entry(costs,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable= var_cost_desserts)
text_cost_desserts.grid(row=2, column=1, padx = 35)

#SubTotal
label_subtotal = Label(costs,
                       text='Subtotal',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg= 'white')
label_subtotal.grid(row=0, column=2)
text_subtotal = Entry(costs,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable= var_subtotal)
text_subtotal.grid(row=0, column=3, padx = 35)

#IVA
label_iva = Label(costs,
                  text='IVA',
                  font=('Dosis', 12, 'bold'),
                  bg='azure4',
                  fg = 'white')
label_iva.grid(row=1, column=2)
text_iva = Entry(costs,
                 bd=1,
                 font=('Dosis', 12, 'bold'),
                 width=10,
                 state='readonly',
                 textvariable= var_iva)
text_iva.grid(row= 1, column=3, padx = 35)

#TOTAL
label_total = Label(costs,
                    text='TOTAL',
                    font=('Dosis', 12, 'bold'),
                    bg='azure4',
                    fg='white')
label_total.grid(row=2, column=2)
text_total = Entry(costs,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width= 10,
                   state='readonly',
                   textvariable= var_total)
text_total.grid(row= 2, column=3, padx = 35)



#botones
list_buttons = ['TOTAL', 'Recibo', 'Guardar', 'Resetear']
buttons_create = []

columnas = 0
for button in list_buttons:
    button = Button(buttoms_panel,
                    text= button.title(),
                    font=('Dosis', 11, 'bold'),
                    fg = 'white',
                    bg = 'azure4',
                    bd =1,
                    width=9)
    buttons_create.append(button)
    
    button.grid(row = 0, column = columnas)
    columnas+=1
    
buttons_create[0].config(command=total)
buttons_create[1].config(command = receipt)
buttons_create[2].config(command= save)
buttons_create[3].config(command = clear)

    
#Recibo
text_receipt = Text(receipt_panel,
                    font=('Dosis', 12, 'bold'),
                    bd = 1,
                    width= 42,
                    height=10)
text_receipt.grid(row=0, column=0)

#calculadora 
viewfinder_calculator = Entry(calculator_panel,
                            font=('Dosis', 16, 'bold'),
                            width=48,
                            bd=1)
viewfinder_calculator.grid(row=0, column=0, columnspan=46)

#Botones
list_buttons_calculator= ['7','8', '9','+', '4', '5', '6','-', '1', '2', '3','x', '=', '0', 'C', '/']
list_new_buttns = []

var_row = 1
var_column = 0

for button in list_buttons_calculator:
    button = Button(calculator_panel,
                   text= button.title(),
                   font=('Dosis', 12, 'bold'),
                   fg = 'white',
                   bg = 'azure4',
                   bd = 1,
                   width=8)
    list_new_buttns.append(button)
    button.grid(row = var_row, column= var_column)
    
    if var_column == 3:
        var_row += 1
    
    var_column += 1
    if var_column ==4:
        var_column = 0

list_new_buttns[0].config(command = lambda: press_operator('7'))
list_new_buttns[1].config(command = lambda: press_operator('8'))
list_new_buttns[2].config(command = lambda: press_operator('9'))
list_new_buttns[3].config(command = lambda: press_operator('+'))
list_new_buttns[4].config(command = lambda: press_operator('4'))
list_new_buttns[5].config(command = lambda: press_operator('5'))
list_new_buttns[6].config(command = lambda: press_operator('6'))
list_new_buttns[7].config(command = lambda: press_operator('-'))
list_new_buttns[8].config(command = lambda: press_operator('1'))
list_new_buttns[9].config(command = lambda: press_operator('2'))
list_new_buttns[10].config(command = lambda: press_operator('3'))
list_new_buttns[11].config(command = lambda: press_operator('*'))
list_new_buttns[12].config(command = reslut_calculator)
list_new_buttns[13].config(command = lambda: press_operator('0'))
list_new_buttns[14].config(command = delete_calculator)
list_new_buttns[15].config(command = lambda: press_operator('/'))

#evita que la pantalla se cierre
app.mainloop()
