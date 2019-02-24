people = ["Sam", "Sarah", "Faith", "Kristy", "Cheryl", "Lisa"]

for person in people:
    print(f"Dear {person}, please come to dinner.")


print(f"{people[3]} cannot make dinner")

people[3] = "Renee"

for person in people:
    print(f"Dear {person}, please come to dinner.")


people.insert(0, "Bob")
people.insert(3, "James")
people.append("Peter")

print(people)


