from datetime import date


class Medicine:
    """class representing a medicine"""

    def __init__(self, name, price, quantity, is_prescription_needed, expiration_date):
        """ініціалізація"""
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__is_prescription_needed = is_prescription_needed
        self.__expiration_date = expiration_date

    def __str__(self):
        """returns description of the medicine"""
        return (
            f"Medicine: {self.__name},"
            f"price: {self.__price},"
            f"expiration date: {self.__expiration_date}"
        )

    def __repr__(self):
        """ruturns string representation of the Medicine object"""
        return (
            f"Medicine({self.__name},"
            f"{self.__price},"
            f"{self.__quantity},"
            f"{self.__is_prescription_needed}, "
            f"{self.__expiration_date})"
        )

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
    """class representing a pharmacy"""

    def __init__(self):
        self.medicines = []

    def remove_expired_medicines(self):
        today = date.today()
        self.medicines = [
            med for med in self.medicines if med.get_expiration_date() >= today
        ]

    def apply_discount(self):
        for med in self.medicines:
            med.set_price(med.get_price() * 0.9)

    def get_cheapest_medicines(self, num):
        sorted_medicines = sorted(self.medicines, key=lambda x: x.get_price())
        return [(med.get_name(), med.get_price()) for med in sorted_medicines[:num]]

    def add_medicine(self, medicine):
        self.medicines.append(medicine)

    def remove_medicine(self, medicine_name):
        for med in self.medicines[:]:
            if med.get_name() == medicine_name:
                self.medicines.remove(med)
            print(f"The medicine {medicine_name} has been removed from the pharmacy.")
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
    for current_medicine in pharmacy.medicines:
        print(
            f"{current_medicine.get_name()}:"
            f"${current_medicine.get_price()},"
            f"Expired: {current_medicine.is_expired()}"
        )

    pharmacy.remove_expired_medicines()
    print("\nMedicines after removing expired:")
    for current_medicine in pharmacy.medicines:
        print(
            f"{current_medicine.get_name()}:"
            f"${current_medicine.get_price()}, "
            f"Expired: {current_medicine.is_expired()}"
        )

    pharmacy.apply_discount()
    print("\nMedicines after applying discount:")
    for current_medicine in pharmacy.medicines:
        print(f"{current_medicine.get_name()}, " f" ${current_medicine.get_price()}")

    print("\nTop 2 cheapest medicines:")
    top_cheapest = pharmacy.get_cheapest_medicines(2)
    for current_medicine in top_cheapest:
        print(f"{current_medicine[0]}: ${current_medicine[1]}")

    pharmacy.remove_medicine("Paracetamol")
    print("\nMedicines after removing Paracetamol:")
    for current_medicine in pharmacy.medicines:
        print(f"{current_medicine.get_name()}: ${current_medicine.get_price()}")
