def mark_bold(function):
    def wrapper(*args, **kwargs):
        return '<b>'+function(*args, **kwargs)+'</b>'
    return wrapper

@mark_bold
def hello(string):
    return string

print(hello('Hello'))