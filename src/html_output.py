from pathlib import Path
from urllib.parse import quote
import webbrowser


def createPlaylistHTML(recommendations, filename="output/playlist.html"):
    """
    Generates HTML file showing recommended songs, reasons for recommendation, and Spotify
    search links. Opens HTML file automatically in the user's default web browser.
    Args:
        recommendations (list): List of tuples containing (song_object, score, reasons_list).
        filename (str): Destination file path for generated HTML.
    """
    output_path = Path(filename) #Ensure target directory exists before creating file
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file: # Open file with UTF-8 encoding, supporting multiple languages
        file.write("""
        <html>
        <head>
        <body style="font-family: Arial; background-color: #f4f4f4; padding: 20px;">
            <h1>MoodPlaylist AI 🎵</h1>
            <h2>Your Recommended Playlist</h2>
            <ol>
        """)
        # Create list of songs based on recommendations including generated Spotify link
        for song, score, reasons in recommendations:
            file.write(f"""
            <li>
                <p>
                    <a href="https://open.spotify.com/search/{quote(song.title + ' ' + song.artists)}">
                        {song.title}
                    </a>
                </p>
                <p>Artist: {song.artists}</p>
                <p>Album: {song.album}</p>
                <p>Score: {score:.3f}</p>
                <ul>
            """)
            # Add bullet points explaining reasons each song was included
            for reason in reasons:
                file.write(f"<li>{reason}</li>")
            # Close reasons list
            file.write("""
                </ul>
            </li>
            """)
        # Close HTML tags left
        file.write("""
            </ol>
        </body>
        </html>
        """)

    webbrowser.open(output_path.resolve().as_uri()) # Open HTML page automatically in default browser

    print(f"Playlist created: {output_path.resolve()}")