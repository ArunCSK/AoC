class Inte:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, index):
        return self.value[index]

    def __setitem__(self, index, value):
        self.value[index] = value

    def __delitem__(self, index):
        del self.value[index]

    def __repr__(self):
        return f'Inte({self.value})'
    
test_inte: Inte = Inte([1, 2, 3, 4, 5])
print(test_inte[2])  # Output: 1
test_inte[2] = 10
print(test_inte)  # Output: 10
del test_inte[1]
print(test_inte)  # Output: Inte([1, 10, 4, 5])