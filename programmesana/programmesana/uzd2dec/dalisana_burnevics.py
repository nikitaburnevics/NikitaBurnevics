for i in range(41):

    if(i%2==0 and i%4==0): #noskaidro kuriem atlikums ir 0
        print(i, 'Dalos gan ar 2 gan ar 4')
    elif(i%2==0): #noskaidro kuriem atlikums ir 2
        print(i, 'Dalos ar 2')
    elif(i%4==0): #noskaidro kuriem atlikums ir 4
        print(i, 'Dalos ar 4')
    else:
        print(i) #izprintē pārējos