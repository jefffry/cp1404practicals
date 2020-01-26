import os
from prac9cp1404 import FilesToSort


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        more_space = filename.split('.')[-1]

        try:
            os.mkdir(more_space)
        except FileExistsError:
            pass
        print("{}/{}".format(more_space, filename))

        os.rename(filename, "{}/{}".format(more_space, filename))


main()