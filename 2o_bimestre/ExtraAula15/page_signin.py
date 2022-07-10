import tkinter as tk
from page import Page
from participante import Participante
from settings import lista_part, fields


class PageSignin(Page):
    page_path = "Menu > Página de Cadastro"

    def __init__(self, parent, controller):
        super().__init__(parent, controller, PageSignin.page_path)
        self.controller = controller

        # main content widgets
        signin_frame = tk.LabelFrame(
            self, width=340, height=270, text="Cadastro de usuario")
        signin_frame.pack(pady=(10, 0))
        signin_frame.pack_propagate(0)
        entries = PageSignin.write_form(signin_frame, fields)

        # action buttons widgets
        buttons_subframe = tk.Frame(signin_frame)
        buttons_subframe.pack(pady=(10, 0))
        register_button = tk.Button(buttons_subframe,
                                    text='Cadastrar',
                                    command=(lambda e=entries: [
                                        PageSignin.register_user(e),
                                        controller.show_frame("PageHome")
                                    ]))
        register_button.pack(side=tk.LEFT, padx=5, pady=5)
        back_button = tk.Button(buttons_subframe,
                                text='Retornar para o menu',
                                command=lambda: [
                                    controller.show_frame("PageHome")
                                ])
        back_button.pack(side=tk.RIGHT, padx=5, pady=5)

    @ staticmethod
    def register_user(entries):
        p = Participante(entries['nome'].get(),
                         entries['login'].get(),
                         entries['senha'].get(),
                         entries['email'].get(),
                         entries['endereco'].get(),
                         entries['telefone'].get())
        lista_part.append(p)

    @staticmethod
    def write_form(root, fields, show_old_info=False, logged_part=None):
        entries = {}
        for key in fields:
            aux_frame = tk.Frame(root)
            aux_frame.pack(side=tk.TOP, pady=(10, 0))
            field_label = tk.Label(aux_frame,
                                   width=10,
                                   text=fields[key]+" : ",
                                   anchor='w')
            field_label.pack(side=tk.LEFT)
            field_input = tk.Entry(aux_frame,
                                   width=30)
            field_input.insert(0, "")
            if show_old_info:
                field_input.insert(0, logged_part.__dict__[key])
            field_input.pack(side=tk.RIGHT)
            entries[key] = field_input
        return entries
