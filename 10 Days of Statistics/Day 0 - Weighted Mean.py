#Day 0: Weighted Mean

def weightedMean(n, ar, wg):
    wglist=[a*b for a,b in zip(ar,wg)];
    return sum(wglist)/sum(wg);
        

n = int(input().strip());
ar = list(map(int, input().strip().split(' ')));
wg = list(map(int, input().strip().split(' ')));
result = weightedMean(n, ar, wg);

print("%.1f" % result);