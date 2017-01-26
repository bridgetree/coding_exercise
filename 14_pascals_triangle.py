row = [1]
k = [0]
for x in range(rowIndex):
  row = [l + r for l, r in zip(row + k, k + row)]
return row
