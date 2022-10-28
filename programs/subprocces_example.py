import subprocess


x = subprocess.call(["ls"])
print(x,"\n")

# You can store the output into a string! 
x = subprocess.check_output(["echo", "Hello World!"])
print(x,"\n")

files_list = subprocess.run(["ls", "-l"])
print("The exit code was: {}".format(files_list))
