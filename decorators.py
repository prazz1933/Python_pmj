def display(func):
    def wrapper(*args, **kwargs):
        print("hello everyone")
        print(f"Function '{func.__name__}' is about to be called.")
        result = func(*args, **kwargs)