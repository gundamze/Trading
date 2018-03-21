x = 1

"""_____________________________________________________________
                          Random Walk
"""

def randomWalk(T=10, period=1):
    """random walk with a fair coin"""
    import random
    x = 0
    answer= [[0,0]]
    for t in xrange(T+1):
        u = random.random()    # Return the next random floating point number in the range [0.0, 1.0).
        if (u<= 0.5): x+=1
        else:         x-=1
        if (t%period == 0 ) :
            answer.append([ t+1 , x ])
    return answer

x = randomWalk()
type(x)
type(x[0])


