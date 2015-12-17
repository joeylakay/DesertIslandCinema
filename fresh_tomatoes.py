import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link rel="icon" href="clapper.ico" type="image/x-icon"/>
    <title>Desert Island Cinema</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="libs/bootstrap.min.css">
    <link rel="stylesheet" href="libs/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="libs/bootstrap.min.js"></script>

    <!-- Styling  -->
    <link href='https://fonts.googleapis.com/css?family=Poiret+One'
    rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Lobster'
    rel='stylesheet' type='text/css'>
    <style type="text/css" media="screen">
        body {
          padding-top: 10px;
          font-family: 'Poiret One', cursive;
          background: #000000;
        }
        h3 {
          color: #DFDFDF;
        }
        .navbar {
          color: #1F1F1F;
          margin-left: -2em;
          margin-bottom: 4em;
          padding-left: 2em;
        }
        .navbar-brand
        {
          padding-top: 0;
        }
        #title {
          padding: 20px;
          font-family: 'Lobster', cursive;
          font-size: 1.5em;
          color: #FFFFFF;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 960px;
            height: 480px;
        }
        .modal-backdrop.in {
            background-color: black;
            opacity: 0.85 !important;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-top: 30px;
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
          cursor: pointer;
          opacity: 1;
        }
        .media {
          display: inline-block;
          position: relative;
          vertical-align: top;
          margin-top: 30px;
          margin-bottom: 20px;
        }
        .media__image { display: block; }
        .media__body {
          display: block;
          background: rgba(0, 0, 0, 0.85);
          bottom: 0;
          color: white;
          font-size: 1em;
          left: 0;
          opacity: 0;
          overflow: hidden;
          padding: 2.5em 5.75em;
          position: absolute;
          text-align: center;
          top: 0;
          right: 0;
          -webkit-transition: 0.6s;
          transition: 0.6s;
        }
        .media__body:hover { opacity: 1; }
        .media__body h2 { margin-top: 0; }
        .media__body p { margin-bottom: 1.5em; }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: black;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop,.modal',
          function (event) {
            // Remove the src so the player itself gets removed,
            // as this is the only reliable way to ensure the video stops
            // playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' +
              trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($
              ("<iframe></iframe>",{
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
      <!-- Trailer Video Modal -->
      <div class="modal" id="trailer">
        <div class="modal-dialog">
          <div class="modal-content">
            <a href="#" class="hanging-close" data-dismiss="modal"
            aria-hidden="true">
              <img src="images/close.png"/>
            </a>
            <div class="scale-media" id="trailer-video-container">
            </div>
          </div>
        </div>
      </div>

      <!-- Main Page Content -->
      <div class="container">
        <div class="navbar navbar-static-top" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <a class="navbar-brand" id="title" href="#">
                <img src="images/clapper.png">
                <span id="title">Desert Island Cinema</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-xs-6 col-md-6 col-lg-4 movie-tile text-center"
  data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal"
  data-target="#trailer">
  <img src="images/{poster_image_url}" width="220" height="342">
  <h3>{movie_title}</h3>
  <div class="media__body">
    <h2>{movie_title}</h2>
    <br>
    <p>{movie_storyline}</p>
    <p>{movie_genre} ~ {running_time} min ~ {release_year}</p>
  </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_genre=movie.genre,
            release_year=movie.relyear,
            running_time=movie.total_running_time
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
