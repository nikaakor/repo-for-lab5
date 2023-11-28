from datetime import date

class Medicine:
    def __init__(self, name, price, quantity, is_prescription_needed, expiration_date):
        """ініціалізація"""
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__is_prescription_needed = is_prescription_needed
        self.__expiration_date = expiration_date

    def __str__(self):
        """повертає рядок, що містить опис медикаменту."""
        return f"Medicine: {self.__name}, price: {self.__price}, expiration date: {self.__expiration_date}"

    def __repr__(self):
        """повертає рядок, що містить конструктор обʼєкта медикаменту"""
        return f"Medicine({self.__name}, {self.__price}, {self.__quantity}, {self.__is_prescription_needed}, {self.__expiration_date})"

    def is_expired(self):
        today = date.today()
        return self.__expiration_date < today

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_is_prescription_needed(self):
        return self.__is_prescription_needed

    def get_expiration_date(self):
        return self.__expiration_date

    def set_price(self, new_price):
        self.__price = new_price

class Pharmacy:
    def __init__(self):
        self.medicines = []

    def remove_expired_medicines(self):
        today = date.today()
        self.medicines = [med for med in self.medicines if med.get_expiration_date() >= today]

    def apply_discount(self):
        for med in self.medicines:
            med.set_price(med.get_price() * 0.9)

    def get_cheapest_medicines(self, num):
        sorted_medicines = sorted(self.medicines, key = lambda x: x.get_price())
        return [(med.get_name(), med.get_price()) for med in sorted_medicines[:num]]

    def add_medicine(self, medicine):
        self.medicines.append(medicine)

    def remove_medicine(self, medicine_name):
        for med in self.medicines:
            if med.get_name() == medicine_name:
                self.medicines.remove(med)
                return
        print("The medicine isn't found in the pharmacy.")

if __name__ == "__main__":
    medicine1 = Medicine("Aspirin", 5, 50, False, date(2023, 12, 31))
    medicine2 = Medicine("Paracetamol", 3, 30, False, date(2024, 6, 15))
    medicine3 = Medicine("Antibiotic", 15, 20, True, date(2022, 8, 1))
    medicine4 = Medicine("Nurofen", 10, 40, True, date(2024, 5, 12))
    medicine5 = Medicine("Strepsils", 25, 15, False, date(2023, 11, 13))

    pharmacy = Pharmacy()

    pharmacy.add_medicine(medicine1)
    pharmacy.add_medicine(medicine2)
    pharmacy.add_medicine(medicine3)
    pharmacy.add_medicine(medicine4)
    pharmacy.add_medicine(medicine5)

    print("Original Medicines:")
    for med in pharmacy.medicines:
        print(f"{med.get_name()}: ${med.get_price()}, Expired: {med.is_expired()}")

    pharmacy.remove_expired_medicines()
    print("\nMedicines after removing expired:")
    for med in pharmacy.medicines:
        print(f"{med.get_name()}: ${med.get_price()}, Expired: {med.is_expired()}")

    pharmacy.apply_discount()
    print("\nMedicines after applying discount:")
    for med in pharmacy.medicines:
        print(f"{med.get_name()}: ${med.get_price()}")

    print("\nTop 2 cheapest medicines:")
    top_cheapest = pharmacy.get_cheapest_medicines(2)
    for med in top_cheapest:
        print(f"{med[0]}: ${med[1]}")

    pharmacy.remove_medicine("Paracetamol")
    print("\nMedicines after removing Paracetamol:")
    for med in pharmacy.medicines:
        print(f"{med.get_name()}: ${med.get_price()}")

    