#to write a prgm that print no frm 1 to 20.for every multiple of 3,print
#'fizz',for every multiple 5,print 'buzz' and for every multiple of both 3&5
#print'fizz buzz',instd of org numbers
for i in range(1,21):
    if not i%3 and not i%5:
        print('fizz buzz\n',end='')
    elif not i%3:
        print('fizz\n',end='')
    elif not i%5:
        print('buzz\n',end='')
    else:
        print(i,end='')
