 #დავალება 1

favorite_movies = [
    "Star wars episode VI",
    "The Dark Knight",
    "silicon valley",
    "star wars epsisode III",
    "Interstellar",
    "The Godfather",
    "Fight Club",
    "The Matrix",
    "Forrest Gump",
    "The Lord of the Rings: The Fellowship of the Ring"
]

for movie in favorite_movies:
    print(movie)


#დავალება 2


family_members = [
    "Nita", 
    "Bakuri", 
    "Luka", 
    "Tamuna", 
]

sentence = "My name is {}. My mother's name is {}. My father's name is {}. My sister's name is {}. My brother's name is {}. My aunt's name is {}. My uncle's name is {}. My cousin's name is {}. My grandmother's name is {}. My grandfather's name is {}.".format(
    family_members[0], 
    family_members[1], 
    family_members[2], 
    family_members[3], 
)

print(sentence)


#დავალება 3

friend_names = [
    "Taso",
    "Tazo",
    "Lasha",
    "Dachi",
]


for friend in friend_names:
    print(friend)


#დავალება 4

group_members = [
    ("Tazo", "kldiashvili"),
    ("Mate", "Kotorashvili"),
    ("Andria ", "Mekaluashvili"),
    ("Giviko", "")
]

def describe_member(name, surname):
    description = {
        "Tazo Kldiashvili": "Tazo is good firend, he knows many things",
        "Mate Kotorashvili": "Mate knows well python and sometimes he helping me",
        "Andria Mekaluashvili": "he is so smart",
        "Giviko": "he is so active "
    }
    full_name = name + " " + surname
    if full_name in description:
        print(full_name + ": " + description[full_name])
    else:
        print(full_name + ": No description available.")

for member in group_members:
    describe_member(member[0], member[1])
