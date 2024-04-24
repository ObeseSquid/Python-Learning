def main():
  hello();
  name = input("what's your name? ");
  hello(name);

def hello(to="world"): # def is to define a function
  print("hello,", to);


main(); # functions must be called to execute