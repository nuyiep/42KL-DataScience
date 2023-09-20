
def ft_tqdm(lst: range) -> None:
    '''mimic the tqdm function'''
    for i in range(len(lst)+1):
        in_percentage = int(i/len(lst) * 100)
        bar_length = in_percentage/2*1.36
        space_length = 100/2*1.36 - bar_length
        print(f"\r{in_percentage}%|{int(bar_length) * '█'}{int(space_length) * ' '}|"
              + f" {i}/{len(lst)}", end='')
        yield i
