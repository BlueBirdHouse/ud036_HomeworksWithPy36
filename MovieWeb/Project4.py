import Media
import fresh_tomatoes
import os

print(os.getcwd())

Toy_Story = Media.Movie("Toy Story","In a world where toys are living things who pretend to be lifeless when humans are present.",
            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#Toy_Story.ShowTrailer()
fresh_tomatoes.open_movies_page([Toy_Story])
Temp = 0