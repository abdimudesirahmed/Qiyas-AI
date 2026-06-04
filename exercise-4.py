# =====================================================
# Exercise 4: Movie Rating Analysis System
# =====================================================

movies = [
    ("Inception", 8.8),
    ("Titanic", 7.9),
    ("Avatar", 8.1),
    ("Batman", 6.5),
    ("Joker", 9.0),
    ("Frozen", 5.9)
]


def highest_rated_movie(movie_list):
    """
    Return highest rated movie.
    """
    return max(movie_list, key=lambda x: x[1])
    
print(highest_rated_movie(movies))
pass


def lowest_rated_movie(movie_list):
    """
    Return lowest rated movie.
    """
    return min(movie_list, key=lambda x: x[1])
    
print(lowest_rated_movie(movies))
pass


def average_rating(movie_list):
    """
    Calculate average movie rating.
    """
    total_rating = sum(rating for _, rating in movie_list)
    return total_rating / len(movie_list)
print(average_rating(movies))
pass


def movies_above_8(movie_list):
    """
    Use filter() to return movies above 8.0.
    """
    return list(filter(lambda x: x[1] > 8.0, movie_list))
print(movies_above_8(movies))
pass


def sort_movies(movie_list):
    """
    Sort movies by rating descending.
    """
    return sorted(movie_list, key=lambda x: x[1], reverse=True)
print(sort_movies(movies))
pass


def process_ratings(movie_list):
    """
    Square ratings above 7.
    Cube ratings below 7.
    """
    return [(movie[0], movie[1] ** 2) if movie[1] > 7 else (movie[0], movie[1] ** 3) for movie in movie_list]
print(process_ratings(movies))
pass


def add_rating_bonus(movie_list):
    """
    Add 0.5 bonus rating using map().
    """
    return list(map(lambda x: (x[0], x[1]+0.5), movie_list))
print(add_rating_bonus(movies))
pass


def additional_movies(movie_list):
    """Add new movies to the list.
    using map() to add new movies 
    """
    new_movies =map(lambda x: (x[0], x[1]), [("Interstellar", 8.6), ("The Dark Knight", 9.0)])
    return movie_list + list(new_movies)
print(additional_movies(movies))

def sort_movies_by_name(movie_list):
    """
    Sort movies by name.
    """
    return sorted(movie_list, key=lambda x: x[0])
print(sort_movies_by_name(movies))

pass