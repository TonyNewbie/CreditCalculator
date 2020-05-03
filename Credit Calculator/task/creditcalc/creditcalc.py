import math
import argparse
import sys


def count_months(principal, payment, interest):
    nominal_interest = interest / 1200
    periods = math.ceil(math.log(payment / (payment - nominal_interest * principal), 1 + nominal_interest))
    years = periods // 12
    rest_month = periods % 12
    if years == 0:
        print(f'You need {rest_month} months to repay this credit!')
    elif rest_month == 0:
        print(f'You need {years} years to repay this credit!')
    else:
        print(f'Ypu need {years} years and {rest_month} months to repay this credit!')
    print(f'Overpayment = {payment * periods - principal}')


def count_monthly_payment(principal, periods, interest):
    nominal_interest = interest / 1200
    annuity_payment = principal \
        * (nominal_interest * pow(1 + nominal_interest, periods))\
        / (pow(1 + nominal_interest, periods) - 1)
    print(f'Your annuity payment = {math.ceil(annuity_payment)}!')
    print(f'Overpayment = {math.ceil(annuity_payment) * periods - principal}')


def count_credit_principal(payment, periods, interest):
    nominal_interest = interest / 1200
    principal = payment / ((nominal_interest * pow(1 + nominal_interest, periods))
                           / (pow(1 + nominal_interest, periods) - 1))
    print(f'Your credit principal = {math.floor(principal)}!')
    print(f'Overpayment = {math.ceil(payment) * periods - math.floor(principal)}')


def count_diff_payment(principal, periods, interests):
    nominal_interest = interests / 1200
    payments_amount = 0
    for period in range(1, periods + 1):
        diff_payment = math.ceil(principal / periods
                                 + nominal_interest * (principal - (principal * (period - 1)) / periods))
        payments_amount += diff_payment
        print(f'Month {period}: paid out {diff_payment}')
    print(f'Overpayment = {payments_amount - principal}')


parser = argparse.ArgumentParser()
parser.add_argument('--type', dest='type')
parser.add_argument('--payment', type=float, dest='payment')
parser.add_argument('--principal', type=int, dest='principal')
parser.add_argument('--periods', type=int, dest='periods')
parser.add_argument('--interest', type=float, dest='interest')
args = parser.parse_args()
if len(sys.argv) != 5:
    print('Incorrect parameters')
elif args.type == 'annuity':
    if not args.principal and not (args.payment < 0 or args.periods < 0 or args.interest < 0):
        count_credit_principal(args.payment, args.periods, args.interest)
    elif not args.payment and not (args.principal < 0 or args.periods < 0 or args.interest < 0):
        count_monthly_payment(args.principal, args.periods, args.interest)
    elif not args.periods and not (args.principal < 0 or args.payment < 0 or args.interest < 0):
        count_months(args.principal, args.payment, args.interest)
    else:
        print('Incorrect parameters')
elif args.type == 'diff':
    if args.payment or args.principal < 0 or args.periods < 0 or args.interest < 0:
        print('Incorrect parameters')
    else:
        count_diff_payment(args.principal, args.periods, args.interest)
else:
    print('Incorrect parameters')
