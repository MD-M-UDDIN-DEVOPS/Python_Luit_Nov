#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.



def split_and_join(line):
 
   # split the string on spaces
    line = line.split(" ")
    
    
    
    # join the list of strings using a hyphen as a separator
    return "-".join(line)

    
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)