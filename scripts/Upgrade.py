# automatic script every X time


def upgrade():
    file_source = open("to_add.txt", "r+")
    file_destination = open("lenses.txt", "a")
    for line in file_source.readlines():
        file_destination.write(line)
    file_source = open("to_add.txt", "w")
    open('file.txt', 'w').close()


upgrade()