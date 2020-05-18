"""
Write a User class, for a fun Taco Reward program
A User knows: name, number of tacos (starts at 5, goes down when they give a taco), and their score
A User can give a taco to another user
We should be able to print a User like:	Ben, 2 points, 4 tacos left
When we make a user, they start with the name we want and appropriate default values


"""

INITIAL_NUMBER_OF_TACOS = 5


class User:

    def __init__(self, name="", score=0):
        self.name = name
        self.number_of_tacos = INITIAL_NUMBER_OF_TACOS
        self.score = score
        self._taco_value = "Default value"
        self._private = "Test private"
        self.__hidden = "Test hidden"

    def __str__(self):
        return "{self.name}, {self.score} points, {self.number_of_tacos} tacos left".format(self=self)

    def __repr__(self):
        return str(self)

    def give_taco(self, other, number_given=1):
        if number_given < 1:
            return
        if self.number_of_tacos < number_given:
            number_given = self.number_of_tacos
        self.number_of_tacos -= number_given
        other.score += number_given

    def steal_taco(self, other):
        self.score = 0


user1 = User("Ben", 4)
user2 = User("Margaret")
user1.give_taco(user2, 2)
# print(user1)
# print(user2)
print(user1._User__hidden)

# user1.steal_taco(user2)
# assert user1.score == 0
#
# print(user1._User__hidden)
# print(user1._private)
#
# print(user1.__dict__)