input_file = open("rainfall.txt", "r")
output_file = open("output.txt", "w")
for line in input_file:
    output_file.write(line)

input_file.close()
output_file.close()

with open("rainfall.txt") as f:
  print(f.read())

new_file = open("rainfall.txt")
print(new_file.readline())
new_file.close()

with open("demofile.txt", "a") as another_file:
  another_file.write("Now the file has more content!")
