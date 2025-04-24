from abc import ABC, abstractstaticmethod

class ISingleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(IPerson, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

p1 = ISingleton()
print(p1)
p2 = ISingleton()
print(p2)

