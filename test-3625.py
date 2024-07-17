def verify(ver):
    data = ''
    for item in ver:
        meta = str.maketrans({'+':'', '-':'', ' ':''})
        rate = item.translate(meta)
        data += rate
    return data.isalnum()

def verify2(ver, ver2):
    val_i = map(lambda x : (x.strip()).isdigit(), ver)
    val_o = map(lambda x : (x.strip()).isdigit(), ver2) 
    data = 0
    for item in val_i:
        data += item
    for item in val_o:
        data += item
    return data

def verify3(ver, ver2):
    use = ''
    use_2 = ''
    rate = 0
    for item in ver:
        if len(item.strip()) > 4:
            use = item.strip()
    for item in ver2:
        if len(item.strip()) > 4:
            use_2 = item.strip()
    if len(use) > 4:
        rate += 1
    if len(use_2) > 4:
        rate += 1
    return rate == 0

def arith(problems, status=False):
    if verify(problems) == True:
        arranged_problems = ''
        operand = []
        fir = []
        sec = []
        ans = []
        line = []
        meta = str.maketrans({'+':'_', '-':'_', ' ':''})
        if len(problems) >= 5:
            return 'Error: Too many problems'
        else:
            for char in problems:
                rot = char.translate(meta)
                rate = rot.split('_')
                fir.append(f'{rate[0]}    ')
                sec.append(f'{rate[1]}    ')
                if '+' in char:
                    operand.append('+')
                    try:
                        ans.append(f'{int(rate[0]) + int(rate[1])}    ')
                    except:
                        ans.append(0)
                if '-' in char:
                    operand.append('-')
                    try:
                        ans.append(f'{int(rate[0]) - int(rate[1])}    ')
                    except:
                        ans.append(0)
        if verify3(fir, sec) == True:
            if verify2(fir, sec) == (len(fir) + len(sec)):
                start = 0
                fir_line = ''
                sec_line = ''
                thr_line = ''
                end_line = ''
                for frame in ans:
                    if frame == 0:
                        pass
                    else:
                        line.append('----  ')
                if len(line) == len(ans):
                    while start < len(line):
                        fir_line += f'{fir[start]}'
                        sec_line += f'{operand[start]}{sec[start]}'
                        thr_line += f'{line[start]}'
                        end_line += f'{ans[start]}'
                        start += 1
                    if status == False:
                        arranged_problems = f'{fir_line}\n{sec_line}\n{thr_line}'
                        return arranged_problems
                    if status == True:
                        arranged_problems = f'{fir_line}\n{sec_line}\n{thr_line}\n{end_line}'
                        return arranged_problems
            else:
                return 'Error: Must contain digits'
        else:
            return 'Error: Number should not be more than four digits'
    else:
            return "Error: Operator must be '+' or '-'."

print(arith(['344 + 65', '76 - 9847']))

