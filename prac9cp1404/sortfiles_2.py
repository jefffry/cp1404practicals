import os
from prac9cp1404 import FilesToSort


def main():

    more_category = {}

    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        more_space = filename.split('.')[-1]

        if more_space not in more_category:
            category = input("What category you want to sort {} the files into? ".format(more_space))

            more_category[more_space] = category
            try:
                os.mkdir(category)

            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(more_category[more_space],filename))


main()
