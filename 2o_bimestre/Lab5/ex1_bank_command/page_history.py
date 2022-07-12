import tkinter as tk
from page import Page
from settings import commands_list


class PageHistory(Page):
    page_path = "Menu > Commands history"

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller, PageHistory.page_path)
        self.controller = controller
        self.history_text = tk.StringVar()

        # main content widgets
        history_frame = tk.LabelFrame(self, width=340, height=440, text=" Check your commands history ! ")
        history_frame.pack(pady=(10, 0))
        history_frame.pack_propagate(0)

        # action buttons widgets
        buttons_subframe = tk.Frame(history_frame)
        buttons_subframe.pack(pady=(10, 0))
        history_list = tk.Label(buttons_subframe, textvariable=self.history_text)
        history_list.pack()
        back_button = tk.Button(history_frame,
                                text='Back to menu',
                                command=lambda: controller.show_frame("PageHome"))
        back_button.pack(side=tk.BOTTOM, padx=5, pady=(15,15))

    def update_content(self) -> None:
        for c in commands_list:
            self.history_text.set(self.history_text.get() + c + "\n")