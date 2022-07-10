import tkinter as tk
from page import Page
from settings import lista_part


class PageUsers(Page):
    page_path = "Menu > Usuários"

    def __init__(self, parent, controller):
        super().__init__(parent, controller, PageUsers.page_path)
        self.controller = controller

        # main content widgets
        list_users_frame = tk.LabelFrame(
            self, width=340, height=270, text="Usuários cadastrados")
        list_users_frame.pack(pady=(10, 0))
        list_users_frame.pack_propagate(0)

        self.list_users_subframe = tk.Frame(list_users_frame)
        self.list_users_subframe.pack(pady=(20, 0))
        self.update_content()

        # action buttons widgets
        buttons_subframe = tk.Frame(list_users_frame)
        buttons_subframe.pack(pady=(20, 0))
        button1 = tk.Button(buttons_subframe, text='Retornar para o menu',
                            command=lambda: controller.show_frame("PageHome"))
        button1.pack()

    def erase_old_users(self):
        for widget in self.list_users_subframe.winfo_children():
            widget.destroy()

    def write_curr_users(self):
        listbox = tk.Listbox(self.list_users_subframe, activestyle=tk.NONE)
        listbox.pack(side=tk.LEFT, padx=(15, 0))
        for part in lista_part:
            listbox.insert(tk.END, part.nome)
        scrollbar = tk.Scrollbar(
            self.list_users_subframe, width=15, orient="vertical")
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)

    def update_content(self):
        self.erase_old_users()
        self.write_curr_users()
