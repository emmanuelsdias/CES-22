import tkinter as tk
from page import Page


class PageHome(Page):
    page_path = "Menu"

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller, PageHome.page_path)
        self.controller = controller

        # main content widgets
        text1 = tk.Label(self, text="Welcome to POO Bank!")
        text1.pack()
        button1 = tk.Button(self,
                            width=30,
                            text="Go to my balance page",
                            command=lambda: controller.show_frame("PageBalance"))
        button1.pack(pady=(10, 0))
        button2 = tk.Button(self,
                            width=30,
                            text="Go to bank statement page",
                            command=lambda: controller.show_frame("PageStatement"))
        button2.pack(pady=(10, 0))
        button3 = tk.Button(self,
                            width=30,
                            text="Go to transfer money page",
                            command=lambda: controller.show_frame("PageTransfer"))
        button3.pack(pady=(10, 0))
        button4 = tk.Button(self,
                            width=30,
                            text="Go to command activity page",
                            command=lambda: controller.show_frame("PageHistory"))
        button4.pack(pady=(10, 0))
