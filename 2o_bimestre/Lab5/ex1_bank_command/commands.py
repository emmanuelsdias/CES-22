from __future__ import annotations
from abc import ABC, abstractmethod

from settings import persons_list, transfers_list, commands_list
from transfer import Transfer


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class GetBalance(Command):
    def __init__(self, person_name: str) -> None:
        self.person_name = person_name

    def execute(self) -> str:
        commands_list.append("Checked account balance")
        for p in persons_list:
            if p.name == self.person_name:
                balance = p.balance
        return f"Your balance: U$ {balance:.2f}"


class GetBankStatement(Command):
    def __init__(self, receiver: ReceiverGetBankStatement, person_name: str, how_many: int) -> None:
        self.receiver = receiver
        self.person_name = person_name
        self.how_many = how_many

    def execute(self) -> str:
        commands_list.append("Printed bank statement")
        return self.receiver.get_last_n_transfers(self.person_name, self.how_many)


class ReceiverGetBankStatement():
    def get_last_n_transfers(self, person: str, how_many: int) -> None:
        my_transfers = self.get_all_transfers(person)
        my_transfers = self.filter_last_transfers(my_transfers, how_many)
        return self.format_statement(my_transfers)

    def get_all_transfers(self, person: str) -> list:
        my_transfers = []
        for t in transfers_list:
            if t.person_paying == person or t.person_paid == person:
                my_transfers.append(t)
        return my_transfers
    
    def filter_last_transfers(self, my_transfers: list, how_many: int) -> list:
        return my_transfers[-how_many:]

    def format_statement(self, my_transfers: list) -> str:
        statement = ""
        for t in my_transfers:
            statement += f"{t.person_paying} paid {t.person_paid} U$ {float(t.amount):.2f}\n"
        return statement


class TransferMoney(Command):
    def __init__(self, person_paying: str, person_paid : str, amount: float) -> None:
        self.person_paying = person_paying
        self.person_paid = person_paid
        self.amount = amount

    def execute(self) -> None:
        commands_list.append("Transfered money")
        transfers_list.append(Transfer(self.person_paying, self.person_paid, self.amount))
        for p in persons_list:
            if p.name == self.person_paying:
                p.balance -= float(self.amount)
            if p.name == self.person_paid:
                print("entrou2")
                p.balance += float(self.amount)