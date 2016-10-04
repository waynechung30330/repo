# Add M to N
# Usage: add_m_to_n.py <Integer m> <Integer n>
# Now Status: Only compelet add one to n
import sys

sum = 0
for i in range(1,sys.argv(1)+1):
	sum += i
print('Add 1 to '+ str(sys.argv(1)) + ' is ' + str(sum))
