def search(list, number):
    objFound = False
    for num in list:
        if num == number:
          objFound = True;
    else:
        if objFound == True:
            print "Found it!"
        else:
            print "not found"
    
   

    
