import fresh_tomatoes
import media

# Below are instances of class Movie with their instance variables.

hudsucker = media.Movie("The Hudsucker Proxy",
                        "A naive business graduate is installed as president \
                        of a manufacturing company as part of a stock scam. \
                        The plot backfires when the graduate's latest \
                        invention succeeds.",
                        "proxy.jpg",
                        "https://www.youtube.com/watch?v=dBa8p0NFwM8",
                        "Comedy",
                        1994,
                        111)

black_stallion = media.Movie("The Black Stallion",
                             "A story about a boy shipwrecked with a wild \
                             stallion. He befriends it and when rescued, \
                             return to his home where they train to race \
                             against the fastest horses in the world.",
                             "stallion.jpg",
                             "https://www.youtube.com/watch?v=wMGaIr7kCqc",
                             "Adventure",
                             1979,
                             118)

space_odyssey = media.Movie("2001: A Space Odyssey",
                            "Humanity finds a mysterious object buried \
                            beneath the Lunar surface and, with the \
                            intelligent computer H.A.L. 9000, sets off \
                            on a quest.",
                            "space.jpg",
                            "https://www.youtube.com/watch?v=Ok32VyEQYYc",
                            "Science Fiction",
                            1968,
                            160)

forgotten_dreams = media.Movie("Cave of Forgotten Dreams",
                               "Werner Herzog gains exclusive access to film \
                               inside the Chauvet caves of Southern France \
                               and captures the oldest known pictorial \
                               creations of humanity.",
                               "cave.jpg",
                               "http://www.youtube.com/"
                               "watch?v=kULwsoCEd3g&t=0m6s",
                               "Documentary",
                               2010,
                               90)

stand_by_me = media.Movie("Stand By Me",
                          "After the death of a friend, a writer recounts a \
                          boyhood journey to find the body of a missing boy. \
                          Just a lark at first, the boys' adventure evolves \
                          into a defining event in their lives.",
                          "standby.jpg",
                          "https://www.youtube.com"
                          "/watch?v=FUVnfaA-kpI&t=0m6s",
                          "Adventure",
                          1986,
                          89)

princess_bride = media.Movie("The Princess Bride",
                             "A fairy tale adventure about a beautiful young \
                             woman and her one true love. They must battle \
                             the evils of the mythical kingdom of Florin to \
                             be reunited with each other.",
                             "princess.jpg",
                             "https://www.youtube.com/watch?v=O3CIXEAjcc8",
                             "Adventure",
                             1987,
                             98)


# define these instances as an array that can be called as a single object.

movies = [hudsucker, black_stallion, space_odyssey, forgotten_dreams,
          stand_by_me, princess_bride]


# call the method open_movies_page from the fresh_tomatoes module with the
# movies object as an arguement.

fresh_tomatoes.open_movies_page(movies)
