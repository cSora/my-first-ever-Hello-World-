def get_hello_massage():
    question = input("whats your name?")
    if question == "":
        question = "world"
    return "hello, "+question


def say_hello():
    hello = get_hello_massage()
    print(hello)


say_hello()