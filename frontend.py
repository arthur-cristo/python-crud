from tkinter import *

class Gui():
  """Graphicak User Interface's Class"""
  # Variables
  x_pad = 5
  y_pad = 3
  width_entry = 30

  window = Tk()
  window.wm_title('PYSQL 1.0')
  txt_name = StringVar()
  txt_last_name = StringVar()
  txt_email = StringVar()
  txt_cpf = StringVar()
  # Labels
  lbl_name = Label(window, text = 'Name')
  lbl_last_name = Label(window, text = 'Last Name')
  lbl_email = Label(window, text = 'E-mail')
  lbl_cpf = Label(window, text = 'CPF')
  # Entrys
  ent_name = Entry(window, textvariable = txt_name, width = width_entry)
  ent_last_name = Entry(window, textvariable = txt_last_name, width = width_entry)
  ent_email = Entry(window, textvariable = txt_email, width = width_entry)
  ent_cpf = Entry(window, textvariable = txt_cpf, width = width_entry)

  list_clients = Listbox(window, width = 100)
  scroll_client = Scrollbar(window)
  # Buttons
  btn_view_all = Button(window, text = 'See all')
  btn_search = Button(window, text = 'Search')
  btn_insert = Button(window, text = 'Insert')
  btn_update = Button(window, text = 'Update')
  btn_del = Button(window, text = 'Delete')
  # Grid
  lbl_name.grid(row=0, column=0), ent_name.grid(row = 0, column = 1, padx = 50, pady = 50)
  lbl_last_name.grid(row=1, column=0), ent_last_name.grid(row = 1, column = 1)
  lbl_email.grid(row=2, column=0), ent_email.grid(row = 2, column = 1)
  lbl_cpf.grid(row=3, column=0), ent_cpf.grid(row = 3, column = 1)
  list_clients.grid(row = 0, column = 2, rowspan = 10)
  scroll_client.grid(row = 4, column = 6, rowspan = 10)
  btn_view_all.grid(row = 4, column = 0, columnspan = 2)
  btn_search.grid(row = 5, column = 0, columnspan = 2)
  btn_insert.grid(row = 6, column = 0, columnspan = 2)
  btn_update.grid(row = 7, column = 0, columnspan = 2)
  btn_del.grid(row = 8, column = 0, columnspan = 2)
  # Conect Scrollbar with Listbox
  list_clients.configure(yscrollcommand=scroll_client.set)
  scroll_client.configure(command=list_clients.yview)
  # Style (swag)
  for child in window.winfo_children():
    widget_class = child.__class__.__name__
    if widget_class == 'Button':
      child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
    elif widget_class == 'Listbox':
      child.grid_configure(sticky='NS', padx = 0, pady = 0)
    elif widget_class == 'Scrollbar':
      child.grid_configure(sticky='NS', padx = 0, pady = 0)
    else:
      child.grid_configure(sticky='N', padx = x_pad, pady = y_pad)
