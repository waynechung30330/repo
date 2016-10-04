# Add M to N
# Usage: add_m_to_n.py <Integer m> <Integer n>
# Now Status: Compeleted

import sys

def _sum(m, n):
        if n==m:
		return m
	else:
		return n + _sum(m, n-1)


m = sys.argv(1)
n = sys.argv(2)

print('Add '+ str(m)+ ' to '+ str(n) + ' is ' + str(_sum(m, n)))
