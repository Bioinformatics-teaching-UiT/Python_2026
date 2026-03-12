def my_function():
  print("Hello from a function")

my_function()

def name_function(fname):
  print(fname + " Refsnes")

name_function("Emil")
name_function("Tobias")

def my_full_name(*names):
  for name in names:
    print("My name is " + name)
  return names

name_list = my_full_name("Tobias", "Linus", "Emil")


