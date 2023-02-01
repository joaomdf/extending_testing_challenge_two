from faker import Faker
import os
import shutil

class Application():
    def __init__(self):
        self.fake = Faker("en_UK")

    def clear_for_test(self):
        shutil.rmtree('target_directory/finals')
        os.makedirs('target_directory/finals')
        shutil.rmtree('target_directory/originals')
        os.makedirs('target_directory/originals')
        shutil.rmtree('target_directory/updates')
        os.makedirs('target_directory/updates')
        if os.path.exists("target_directory/allowlist"):
            os.remove("target_directory/allowlist")
        if os.path.exists("target_directory/droplist"):
            os.remove("target_directory/droplist")

    def create_allowlist(self, seed_number,number_of_records):
        f = open("target_directory/allowlist", "w+")
        Faker.seed(int(seed_number))
        for i in range(0,int(number_of_records)):
            name = self.fake.name()
            split_name = name.split(" ")
            surname = split_name[-1]
            f.write(surname + "\n")
        f.close()

    def create_droplist(self, seed_number,number_of_records):
        f = open("target_directory/droplist", "w+")
        Faker.seed(int(seed_number))
        for i in range(0,int(number_of_records)):
            name = self.fake.name()
            split_name = name.split(" ")
            surname = split_name[-1]
            f.write(surname + "\n")
        f.close()

    def create_original(self, seed_number,number_of_records):
        surname_list = []
        name_list = []
        address_list = []
        Faker.seed(int(seed_number))
        for i in range(0,int(number_of_records)):
            name = self.fake.name()
            name_list.append(name)
            split_name = name.split(" ")
            surname = split_name[-1]
            surname_list.append(surname)

        Faker.seed(int(seed_number))
        for i in range(0,int(number_of_records)):
            address = self.fake.address()
            address_list.append(address)

        for i in range(0,int(number_of_records)):
            f = open(f"target_directory/originals/{surname_list[i]}", "w+")
            f.write(name_list[i] + "\n")
            f.write(address_list[i])
        f.close()

if __name__ == '__main__':
    app = Application()
    app.clear_for_test()
    original_seed = int(input("Choose your original records data seed:"))
    number_of_records = int(input("Choose number of original records to create:"))
    app.create_original(original_seed,number_of_records)
    allow_or_drop = input("Allowlist or droplist (A/D):")
    if allow_or_drop.capitalize() == "A":
        app.create_allowlist(original_seed,number_of_records)
    elif allow_or_drop.capitalize() == "D":
        app.create_droplist(original_seed,number_of_records)
    updates = ""
    while updates != "DONE":
        updates = input("Check folder directory and pick your updates. Input DONE when finished.")
        if updates == "DONE":
            break
        shutil.copyfile("target_directory/originals/" + updates, "target_directory/updates/" + updates)