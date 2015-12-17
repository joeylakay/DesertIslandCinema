## Synopsis

This application builds a webpage where users can see my favorite movies and watch the trailers. The server side code, stores a list of movie titles, box art, poster images, movie trailer URLs and other movie data. The data is expressed on the web page and allow users to watch the trailers when clicking on the individual movie listings.

## Code Example

- All files can be found in the **movies** directory.
- To build a new instance of class Movie:
    - Navigate to the **entertainment_center.py** file.
    - Create a new class instance using the following syntax:

    ```
    princess_bride = media.Movie("The Princess Bride",
        "A fairy tale adventure about a beautiful young woman and her one true love. They must battle the evils of the mythical kingdom of Florin to be reunited with each other.",
        "http://41.media.tumblr.com/31b63a6e63596abccc4806c4bccc7a1c/tumblr_mt8b3iae4D1rfnfyzo1_1280.jpg",
        "https://www.youtube.com/watch?v=O3CIXEAjcc8",
        "Adventure",
        1987,
        98)
    ```

- To add the new movie object to the website, append the latest instance to the movies array, like so:

    ```
    movies = [hudsucker, black_stallion, space_odyssey, forgotten_dreams, stand_by_me, princess_bride]
    ```

- To update the rendering and styling of the webpage, update the html and css code embedded in the fresh_tomatoes.pyfile.  This script dynamically generates the html file **fresh_tomatoes.html**.

## Motivation

This app was built as an assignment as part of Udacity's Full-Stack Developer Nano-degree.

## Installation

To install this app:

- Download and unpack the file **movie.zip**.
- Run the entertainment_center.py python module using your favorite python integrated development environment.
- I used IDLE, but you can launch the script from the command line as well!

    ```
    cd dir_where_you_put_movies/movies
    python entertainment_center.py
    ```

- This will generate the fresh_tomatoes.html and launch a web browser with the rendered html.

## Directory structure:

- movies/
    - clapper.ico
    - entertainment_center.py
    - fresh_tomatoes.html
    - fresh_tomatoes.py
    - images/
        - clapper.png
    - libs/
        - bootstrap-theme.min.css
        - bootstrap.min.css
        - bootstrap.min.js
    - media.py
    - README.md

## Contributors

- Joanna Laurent

## License

- Open-Source