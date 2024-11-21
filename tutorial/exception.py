#example of basic exception handling
try:
    filename = "myfile.txt"
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        print(line)
        pass
    pass
except FileNotFoundError:
    print("File not found")
    pass
except Exception as e:
    print(e)
else:
    print("no exception were raised")
    pass
finally:
    print("end of file exception hadnling")
    pass



