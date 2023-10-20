def movie_organizer(*args):
    movies = {}
    for movie, genre in args:
        if genre not in movies.keys():
            movies[genre] = []
        movies[genre].append(movie)

    ordered_movies = dict(sorted(movies.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = []
    for genre, movies in ordered_movies.items():
        result.append(f'{genre} - {len(movies)}')
        for movie in sorted(movies):
            result.append(f'* {movie}')

    return '\n'.join(result)


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

# print(movie_organizer(
#     ("Avatar: The Way of Water", "Action"),
#     ("House Of Gucci", "Drama"),
#     ("Top Gun", "Action"),
#     ("Ted", "Comedy"),
#     ("Duck Soup", "Comedy"),
#     ("The Dark Knight", "Action"),
#     ("A Star Is Born", "Musicals"),
#     ("The Warrior", "Action"),
#     ("Like A Boss", "Comedy"),
#     ("The Green Mile", "Drama"),
#     ("21 Jump Street", "Comedy")))
