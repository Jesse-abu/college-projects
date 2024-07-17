def verify(ver):
    data = ''
    for item in ver:
        meta = str.maketrans({'+':'', '-':'', ' ':''})
        uni = item.translate(meta)
        data += uni
    return data.isalnum()

def summit(num):
    pass

def arith(problems, status=False):
    if verify(problems) == True:
        arranged_problems = ''
        fir = ''
        sec = ''
        line = ''
        ans = ''
        if len(problems) >= 5:
            return 'Error: Too many problems'
        else:
            num_add = [
            digit.split('+') if '+' in digit
            else '0'
            for digit in problems]
            print(num_add)
            num_sub = [
            digit.split('-') if '-' in digit
            else '0'
            for digit in problems]
            print(num_sub)
            alt = []
            k = 0
            for it in num_sub:
                if it == '0':
                    alt.append(num_add[k])
                k += 1
                for item in alt:
                    array = f'\n{item[0]}\n+{item[1]}'
                    if status == True:
                        array = f'\n{item[0]}\n{item[1]}\n{sum(item)}'
                arranged_problems += array
                if len(max(it).strip()) > 4:
                    return 'Error: Numbers cannot be more than four digits.'   
                elif status == True:
                    if len(it) > 1:
                        subit = int(it[0]) - int(it[1])
                        array = f'''
{it[0]}
-{it[1]}
----
{subit}
----'''
                        arranged_problems += array
                else:
                    if len(it) > 1:  
                        array = f'''
{it[0]}
-{it[1]}'''
                        arranged_problems += array
        return arranged_problems
    else:
        return "Error: Operator must be '+' or '-'."
tu = arith(['123 + 78', '3801 - 2', '900 + 23', '123 + 798'])

print(tu)
