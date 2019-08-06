# https://realpython.com/python-f-strings/
class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


def main():
    new_comedian = Comedian("Eric", "Idle", "74")
    print(new_comedian)  # gọi hàm __str__
    print(f"{new_comedian}")  # gọi hàm __str__
    print(f"{new_comedian!r}")  # gọi hàm __repr__


if __name__ == '__main__':
    main()
