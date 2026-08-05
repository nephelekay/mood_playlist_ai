from urllib.parse import quote

def createPlaylistHTML(recommendations, filename="output/playlist.html"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("""
        <html>
        <head>
            <title>MoodPlaylist AI</title>
        </head>
        <body>
            <h1>Your Recommended Playlist</h1>
            <ol>
        """)

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

            for reason in reasons:
                file.write(f"<li>{reason}</li>")

            file.write("""
                </ul>
            </li>
            """)

        file.write("""
            </ol>
        </body>
        </html>
        """)