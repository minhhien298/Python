class Food:
    def __init__(self, id, name, rating, photo):   # Constructor
        self.id = id
        self.name = name
        self.rating = rating
        self.photo = photo

    def __str__(self):
        return f"{self.name} - {self.rating}"


if __name__ == "__main__":
    taco = Food("Taco", 5)
    bun_cha = Food("Bún Chả", 4.5)
    print(bun_cha)