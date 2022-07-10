import tkinter as tk
from page_home import PageHome
from page_login import PageLogin
from page_logged import PageLogged
from page_signin import PageSignin
from page_users import PageUsers


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args,  **kwargs)
        self.geometry("380x530")
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PageHome, PageLogin, PageSignin, PageUsers):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageHome")

    def show_frame(self, page_name, update=False):
        '''Show a frame for the given page name'''
        self.frames[page_name].update_content()
        self.frames[page_name].tkraise()

    def show_auth_frame(self, part_logado):
        '''Authorized frame, gets removed when changing pages'''
        frame = PageLogged(parent=self.container, controller=self,
                           auth_part=part_logado)
        frame.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
