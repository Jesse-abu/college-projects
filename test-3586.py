def exp_add(exps, cat, am):
    exps.append({'cat': cat, 'am':am})

def pri_exp(exps):
    for exp in exps:
        print(exp['cat'], exp['am'])

def exsp(exps):
	a = map(lambda exp : exp['am'], exps)
	print('total is: ', sum(a))

def filt(exps, cat):
    tr = filter(lambda exp : exp['cat'] == cat, exps)
    for zv in tr:
        print(zv)
        
def main():
    exps = []
    exp = dict()
    while True:
        print('\nExpense Tracker')
        print('1. Add')
        print('2. List all')
        print('3. Category')
        print('4. Expense total')
        print('5. Exit')
        
        choice = input('Pick ')
        if choice == '1':
            am = float(input('Amount> '))
            cat = input('category> ')
            exp_add(exps, cat, am)
            print('Added')
        elif choice == '2':
            print('\nAll Expenses')
            pri_exp(exps)
        elif choice == '3':
            cat = input('category> ')
            filt(exps, cat)
        elif choice == '4':
            exsp(exps)
        elif choice == '5':
            print('Exiting')
            break

        
if __name__ == '__main__':
    main()