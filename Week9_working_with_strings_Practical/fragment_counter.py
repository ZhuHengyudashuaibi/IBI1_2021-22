import re
seq='ATGCCATCGACTACGATCAATCGAGGGCC'
frag=re.findall(r'GAATTC',seq)
print('numbers =',len(frag)+1)
