from nested_data import albums

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artists, year, songs) in enumerate (albums):
        print ("{}: {}, {}, {}, {}".format(index + 1, title, artists, year, songs))

    for index, value in enumerate(albums):
        title, artists, year, songs = value
        print(index, title, artists, year, songs)
    break



