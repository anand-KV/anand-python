#to write a program to create an inverted dictionary
d={1:"apple",2:"orange",3:"grapes",4:"apples",5:"kiwi"}
inve={v:k for k,v in d.items()}
print("original dictionary:")
print(d)
print("inverted dictionary:")
print(inve)
