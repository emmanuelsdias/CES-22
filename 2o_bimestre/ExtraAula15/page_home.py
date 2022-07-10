import tkinter as tk
from page import Page


class PageHome(Page):
    page_path = "Menu"

    def __init__(self, parent, controller):
        super().__init__(parent, controller, PageHome.page_path)
        self.controller = controller

        # main content widgets
        text1 = tk.Label(self, text="Bem-vindo ao Leilão Virtual!")
        text1.pack()
        button1 = tk.Button(self,
                            width=30,
                            text="Logar",
                            command=lambda: controller.show_frame("PageLogin"))
        button1.pack(pady=(10, 0))
        button2 = tk.Button(self,
                            width=30,
                            text="Cadastrar",
                            command=lambda: controller.show_frame("PageSignin"))
        button2.pack(pady=(10, 0))
        button3 = tk.Button(self,
                            width=30,
                            text="Ver usuários",
                            command=lambda: controller.show_frame("PageUsers"))
        button3.pack(pady=(10, 0))
