import greeting

print("File1 __name__ = %s" % __name__)

avar = 10

if __name__ == "__main__":
    print("File1 is being run directly")
else:
    print("File1 is being imported")
    greeting.say_hello('HI')
