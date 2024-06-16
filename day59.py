def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx
@greet
def hello():
    print("hello world")
def add(a, b):
    print(a + b)

hello()
greet(hello)()
greet(add)(1, 2)
add(1, 2) 
add(1, 4)