#Data Preparation:
persons_list= [
    {"name": "Kuldeep", "age": 22, "city": "INDORE"},
    {"name": "Tonny", "age": 20, "city": "Ratlam"},
    {"name": "Kandy", "age": 26, "city": "Pune"},
    {"name": "Kunj", "age": 24, "city": "Mumbai"}
]

# Filtering: Persons under the age of 25
filtered_persons = [person for person in persons_list if person["age"] >= 25]

#Sort by city in alphabetical order
sorted_persons = sorted(filtered_persons, key=lambda x: x["city"])

#Print the final list of persons
for person in sorted_persons:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
    