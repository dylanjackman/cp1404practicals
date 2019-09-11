class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "Guitar: {}, Year of Make({}), worth ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2019 - self.year
        # age -= self.year
        # if age < 50:
        #     return "The guitar is {} years old and is not vintage".format(age)
        # else:
        #     return "The guitar is {} years old and is a vintage".format(age)

    def is_vintage(self):
        return self.get_age() >= 50

