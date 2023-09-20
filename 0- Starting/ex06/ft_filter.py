
def ft_filter(ft_function, ft_iterable) -> list:
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    if ft_function is None:
        return [word for word in ft_iterable if word]
    return [word for word in ft_iterable if ft_function(word)]
