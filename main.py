class Game:
    def __init__(self, title, level):
        self.title = title
        self.__level = level

    def get_level(self):
        return self.__level

    def set_level(self, new_level):
        if 1 <= new_level <= 100:
            self.__level = new_level
            print("Level yangilandi")
        else:
            print("Level noto'g'ri")


g1 = Game("Minecraft", 10)

print(g1.title)
print(g1.get_level())

g1.set_level(50)
print(g1.get_level())

g1.set_level(150)

print()
