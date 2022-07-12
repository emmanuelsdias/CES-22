import tkinter as tk
from page import Page
from settings import fields
from commands import *


class PageTransfer(Page):
    page_path = "Menu > Transfer money"

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller, PageTransfer.page_path)
        self.controller = controller

        # main content widgets
        transfer_frame = tk.LabelFrame(self, width=340, height=180, text=" Transfer your money ! ")
        transfer_frame.pack(pady=(10, 0))
        transfer_frame.pack_propagate(0)
        entries = self.write_form(transfer_frame, fields)

        # action buttons widgets
        buttons_subframe = tk.Frame(transfer_frame)
        buttons_subframe.pack(pady=(10, 0))
        transfer_button = tk.Button(buttons_subframe,
                                 text='Transfer amount',
                                command=(lambda e=entries: [TransferMoney(entries['person_paying'].get(), entries['person_paid'].get(), entries['amount'].get()).execute(),
                                                            self.controller.show_frame("PageHome")]))
        transfer_button.pack(side=tk.LEFT, padx=5, pady=15)
        back_button = tk.Button(buttons_subframe,
                                text='Back to menu',
                                command=lambda: controller.show_frame("PageHome"))
        back_button.pack(side=tk.LEFT, padx=5, pady=15)

    def write_form(self, root, fields) -> None:
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
            if key == 'person_paying':
                field_input.insert(0, persons_list[0].name)
                field_input.config(state='readonly')
            field_input.pack(side=tk.RIGHT)
            entries[key] = field_input
        return entries
