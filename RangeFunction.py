

def myRange(start,end=None,multiple=None):
    if end == None and multiple == None:
        accumulator = 0
        lst = [0]
        while accumulator != (start-1):
            accumulator += 1
            
            lst.append(accumulator)
        return lst

    elif multiple == None:
        lst = []
        while start != end:
            
            lst.append(start)
            start += 1
        return lst 
        
    else:
        if multiple > 0:
            lst = []
            while start != end:
                
                lst.append(start)
                start += 1
            lst1 = (lst[::multiple])
            return lst1
        elif multiple < 0:
            lst = []
            while start != end:
                
                lst.append(start)
                start -= 1
            
            
            return lst



if __name__ == '__myRange__':                                               
    print(__myRange__)
    myRange(10)
    


assert(myRange(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert(myRange(1, 10, 2) == [1, 3, 5, 7, 9])
assert(myRange(10, 1, -1) == [10, 9, 8, 7, 6, 5, 4, 3, 2])
assert(myRange(4,12,2) == [4, 6, 8, 10])


