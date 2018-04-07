def mean(n, ar): # self Documented
    return sum(ar)/n


def median(n, ar):
    sort_ar=sorted(ar); # Sort that list
    if not n%2==0 : # If not even lenght of list
        return sort_ar(n/2); # Return the exact middle value of the sorted list
    else:
        return (sort_ar[int(n/2)-1]+sort_ar[int(n/2)])/2; # else, compute the ceiling and floor of the median value index

    
def mode(n, ar):
    sort_ar=sorted(ar); # Sort list
    
    intfreq = []
    for w in sort_ar:
        intfreq.append(sort_ar.count(w)); # create list of occurences
        
    if len(set(intfreq))==1: # If cardinal of occurences, return lowest value
        return sort_ar[0];
    
    else: # Else, return most frequent value
        return max(set(sort_ar), key=sort_ar.count);

    
n = int(input().strip());
ar = list(map(int, input().strip().split(' ')));
result = mode(n, ar);
print(mean(n, ar), median(n, ar), mode(n, ar));