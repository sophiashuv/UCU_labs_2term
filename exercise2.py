class Animal:
    def __init__(self, phylum, clas):
		self.phylum = phylum
		self.clas = clas

	def __str__(self):
		return "<animal class is {}>".format(self.clas)



class Cat(Animal):
	def __init__(self, phylum, clas, genus):
		super().__init__(phylum, clas)
		self.genus = genus


	def sound(self):
		return 'Meow'


	def __str__(self):
		return "<This {} animal class is {}>".format(self.genus, self.clas)


if name == '__main__':
	animal1 = Animal("chordata", "mammalia")
	assert (animal1.phylum == "chordata")
	assert (animal1.clas == "mammalia")
	assert (str(animal1) == "<animal class is mammalia>")
	animal2 = Animal("chordata", "birds")
	assert (not (animal1 == animal2))
	cat1 = Cat("chordata", "mammalia", "felis")
	assert (cat1.sound() == "Meow")
	assert (cat1.genus == "felis")
	assert (isinstance(cat1, Animal))
	assert (str(cat1) == "<This felis animal class is mammalia>")