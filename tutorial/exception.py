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

#index out of range exception

try:
    items = [2, 4, 11]
    item = items[5]
    print("Item", item)
    pass
except Exception as e:
    print(e)
    pass
finally:
    print("end of index out of range exception handling")
    pass

#key values exceptions
try:
    dictionary = {
        3: "three",
        4: "four"
    }
    key = "10"
    value = dictionary.get(key)
    print("Value", value)
    pass
except Exception as e:
    print(e)
    pass
else:
    print("no exception were raised")
    pass
finally:
    print("end of key value exception handling")
    pass









