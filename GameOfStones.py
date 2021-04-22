def gameOfStones(n):
    if (n % 7 == 0 or n % 7 == 1):
        return "Second";
    else:
        return "First";

print(gameOfStones(1))
print(gameOfStones(2))
print(gameOfStones(3))
print(gameOfStones(4))
print(gameOfStones(5))
print(gameOfStones(6))
print(gameOfStones(7))
print(gameOfStones(10))

