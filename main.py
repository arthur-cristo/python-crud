from frontend import *
import backend as core


app = None


def view_command():
    rows = core.view()
    app.list_clients.delete(0, END)
    for r in rows:
        app.list_clients.insert(END, r)
        

def search_command():
    app.list_clients.delete(0, END)
    rows = core.search(
        app.txt_name.get(),
        app.txt_last_name.get(),
        app.txt_email.get(),
        app.txt_cpf.get())
    for r in rows:
        app.list_clients.insert(END, r)
    
    
def insert_command():
    core.insert(app.txt_name.get(), app.txt_last_name.get(), app.txt_email.get(), app.txt_cpf.get())
    view_command()
    
    
def update_command():
    core.update(selected[0], app.txt_name.get(), app.txt_last_name.get(), app.txt_email.get(), app.txt_cpf.get())
    view_command()

    
def del_command():
    id = selected[0]
    core.delete(id)
    view_command()
        

def getSelectedRow(event):
    global selected
    selected_index = app.list_clients.curselection()
    
    if selected_index:
        index = selected_index[0]
        selected = app.list_clients.get(index)
        app.ent_name.delete(0, END)
        app.ent_name.insert(END, selected[1])
        app.ent_last_name.delete(0, END)
        app.ent_last_name.insert(END, selected[2])
        app.ent_email.delete(0, END)
        app.ent_email.insert(END, selected[3])
        app.ent_cpf.delete(0, END)
        app.ent_cpf.insert(END, selected[4])

if __name__ == "__main__":
    app = Gui()
    app.list_clients.bind('<<ListboxSelect>>', getSelectedRow)
    app.btn_view_all.configure(command=view_command)
    app.btn_search.configure(command=search_command)
    app.btn_insert.configure(command=insert_command)
    app.btn_update.configure(command=update_command)
    app.btn_del.configure(command=del_command)
    app.window.mainloop()