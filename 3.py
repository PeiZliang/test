long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""


result = {
    'name': 'Variopartner SICAV',
    'lei': '529900LPCSV88817QH61',
    'sub_fund': []
}

lines = long_text.strip().split('\n')
sub_fund = {'title': None, 'isin': []}
for line in lines[2:]:
    if line.startswith('LU'):
        sub_fund['isin'].append(line)
    else:
        sub_fund = {'title': line, 'isin': []}

if sub_fund['title'] is not None:
    result['sub_fund'].append(sub_fund)

print(result)
