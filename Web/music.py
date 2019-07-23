import sys
import json
import urllib.request
from urllib.parse import quote_plus

root_url = "http://musicbrainz.org/ws/2/{api}?query={term}&fmt=json"


def urlencode(search_term):
    return quote_plus(search_term)


def search_artist(search_term):
    search_term = urlencode(search_term)
    url = root_url.format(api="artist", term=search_term)
    response = urllib.request.urlopen(url)
    content = response.read()
    content_as_string = content.decode()
    data = json.loads(content_as_string)

    musician = data["artists"][0]["sort-name"]
    print(musician)
    print("----------")
    category = data["artists"][0]["tags"]
    for m in range(len(category)):
        tags = category[m]
        name = tags["name"]
        print (name)


def search_song(search_term):
    search_term = urlencode(search_term)
    url = root_url.format(api="release", term=search_term)
    response = urllib.request.urlopen(url)
    content = response.read()
    data = json.loads(content)

    for i in data["releases"]:
        artist = i["artist-credit"][0]["artist"]
        name = artist["name"]
        title = i["title"]
        print("{} by {}".format(title, name))


if __name__ == "__main__":
    command = sys.argv[1]
    search_term = sys.argv[2]
    if command == "song":
        search_song(search_term)
    elif command == "artist":
        search_artist(search_term)
    else:
        print("Unknown command:" + command)
