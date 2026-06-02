blocks = "WBBWWBBWBW"
#0-9
def minimumRecolors(self, blocks, k):
    
    no_of_whites=0
    for i in range(k):
        if(blocks[i]=='W'):
            no_of_whites+=1
    min_whites=no_of_whites
    start=1
    end=k
    while(end<len(blocks)):
        if(blocks[start-1]=='W'):
            no_of_whites-=1
        if(blocks[end]=='W'):
            no_of_whites+=1
        min_whites=min(min_whites,no_of_whites)
        start+=1
        end+=1
    return min_whites

minimumRecolors(blocks=blocks,k=7)

