from random import randint
l1 = [0,0,0,0,0,0,0,0,0,0]
l2 = [1,1,1,1,1,1,1,1,1,1]

if __name__ == '__main__':

    if len(l1) == len(l2):
        print('it is right')
        l3 = [l1,l2]
        print(l3)
    else:
        print('it is a not right')
