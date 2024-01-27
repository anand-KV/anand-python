#to write a program to merge two dictionaries
d1={1:'A',2:'B',3:'C',4:'D'}
d2={1:'A',5:'B',2:'C',6:'D'}
print("dictionary1:",d1)
print("dictionary2:",d2)
d1.update(d2)
print('after merging:',d1)
