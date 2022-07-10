import tkinter as tk
from page import Page
from settings import lista_part, fields
from page_signin import PageSignin


class PageLogin(Page):
    page_path = "Menu > Página de Login"

    def __init__(self, parent, controller):
        super().__init__(parent, controller, PageLogin.page_path)
        self.controller = controller

        # main content widgets
        login_frame = tk.LabelFrame(
            self, width=340, height=150, text="Login de usuario")
        login_frame.pack(pady=(10, 0))
        login_frame.pack_propagate(0)
        self.entries = PageSignin.write_form(
            login_frame, dict(list(fields.items())[1:3]))

        # action buttons widgets
        buttons_subframe = tk.Frame(login_frame)
        buttons_subframe.pack(pady=(10, 0))
        login_button = tk.Button(buttons_subframe,
                                 text='Login',
                                 command=lambda: self.login_participante())
        login_button.pack(side=tk.LEFT, padx=5, pady=5)
        back_button = tk.Button(buttons_subframe,
                                text='Retornar para o menu',
                                command=lambda: controller.show_frame("PageHome"))
        back_button.pack(side=tk.LEFT, padx=5, pady=5)

    def login_participante(self):
        login = self.entries['login'].get()
        senha = self.entries['senha'].get()
        for part in lista_part:
            if(part.authenticate_part(login, senha)):
                self.controller.show_auth_frame(part)
