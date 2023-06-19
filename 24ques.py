# Question 24
class Car:
    def set_brandname(self, brandname):
        self.brandname = brandname

    def get_brandname(self):
        return self.brandname

class Accord(Car):
    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

acc = Accord()

brandname = input("Enter the brandname: ")
acc.set_brandname(brandname)

model = input("Enter the model: ")
acc.set_model(model)

print("Brandname:", acc.get_brandname())
print("Model:", acc.get_model())
