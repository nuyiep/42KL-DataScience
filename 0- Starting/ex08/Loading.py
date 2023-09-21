
def ft_tqdm(lst: range) -> None:
    '''mimic the tqdm function'''
    for i in range(len(lst)+1):
        in_percentage = int(i/len(lst) * 100)
        bar_len = in_percentage/2*1.36
        space_len = 100/2*1.36 - bar_len
        print(f"\r{in_percentage}%|{int(bar_len) * '█'}{int(space_len) * ' '}|"
              + f" {i}/{len(lst)}", end='')
        yield i
