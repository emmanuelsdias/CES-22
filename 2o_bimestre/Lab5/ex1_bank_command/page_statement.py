import tkinter as tk
from commands import *
from page import Page


class PageStatement(Page):
    page_path = "Menu > Bank statement"

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller, PageStatement.page_path)
        self.controller = controller
        self.statement_text = tk.StringVar()
        self.statement_text.set("")

        # main content widgets
        statement_frame = tk.LabelFrame(self, width=340, height=440, text=" Get your bank statement ! ")
        statement_frame.pack(pady=(10, 0))
        statement_frame.pack_propagate(0)

        # action buttons widgets
        buttons_subframe = tk.Frame(statement_frame)
        buttons_subframe.pack(pady=(10, 0))
        statement_button = tk.Button(buttons_subframe,
                                text='Generate bank statement',
                                command=lambda: self.statement_text.set(GetBankStatement(ReceiverGetBankStatement(), persons_list[0].name, 3).execute()))
        statement_button.pack(side=tk.TOP, padx=5, pady=(5,15))
        balance_value = tk.Label(buttons_subframe, textvariable=self.statement_text)
        balance_value.pack()
        back_button = tk.Button(statement_frame,
                                text='Back to menu',
                                command=lambda: controller.show_frame("PageHome"))
        back_button.pack(side=tk.BOTTOM, padx=5, pady=(15,15))

    def update_content(self) -> None:
        self.statement_text.set("")