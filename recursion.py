"""Recursion"""
def countdown(n):
	if n <= 0:
		print 'Bam!'
	else:
		print n 
		countdown(n-1)
"""			
	--- stack diagram --- 
                  ____________
module			 |  __main__  |
                  ------------ 
countdown   	 |	n  ->  3  |
                  ------------
countdown		 |	n  ->  2  |
                  ------------
countdown        |  n  ->  1  |
                  ------------
countdown        |  n  ->  0  |
                  ------------

"""

def print_n(str, n):
	if n <= 0:
		return
	print str
	print_n(str, n-1)

