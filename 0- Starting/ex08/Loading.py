
def ft_tqdm(lst: range) -> None:
	'''mimic the tqdm function'''
	for i in range(len(lst)+1):
		in_percentage = int(i/len(lst) * 100)
		bar_length = in_percentage/2*1.36
		print(f"\r{in_percentage}%|{int(bar_length) * '█'}| {len(lst)}/{len(lst)}", end='')
		yield i
