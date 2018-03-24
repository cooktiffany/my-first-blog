print("Hello, Django girls!")
if 3 > 2:
    print('It works!')

x = 2
y = 3
if x > y:
    print('x is indeed greater than y')
else:
    print('x is not greater than y')

name = 'Dave'
if name == 'Pete':
    print('Hey, Pete!')
elif name == 'Dave':
    print('Hey, Dave!')
else:
    print('Hey, you!')


def hi():
    print('Hi there!')
    print('How are you?')

hi()
def hi(name):
    if name == 'Dave':
        print('Hi, Dave!')
    elif name == 'Pete':
        print('Hi, PETE!')
    else:
        print('Hey!')

hi("Pete")
hi("Steve")

def hi(name):
    print('Hi, ' + name + '!')

hi("Leonard")

girls = ['Rachel', 'Monica', 'Phoebe', 'Patty', "Emily"]
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i + 1)
    
