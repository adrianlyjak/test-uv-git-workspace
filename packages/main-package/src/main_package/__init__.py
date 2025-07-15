from core_package import hello as hello_core

def hello() -> str:
    string = "Hello from main-package!" + hello_core()
    print(string)
    return string
