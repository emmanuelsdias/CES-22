import tkinter as tk
from page import Page
from settings import lista_part, fields
from page_signin import PageSignin


class PageLogged(Page):
    page_path = "Menu > Meu perfil"

    def __init__(self, parent, controller, auth_part):
        super().__init__(parent, controller, PageLogged.page_path)
        self.controller = controller
        self.logged_part = auth_part

        # main content widgets
        hello_text = tk.Label(self, text="Bom dia, " +
                              self.logged_part.nome +
                              "!\nVocê entrou na sua conta =)")
        hello_text.pack()
        user_info_frame = tk.LabelFrame(
            self, width=340, height=270, text="Alterações do usuário")
        user_info_frame.pack(pady=(10, 0))
        user_info_frame.pack_propagate(0)
        self.entries = PageSignin.write_form(
            user_info_frame, fields, show_old_info=True, logged_part=self.logged_part)

        # action buttons widgets
        buttons_subframe = tk.Frame(user_info_frame)
        buttons_subframe.pack(pady=(10, 0))
        update_button = tk.Button(buttons_subframe,
                                  text='Alterar dados',
                                  command=lambda: [
                                      self.alterar_participante(),
                                      controller.show_auth_frame(
                                          lista_part[-1]),
                                      self.grid_forget()])
        update_button.pack(side=tk.LEFT, padx=5, pady=5)
        back_button = tk.Button(buttons_subframe,
                                text='Retornar para o menu',
                                command=lambda: [
                                    controller.show_frame("PageHome"),
                                    self.grid_forget()])
        back_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # delete frame
        delete_frame = tk.LabelFrame(
            self, width=340, height=110, text="Exclusão do usuário")
        delete_frame.pack(pady=(20, 0))
        delete_text = tk.Label(
            delete_frame, text="Deseja mesmo excluir sua conta?")
        delete_text.pack(pady=(10, 0))
        delete_frame.pack_propagate(0)
        delete_button = tk.Button(delete_frame,
                                  text='Excluir minha conta',
                                  command=lambda: [
                                      lista_part.remove(self.logged_part),
                                      controller.show_frame("PageHome"),
                                      self.grid_forget()])
        delete_button.pack(pady=(10, 0))

    def alterar_participante(self):
        lista_part.remove(self.logged_part)
        PageSignin.register_user(self.entries)
