l = ["Bob", "Rolf", "Anne"]

t = ("Bob", "Rolf", "Anne")

s = {"Bob", "Rolf", "Anne"}

# Accessing
print(l[0])
print(t[2])


# Modifying
l[0] = "Smith"
print(l)

# This will cause an error because tuples are immutable
# t[0] = "Jhon"
# print(t)

# Sets does not support subscript notation
# s{0} = "Smith"

# Adding elements
l.append("Carlos")
print(l)

# This causes an error, because touples has no attribute append
# t.append("Carlos")
# print(t)

s.add("Juan")

# Removing elements
l.remove("Carlos")
print(l)

s.remove("Bob")
print(s)
