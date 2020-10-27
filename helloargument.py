def get_username():
    name = input("whats your name?")
    return name.capitalize()


def get_hello_massage(name):
    if name == "":
        name = "World"
    return "hello, "+name


def say_hello():
    hello = get_hello_massage(get_username())
    print(hello)


say_hello()