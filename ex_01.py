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
        self._label_length = len(f"{self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return self._label_length

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


def create_contacts(choice, how_many):
    new_list = []
    match choice:
        case "1":
            for _ in range(how_many):
                new_list.append(
                    BaseContact(
                        first_name=person.first_name(),
                        last_name=person.last_name(),
                        mail=person.email(),
                        private_phone=person.phone_number(),
                    )
                )
        case "2":
            for _ in range(how_many):
                new_list.append(
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
    return new_list


if __name__ == "__main__":
    choice = input(
        "Jaki rodzaj wizytówek wybierasz? :\n1 Base Contact\n2 Buisnes Contact\n"
    )
    if choice in ("1", "2"):
        try:
            how_many = int(input("Ile wygenerować ? "))
        except ValueError:
            logging.error("Nieprawidłowe dane!")
            exit(0)
        list = create_contacts(choice, how_many)
        for card in list:
            print(card.contact())
    else:
        logging.error("Nieprawidłowy wybór!")
