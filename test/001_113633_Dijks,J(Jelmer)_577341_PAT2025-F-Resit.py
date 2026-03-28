
def balanced(s):
    # your code here
    
    
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    
    s = s.lower()
    vcount=0
    count=0
    for ch in s:
          if ch in s:
               v_count += 1
          elif ch in consonants:
               c_count += 1

    return v_count == c_count
 
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True



def firstPrime(n):
    # your code here
    candidate = n+1
    while True:
        if isPrime(candidate):
             return candidate
        candidate += 1
   
        
    

    
    

def alphabetical(list1):
    # your code here
    lower_list = [s.lower() for s in list1]
    return lower_list == sorted(lower_list)
        
  
def dinner(recipe, pantry):
    # your code here
    
            
    
def standings(path):
    #your code here
    max_points = -1
    best_team = ""
    with open(path,'r') as fp:
        for line in fp:
            team,points = line.strip().split()
            points = int(points)
        if points > max_points:
            max_points = points
            best_team = team
    return best_team
