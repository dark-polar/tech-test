words = ["pro", "gram", "merit", "program", "it", "programmer"]
patterns = "program" # ganti sama string yang mau dicari
matching = [s for s in words if patterns in s]

print(matching)