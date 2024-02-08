print("Welcome to my game quiz!")

play = input("Are you ready? ")

if play.lower() != "yes":
    quit()

print("Okay! Let's play:)")

questions = [
    ("What is the full name of the game commonly referred to as WoW? ", "World of Warcraft"),
    ("Who is the main character in the game 'The Legend of Zelda'? ", "Link"),
    ("In Minecraft, what material is used to craft torches? ", "Stick"),
    ("What is the main objective in the game 'Fortnite'? ", "Be the last one standing"),
    ("Which game features a plumber named Mario? ", "Super Mario"),
    ("What is the name of the company that developed the game 'Grand Theft Auto'? ", "Rockstar Games"),
    ("What is the highest selling video game of all time? ", "Minecraft"),
    ("Which game features a character named Pikachu? ", "Pokemon"),
    ("What is the name of the protagonist in 'Assassin's Creed'? ", "Altair"),
    ("What is the currency used in 'The Sims' games? ", "Simoleons"),
    ("In which game can you find the character Nathan Drake? ", "Uncharted"),
    ("What is the name of the virtual world created by Linden Lab? ", "Second Life"),
    ("Which game franchise features characters like Master Chief and Cortana? ", "Halo"),
    ("What is the name of the fictional continent in 'The Elder Scrolls' series? ", "Tamriel"),
    ("Which game revolves around a group of survivors trying to fend off zombies? ", "Left 4 Dead"),
    ("What is the name of the princess in the 'Legend of Zelda' series? ", "Zelda"),
    ("Which game has the slogan 'Gotta Catch 'Em All'? ", "Pokemon"),
    ("In which game can you perform fatalities? ", "Mortal Kombat"),
    ("What is the name of the map in 'Among Us' where players complete tasks? ", "The Skeld"),
    ("Which game features the character Geralt of Rivia? ", "The Witcher")
]

score = 0

for question, correct_answer in questions:
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print("That is correct!")
        score += 1
    else:
        print("Wrong answer. The correct answer is:", correct_answer)

print("Game over! You scored", score, "out of", len(questions))
