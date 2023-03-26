import spacy


def find_most_similar_movie(description):
    """
    Function that finds the most similar movie based on a given movie description
    :param description: a string representing a movie description
    :return: a string representing the most similar movie
    """
    # Load the spacy model
    nlp = spacy.load('en_core_web_md')

    # Read the movie descriptions from file
    with open('movies.txt', 'r') as f:
        movies = f.read().splitlines()

    # Create a dictionary of movie titles and descriptions
    movie_dict = {movie.split(' :')[0]: movie.split(' :')[1] for movie in movies}

    # Initialize the highest similarity coefficient and the most similar movie title
    highest_coefficient = 0
    most_similar_movie = ''

    # Iterate over all movies and calculate their similarity to the given movie description
    for title, movie_desc in movie_dict.items():
        movie_token = nlp(movie_desc)
        similarity_coefficient = nlp(description).similarity(movie_token)
        if similarity_coefficient > highest_coefficient:
            highest_coefficient = similarity_coefficient
            most_similar_movie = title

    return most_similar_movie


# Example usage
description = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for ' \
              'the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a ' \
              'planet where the Hulk can live in peace. Unfortunately, Hulk land on the ' \
              'planet Sakaar where he is sold into slavery and trained as a gladiator.'
most_similar_movie = find_most_similar_movie(description)
print(f'The most similar movie is {most_similar_movie}')
