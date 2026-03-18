# 1
students = {
      "Ali": 85,
      "Vali": 90,
      "Hasan": 78,
      "Husan": 92
}

print(students)


m_ball = max(students.values())
print(students.values())
print(m_ball)

# 2
sales = {
    "apples": 50,
    "oranges": 75,
    "bananas": 30,
    "pears": 45
}

print(sales)


summa = sum(sales.values())

print(summa)

# 3
grades = {
    "Math": 80,
    "Physics": 75,
    "Chemistry": 85,
    "Biology": 90
}

print(grades)

for s, score in grades.items():
    if score > 75:
        print(s)

# 4
inventory = {
    "pen": 10,
    "pencil": 20,
    "notebook": 15,
    "eraser": 5
}

print(inventory)

min_item = min(inventory, key=inventory.get)
print(min_item)


# 5
products = {
    "A": 100,
    "B": 200,
    "C": 150,
    "D": 250
}

print(products)

a = sum(products.values()) / len(products)
print(a)

# 6
d = dict()

d["x"] = 10
d["y"] = 20
d["z"] = 30

print(d)


# 7
d = {
    "a": 5,
    "b": 10
}

print(d)

# 8
d = dict(name="Ali", age=20)

d["age"] = 25

print(d)


# 10
d1 = {"x": 1, "y": 2}
d2 = {"y": 3, "z": 4}

d1.update(d2)

print(d1)
