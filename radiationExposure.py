def f(x):
    import math
    return 10 * math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
    the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
    between start and stop times.
    
    ex: 0, 5, 1 = 39.10; 5, 11, 1 = 22.94; 0, 11, 1 = 62.05; 
    40, 100, 1.5 = 0.43
    '''
    area = 0.0
    totalArea = 0.0
    if step == 0: return 0.0
    if stop <= start: return 0.0
    if step % 1 != 0:
        while start < stop:
            area = f(start) * step
            totalArea += area
            start += step 
        return totalArea
    
    for year in range(start, stop, step):
        area = f(year) * step
        totalArea += area

    return totalArea
    
print radiationExposure(5, 5, 1)
print radiationExposure(5, 11, 0)
print radiationExposure(0, 5, 1)
print radiationExposure(5, 11, 1)
print radiationExposure(0, 11, 1)
print radiationExposure(40, 100, 1.5)