fname = input("Enter file name: ")  # Input your text file that contain words that you want to count
opened = open(fname)                # opens the file specified in the 'fname' input
value = []                          # an empty list that will be populated later with strings of words from your text file
counts = dict()                     # an empty dictionary that will be later populated from element in value
for line in opened :                # use iteration variable 'line' to through string of words in opened (your text file)
    lineB = line.rstrip()           # go through the string contents in 'opened' and remove all newline blankspaces and then assign resolved string to 'lineB'   
    extract = lineB.split()         # splits value of 'lineB' into a lists and assign it to variable 'extract'
    value = value + extract         # make a list adition to populate the empty list 'value' that was defined above.

#Populating the above dictionary 'counts'
for cnt in value :                  # assign a variable 'cnt' to each element in the populated list 'value'  
    cnt = cnt.lower()               # convet all list elements to lower case letters  
    if cnt not in counts :          # go through 'counts' looking of values of 'cnt', but if not found, run below code. 
        counts[cnt] = 1             # assign 1 to any value of 'cnt' not found in 'counts'
    else :                          # while going through the 'counts' if values of 'cnt' is found, run below code
        counts[cnt] = counts[cnt] + 1  # make addition of 1 to any values of 'cnt' that is found.

# Populating a new list 'lst'     
lst = list()                        # define a new empty list as 'lst'
for k,v in counts.items():          # go through all items in dictionary 'counts', assign its key:value pair to k and v respectively. 
    npair = (k,v)                   # set the key:value pair to 'npair' (a tuple)
    lst.append(npair)               # append tuple values to 'lst' to populate it.  

# Sorting in alphabetical order the list of tuples which will show both counted words and number of occurrance 
lst = sorted(lst)
for a,b in lst:
    print(b,a)