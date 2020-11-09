import library.file

def get_artist_list(alphabet):

    if library.file.file_exists("S:\\Website Projects\\live\\freemidi\\artist\\"+alphabet+".html"):
        pass
    else:
        library.url.download_html_content("https://freemidi.org/artists-"+alphabet,"S:\\Website Projects\\live\\freemidi\\artist\\"+alphabet+".html")