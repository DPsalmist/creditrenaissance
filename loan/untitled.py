###############
'''
A *lender* opens a *loan*. The loan has a tenure, principal, interest, total, week, group, status
'''

def lender(principal):
	amt = int(input('Enter your amount: '))
	tenure = int(input('Enter the tenure: '))
	int_rate = 10 / 100

	for i in range (1, tenure+1):
		interest = amt * int_rate
		tot_mont_repay = interest + mont_prin
		mont_prin = amt / tenure

		print('Total monthly Payment is: ', tot_mont_repay)
		print('Interest is: ', interest)
		print('Monthly Principal Payment is: ', mont_prin)