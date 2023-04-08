from faker import Faker

person = Faker("pl_PL")

import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class BaseContact:
    def __init__(self, first_name, last_name, mail, private_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.private_phone = private_phone
        self.label_length = len(f"{self.first_name} {self.last_name}")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def contact(self):
        return f"Wybieram numer {self.private_phone} i dzwonię do {self.first_name} {self.last_name}"

    def label(self):
        return f"Długość etykiety dla {self.first_name} {self.last_name} -- {self.label_length}"


class BusinessContact(BaseContact):
    def __init__(self, firm, position, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.firm = firm
        self.position = position
        self.work_phone = work_phone

    def contact(self):
        return f"Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name}"


def create_contacts():
    choice = input(
        "Jaki rodzaj wizytówek wybierasz? :\n1 Base Contact\n2 Buisnes Contact\n"
    )
    if choice in ("1", "2"):
        try:
            how_many = int(input("Ile wygenerować ? "))
        except ValueError:
            logging.error("Nieprawidłowe dane!")
            exit(0)
        if choice == "1":
            base_contact_list = []
            for _ in range(how_many):
                base_contact_list.append(
                    BaseContact(
                        first_name=person.first_name(),
                        last_name=person.last_name(),
                        mail=person.email(),
                        private_phone=person.phone_number(),
                    )
                )
            for card in base_contact_list:
                print(card.contact())

        elif choice == "2":
            buisness_contact_list = []
            for _ in range(how_many):
                buisness_contact_list.append(
                    BusinessContact(
                        first_name=person.first_name(),
                        last_name=person.last_name(),
                        firm=person.company(),
                        position=person.job(),
                        mail=person.email(),
                        private_phone=person.phone_number(),
                        work_phone=person.phone_number(),
                    )
                )
            for card in buisness_contact_list:
                print(card.contact())
    else:
        logging.error("Nieprawidłowy wybór!")


if __name__ == "__main__":
    create_contacts()
