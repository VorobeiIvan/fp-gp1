from src.addressbook.models import AddressBook, Record
from src.addressbook.storage import get_upcoming_birthdays

def main():
    address_book = AddressBook()

    record1 = Record(name=type("Name", (), {"value": "John Doe"}), birthday=type("Birthday", (), {"value": "15.01.1985"}))
    record2 = Record(name=type("Name", (), {"value": "Jane Smith"}), birthday=type("Birthday", (), {"value": "20.01.1990"}))

    address_book.add_record(record1)
    address_book.add_record(record2)

    print("Address Book Records:")
    for name, record in address_book.items():
        print(f"Name: {name}, Birthday: {record.birthday.value if record.birthday else 'N/A'}")

    search_name = "John Doe"
    found_record = address_book.find(search_name)
    if found_record:
        print(f"\nFound record for {search_name}: {found_record.birthday.value if found_record.birthday else 'N/A'}")
    else:
        print(f"\nRecord for {search_name} not found.")


    print("\nUpcoming Birthdays:")
    print(get_upcoming_birthdays(address_book))

if __name__ == "__main__":
    main()