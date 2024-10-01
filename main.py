from tkinter import *
import funcs as f

def get_icao(event):
    icao_code = icao_input.get().upper()

    if icao_code == 'Q':
        main.destroy()

    if len(icao_code) != 4:
        country_label.config(text='')
        airport_label.config(text='Check ICAO Code')
    else:
        result = f.search_icao(icao_code)
        if len(result) == 0:
            country_label.config(text='')
            airport_label.config(text='Airport not found')
        else:
            country_label.config(text=result[0])
            airport_label.config(text=result[1])

main = Tk()

# Basic Settings
main.title('ICAO Codes')
main.iconbitmap('icon.ico')
main.geometry('600x300')
main.resizable(0,0)
main.config(background='#d3d3d3')

# ICAO Code
# Test Button
btn = Button(main,text='Find',command= get_icao) 
btn.pack()

icao_label = Label(main, text='Enter ICAO Code', bg='#d3d3d3')
icao_label.pack(pady=(5,5))
icao_label.config(font=('verdana',12))
icao_input = Entry(main, width=10,justify='center')
icao_input.pack(pady=(0,10))
icao_input.config(font=('verdana', 24, 'bold'))
icao_input.focus_set()
main.bind("<Return>", get_icao)

# Airport Info
country_label = Label(main, text='',bg='#d3d3d3')
country_label.pack(pady=(10,10))
country_label.config(font=('verdana', 20))

airport_label = Label(main, text='',bg='#d3d3d3')
airport_label.pack(pady=(10,10))
airport_label.config(font=('verdana', 20))

main.mainloop()