class LogExecution:
    def __init__(self, message):
        self.message = message

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"Starting: {self.message}")
            result = func(*args, **kwargs)
            print(f"Finishing: {self.message}")
            return result
        return wrapper

@LogExecution("Adding two numbers")
def add(a, b):
    return a + b

result = add(3, 4)
print(f"Sum result: {result}")
