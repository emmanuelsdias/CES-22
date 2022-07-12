class Transfer():
    def __init__(self, person_paying_name: str, person_paid_name: str, amount: float) -> None:
        self.person_paying = person_paying_name
        self.person_paid = person_paid_name
        self.amount = amount

    @staticmethod
    def get_fields():
        return {'person_paying': "Sender",
                'person_paid': "Recipient",
                'amount': "Amount"}