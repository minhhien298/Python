from Python import file1


def main():
    print("File2 is being run directly")
    print("File2 __name__ = %s" % __name__)
    print(file1.avar)
    file1.avar = 12
    print(file1.avar)


if __name__ == "__main__":
    main()
else:
    print("File2 is being imported")

