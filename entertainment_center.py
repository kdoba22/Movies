import fresh_tomatoes
import media

# create instances of the Movie class passing all 4 arguments
# needed to create the instance correnctly
rocky = media.Movie("Rocky",
                    "A local boxer gets the chance  of a lifetime",
                    "https://upload.wikimedia.org/wikipedia/en/1/18/"
                    "Rocky_poster.jpg",
                    "https://www.youtube.com/watch?v=PZ0a2tUh4Nc")

american_history_x = media.Movie("American History X",
                                 "A young skinheads transformation",
                                 "https://upload.wikimedia.org/wikipedia"
                                 "/en/0/0a/"
                                 "American_history_x_poster.jpg",
                                 "https://www.youtube.com/watch?v=XfQYHqsiN5g")

rudy = media.Movie("Rudy",
                   "A young man's will and drive to play Notre Dame Football",
                   "https://upload.wikimedia.org/wikipedia/en/2/29/Rudy2.jpg",
                   "https://www.youtube.com/watch?v=5HotC8sXQPg")

tombstone = media.Movie("Tombstone",
                        "The story of Wyatt Earp and the"
                        " 'Shootout at the OK coral'",
                        "https://upload.wikimedia.org/wikipedia/en/7/71/"
                        "Tombstoneposter.jpeg",
                        "https://www.youtube.com/watch?v=Mtu4ThDIdoA")

something_the_lord_made = media.Movie("Something the Lord Made",
                                      "The story of the firstopen heart"
                                      " surgury",
                                      "https://upload.wikimedia.org/"
                                      "wikipedia/en/5/57/"
                                      "Something_the_Lord_Made.jpg",
                                      "https://www.youtube.com/watch?v="
                                      "UmiRohBSy5Y")

march_of_the_penguins = media.Movie("March of the Penguins",
                                    "The story of the great penguin march",
                                    "https://upload.wikimedia.org/wikipedia"
                                    "/en/1/19/March_of_the_penguins_poster"
                                    ".jpg",
                                    "https://www.youtube.com/watch?v="
                                    "L7tWNwhSocE")

# create a movie array to be used to create themovies in the html page

movies = [rocky, american_history_x, rudy, tombstone, something_the_lord_made,
          march_of_the_penguins]

#dynamically generate python data structure
fresh_tomatoes.open_movies_page(movies)
