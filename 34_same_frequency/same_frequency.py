def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_sorted = sorted([int(num) for a, num in enumerate(str(num1))])
    num2_sorted = sorted([int(num) for a, num in enumerate(str(num2))])
    if num1_sorted == num2_sorted:
        return True
    else:
        return False 