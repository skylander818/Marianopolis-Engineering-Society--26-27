
x= ["bobo", "yellow", "red"]
def longest_string(x):
    i = 0
    value= 0
    while i< len(x):
        if len(x[i]) > value:
            value = len(x[i])
            y = x[i]
        i+=1
    return y
print(longest_string(x))