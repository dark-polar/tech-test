words = ["pro", "gram", "merit", "program", "it", "programmer"]
patterns = "program"
matching = [s for s in words if patterns in s]

print(matching)
