class Cat:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def describe_cat(self):
        full_name = f"{self.name} {self.gender} {self.age}"
        return full_name.title()

cat_sam = Cat('sam', 'male', 2)
print(cat_sam.describe_cat())

cat_baron = Cat('baron', 'male', 2)
print(cat_baron.describe_cat())
