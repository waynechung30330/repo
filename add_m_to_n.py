# Add M to N
# Usage: add_m_to_n.py <Integer m> <Integer n>
# Now Status: Compeleted
import sys

m = sys.argv(1)
n = sys.argv(2)
sum = 0
for i in range(m, n):
	sum += i
print('Add '+ str(m)+ ' to '+ str(m) + ' is ' + str(sum))
