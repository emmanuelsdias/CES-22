import tkinter as tk
from page import Page
from commands import *

class PageBalance(Page):
    page_path = "Menu > My balance"

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller, PageBalance.page_path)
        self.controller = controller
        self.balance_text = tk.StringVar()
        self.balance_text.set("Your balance:")

        # main content widgets
        balance_frame = tk.LabelFrame(self, width=340, height=160, text=" Check your balance ! ")
        balance_frame.pack(pady=(10, 0))
        balance_frame.pack_propagate(0)

        # action buttons widgets
        buttons_subframe = tk.Frame(balance_frame)
        buttons_subframe.pack(pady=(10, 0))
        balance_button = tk.Button(buttons_subframe,
                                text='Show my Balance',
                                command=lambda: self.balance_text.set(GetBalance(persons_list[0].name).execute()))
        balance_button.pack(side=tk.TOP, padx=5, pady=(5,15))
        balance_value = tk.Label(buttons_subframe, textvariable=self.balance_text)
        balance_value.pack()
        back_button = tk.Button(buttons_subframe,
                                text='Back to menu',
                                command=lambda: controller.show_frame("PageHome"))
        back_button.pack(side=tk.BOTTOM, padx=5, pady=(15,5))

    def update_content(self) -> None:
        self.balance_text.set("Your balance: ----------")



