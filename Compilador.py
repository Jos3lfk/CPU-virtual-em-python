import sys

with open("C:\\CPU Rita e Tomas\\C.c", "r") as arquivo:
    codigoc = arquivo.read()

localarquivo = 'C:\\CPU Rita e Tomas\\assembly.txt'


def syntax_error(a):
    sys.exit(f"Syntax error!\nSyntax error: {a}")


def dec_bin_int(decimal):
    if '.' in decimal:
        g1 = ''
        g2 = ''
        for i in range(len(decimal)):
            if decimal[i] == '.':
                for j in range(len(decimal)):
                    if j < i:
                        g1 += decimal[j]
                    elif j > i:
                        g2 += decimal[j]
        g2 = dec_bin_int(g2)
        g2[0] = '00' + g2[0]
        b = dec_bin_int(g1) + g2
        return b
    else:
        decimal = int(decimal)
        if decimal < 0:
            decimal = -decimal
            guardar = -1
        else:
            guardar = 1
        binario = ''
        if decimal != 0:
            while decimal > 0:
                binario += str(decimal % 2)
                decimal //= 2
            a = binario[:: -1]
        else:
            a ='0'

        if len(a) % 5 != 0:
            if len(a) % 5 == 1:
                a = '0000' + a
            elif len(a) % 5 == 2:
                a = '000' + a
            elif len(a) % 5 == 3:
                a = '00' + a
            elif len(a) % 5 == 4:
                a = '0' + a

        b = []
        c = ''
        for i in range(len(a)):
            c += a[i]
            if (i + 1) % 5 == 0:
                b.append(c)
                c = ''
        if len(b) < 4:
            d = b
            for i in range(len(d)):
                if len(d[i]) < 5:
                    if len(d[i]) == 1:
                        d[i] = '0000' + d[i]
                    if len(d[i]) == 2:
                        d[i] = '000' + d[i]
                    if len(d[i]) == 3:
                        d[i] = '00' + d[i]
                    if len(d[i]) == 4:
                        d[i] = '0' + d[i]
            if len(b) == 1:
                b = [
                    '00000',
                    '00000',
                    '00000',
                    d[0]
                ]
            if len(b) == 2:
                b = [
                    '00000',
                    '00000',
                    d[0],
                    d[1]
                ]
            elif len(b) == 3:
                b = [
                    '00000',
                    d[0],
                    d[1],
                    d[2],
                ]

        if len(b) > 4:
            sys.exit('ERROR: value is too long for "int" type')
        if guardar >= 0 and b[0] != '1':
            b[0] = '0' + b[0]
        elif guardar >= 0 and b[0] == '1':
            for i in range(len(b)):
                if i < len(b) - 1:
                    b[i] = b[i + 1]
                else:
                    b[i] = ''
            b[0] = '0' + b[0]
        elif guardar <= 0 and b[0] != '1':
            b[0] = '1' + b[0]
        elif guardar <= 0 and b[0] == '1':
            for i in range(len(b)):
                if i < len(b) - 1:
                    b[i] = b[i + 1]
                else:
                    b[i] = ''
            b[0] = '1' + b[1]
        return b

with open(localarquivo, "w") as asbly:
    asbly = asbly
if 'int main() ' or 'int main(void) ' in codigoc:
    print()
else:
    syntax_error('Expected "main" function')

memory = 0
comp = codigoc.split()
valor = 0
controle = -1
varc_asbly = {}
varm_asbly = {}
art = 0
guarda = 0
L = 0

for i in range(len(comp)):
    for j in range(len(comp)):
        if j <= i:
            if i != controle:
                if comp[i] == 'int':
                    if '()' in comp[i + 1] or '()' in comp[i + 2]:
                        if comp[i + 2] == '{':
                            with open(localarquivo, "a") as asbly:
                                asbly.write('main:\n')
                                valor = 0
                        else:
                            syntax_error('expected "{" expression after "main" function')
                    else:
                        if comp[i + 2] == '=':
                            if ';' in comp[i + 3]:
                                for l in comp[i + 3]:
                                    if l == ';':
                                        guarda = comp[i + 3].replace(l, '')
                                valor = guarda
                                with open(localarquivo, "a") as asbly:
                                    asbly.write(f'  store {valor} to {memory} size 4\n')
                                    varc_asbly[comp[i + 1]] = f"{valor}"
                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                    memory = memory + 4
                                    valor = 0
                            else:
                                for k in range(len(comp)):
                                    for p in range(len(comp)):
                                        if comp[k] == '+' or comp[k] == '-' or comp[k] == '*' or comp[k] == '/' and k > i:
                                            if '1' in comp[k + 1] or '2' in comp[k + 1] or '3' in comp[k + 1] or '4' in comp[k + 1] or '5' in comp[k + 1] or '6' in comp[k + 1] or '7' in comp[k + 1] or '8' in comp[k + 1] or '9' in comp[k + 1] or '0' in comp[k + 1]:
                                                if '1' in comp[k - 1] or '2' in comp[k - 1] or '3' in comp[k - 1] or '4' in comp[k - 1] or '5' in comp[k - 1] or '6' in comp[k - 1] or '7' in comp[k - 1] or '8' in comp[k - 1] or '9' in comp[k - 1] or '0' in comp[k - 1]:
                                                    if comp[k] == '+':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  add {guarda} r1\n  store r1 to {memory}  size 4\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  add {guarda} r1\n  store r1 to {memory} size 4\n')
                                                                    varc_asbly[comp[i]] = f"{int(valor) + int(guarda)}"
                                                                    varm_asbly[comp[i]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  add {comp[k + 1]} r1\n')
                                                                        controlei = int(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{int(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 4
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break
                                                    elif comp[k] == '-':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  sub {guarda} r1\n  store r1 to {memory} size 4\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  sub {guarda} r1\n  store r1 to {memory} size 4\n')
                                                                    varc_asbly[comp[i]] = f"{int(valor) + int(guarda)}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  sub {comp[k + 1]} r1\n')
                                                                        controlei = int(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{int(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 4
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break
                                                    elif comp[k] == '*':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  mul {guarda} r1\n  store r1 to {memory} size 4\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  mul {guarda} r1\n  store r1 to {memory} size 4\n')
                                                                    varc_asbly[comp[i + 1]] = f"{int(valor) + int(guarda)}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  mul {comp[k + 1]} r1\n')
                                                                        controlei = int(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{int(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 4
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break
                                                    elif comp[k] == '/':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  div {guarda} r1\n  store r1 to {memory} size 4\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  div {guarda} r1\n  store r1 to {memory} size 4\n')
                                                                    varc_asbly[comp[i + 1]] = f"{int(valor) + int(guarda)}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 4
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  div {comp[k + 1]} r1\n')
                                                                        controlei = int(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{int(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 4
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break

                                            else:
                                                if ('1' in comp[k - 1] or '2' in comp[k - 1] or '3' in comp[k - 1] or '4' in comp[k - 1] or '5' in comp[k - 1] or '6' in comp[k - 1] or '7' in comp[k - 1] or '8' in comp[k - 1] or '9' in comp[k - 1] or '0' in comp[k - 1]) and ';' not in comp[k - 1]:
                                                    with open(localarquivo, "a") as asbly:
                                                        for l in varc_asbly:
                                                            if l == comp[k + 1]:
                                                                controle_valor = int(varc_asbly.get(l))
                                                        valor = int(comp[k - 1]) + controle_valor
                                                        asbly.write(f'  store {valor} to {memory} size 4\n')
                                                        varc_asbly[comp[i + 1]] = f"{valor}"
                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                        memory = memory + 4
                                                        valor = 0
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  store {valor} to {memory} size 4\n')
                                                            varc_asbly[comp[i + 1]] = f"{valor}"
                                                            varm_asbly[comp[i + 1]] = f"{memory}"
                                                            memory = memory + 4
                                                            valor = 0
                                                else:
                                                    valor = comp[i + 3]
                                                    with open(localarquivo, "a") as asbly:
                                                        asbly.write(f'  store {valor} to {memory} size 4\n')
                                                        varc_asbly[comp[i + 1]] = f"{valor}"
                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                        memory = memory + 4
                                                        valor = 0
                                        if ';' in comp[i]:
                                            break
                if comp[i] == 'float':
                    if '()' in comp[i + 1] or '()' in comp[i + 2]:
                        if comp[i + 2] == '{':
                            with open(localarquivo, "a") as asbly:
                                asbly.write('main:\n')
                                valor = 0
                        else:
                            syntax_error('expected "{" expression after a function')
                    else:
                        if comp[i + 2] == '=':
                            if ';' in comp[i + 3]:
                                for l in comp[i + 3]:
                                    if l == ';':
                                        guarda = comp[i + 3].replace(l, '')
                                valor = guarda
                                with open(localarquivo, "a") as asbly:
                                    asbly.write(f'  store {valor} to {memory} size 4\n')
                                    varc_asbly[comp[i + 1]] = f"{valor}"
                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                    memory = memory + 8
                                    valor = 0
                            else:
                                for k in range(len(comp)):
                                    for p in range(len(comp)):
                                        if comp[k] == '+' or comp[k] == '-' or comp[k] == '*' or comp[k] == '/' and k > i:
                                            if '1' in comp[k + 1] or '2' in comp[k + 1] or '3' in comp[k + 1] or '4' in comp[k + 1] or '5' in comp[k + 1] or '6' in comp[k + 1] or '7' in comp[k + 1] or '8' in comp[k + 1] or '9' in comp[k + 1] or '0' in comp[k + 1]:
                                                if '1' in comp[k - 1] or '2' in comp[k - 1] or '3' in comp[k - 1] or '4' in comp[k - 1] or '5' in comp[k - 1] or '6' in comp[k - 1] or '7' in comp[k - 1] or '8' in comp[k - 1] or '9' in comp[k - 1] or '0' in comp[k - 1]:
                                                    if comp[k] == '+':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  add {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  add {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{float(valor) + float(guarda)}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  add {comp[k + 1]} r1\n')
                                                                        controlei = float(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{float(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 8
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break
                                                    elif comp[k] == '-':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  sub {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    memory = memory + 8
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  sub {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{float(valor) + float(guarda)}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  sub {comp[k + 1]} r1\n')
                                                                        controlei = float(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{float(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 8
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break
                                                    elif comp[k] == '*':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  mul {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  mul {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{float(valor) + float(guarda)}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  mul {comp[k + 1]} r1\n')
                                                                        controlei = float(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{float(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 8
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break
                                                    elif comp[k] == '/':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  div {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  div {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{float(valor) + float(guarda)}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  div {comp[k + 1]} r1\n')
                                                                        controlei = float(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{float(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 8
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break

                                            else:
                                                if '1' in comp[k - 1] or '2' in comp[k - 1] or '3' in comp[k - 1] or '4' in comp[k - 1] or '5' in comp[k - 1] or '6' in comp[k - 1] or '7' in comp[k - 1] or '8' in comp[k - 1] or '9' in comp[k - 1] or '0' in comp[k - 1]:
                                                    with open(localarquivo, "a") as asbly:
                                                        for l in varc_asbly:
                                                            if l == comp[k + 1]:
                                                                controle_valor = float(varc_asbly.get(l))
                                                        valor = float(comp[k - 1]) + controle_valor
                                                        asbly.write(f'  store {valor} to {memory} size 4\n')
                                                        varc_asbly[comp[i + 1]] = f"{valor}"
                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                        memory = memory + 8
                                                        valor = 0
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  store {valor} to {memory} size 4\n')
                                                            varc_asbly[comp[i + 1]] = f"{valor}"
                                                            varm_asbly[comp[i + 1]] = f"{memory}"
                                                            memory = memory + 8
                                                            valor = 0
                                                else:
                                                    valor = comp[i + 3]
                                                    with open(localarquivo, "a") as asbly:
                                                        asbly.write(f'  store {valor} to {memory} size 4\n')
                                                        varc_asbly[comp[i + 1]] = f"{valor}"
                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                        memory = memory + 8
                                                        valor = 0
                if comp[i] == 'double':
                    if '()' in comp[i + 1] or '()' in comp[i + 2]:
                        if comp[i + 2] == '{':
                            with open(localarquivo, "a") as asbly:
                                asbly.write('main:\n')
                                valor = 0
                        else:
                            syntax_error('expected "{" expression after a function')
                    else:
                        if comp[i + 2] == '=':
                            if ';' in comp[i + 3]:
                                valor = comp[i + 3]
                                for l in comp[i + 3]:
                                    if l == ';':
                                        guarda = comp[i + 3].replace(l, '')
                                        valor = guarda
                                with open(localarquivo, "a") as asbly:
                                    asbly.write(f'  store {valor} to {memory} size 8\n')
                                    varc_asbly[comp[i + 1]] = f"{valor}"
                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                    memory = memory + 8
                                    valor = 0
                            else:
                                for k in range(len(comp)):
                                    for p in range(len(comp)):
                                        if comp[k] == '+' or comp[k] == '-' or comp[k] == '*' or comp[k] == '/' and k > i:
                                            if '1' in comp[k + 1] or '2' in comp[k + 1] or '3' in comp[k + 1] or '4' in comp[k + 1] or '5' in comp[k + 1] or '6' in comp[k + 1] or '7' in comp[k + 1] or '8' in comp[k + 1] or '9' in comp[k + 1] or '0' in comp[k + 1]:
                                                if '1' in comp[k - 1] or '2' in comp[k - 1] or '3' in comp[k - 1] or '4' in comp[k - 1] or '5' in comp[k - 1] or '6' in comp[k - 1] or '7' in comp[k - 1] or '8' in comp[k - 1] or '9' in comp[k - 1] or '0' in comp[k - 1]:
                                                    if comp[k] == '+':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  add {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  add {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{float(valor) + float(guarda)}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  add {comp[k + 1]} r1\n')
                                                                        controlei = float(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{float(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 8
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break
                                                    elif comp[k] == '-':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  sub {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + guarda
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  sub {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{float(valor) + float(guarda)}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  sub {comp[k + 1]} r1\n')
                                                                        controlei = float(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{float(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 8
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break
                                                    elif comp[k] == '*':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  mul {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + guarda
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = comp[k - 1] + comp[k + 1]
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(';', '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  mul {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{float(valor) + float(guarda)}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  mul {comp[k + 1]} r1\n')
                                                                        controlei = float(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{float(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 8
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break
                                                    elif comp[k] == '/':
                                                        if art == 0:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n  div {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[guarda] = f"{comp[k - 1] + guarda}"
                                                                    varm_asbly[guarda] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = float(comp[k - 1] + guarda)
                                                                break
                                                            else:
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  load {comp[k - 1]} r1\n')
                                                                    varc_asbly[comp[i + 1]] = f"{comp[k - 1] + comp[k + 1]}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = float(comp[k - 1] + comp[k + 1])
                                                                    art = art + 1
                                                        else:
                                                            if ';' in comp[k + 1]:
                                                                for l in comp[k + 1]:
                                                                    if l == ';':
                                                                        guarda = comp[k + 1].replace(l, '')
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  div {guarda} r1\n  store r1 to {memory}\n')
                                                                    varc_asbly[comp[i + 1]] = f"{float(valor) + float(guarda)}"
                                                                    varm_asbly[comp[i + 1]] = f"{memory}"
                                                                    memory = memory + 8
                                                                    valor = 0
                                                                    art = 0
                                                                break
                                                            else:
                                                                if comp[k - 1] != '=':
                                                                    with open(localarquivo, "a") as asbly:
                                                                        asbly.write(f'  div {comp[k + 1]} r1\n')
                                                                        controlei = float(comp[k + 1])
                                                                        varc_asbly[comp[i + 1]] = f"{float(valor) + controlei}"
                                                                        varm_asbly[comp[i + 1]] = f"{memory}"
                                                                        memory = memory + 8
                                                                        art = art + 1
                                                                        valor = 0
                                                                    break

                                                else:
                                                    if '1' in comp[k - 1] or '2' in comp[k - 1] or '3' in comp[k - 1] or '4' in comp[k - 1] or '5' in comp[k - 1] or '6' in comp[k - 1] or '7' in comp[k - 1] or '8' in comp[k - 1] or '9' in comp[k - 1] or '0' in comp[k - 1]:
                                                        with open(localarquivo, "a") as asbly:
                                                            for l in varc_asbly:
                                                                if l == comp[k + 1]:
                                                                    controle_valor = int(varc_asbly.get(l))
                                                            valor = float(comp[k - 1]) + controle_valor
                                                            asbly.write(f'  store {valor} to {memory} size 8\n')
                                                            varc_asbly[comp[i + 1]] = f"{valor}"
                                                            varm_asbly[comp[i + 1]] = f"{memory}"
                                                            memory = memory + 8
                                                            valor = 0
                                                            with open(localarquivo, "a") as asbly:
                                                                asbly.write(f'  store {valor} to {memory} size 8\n')
                                                                varc_asbly[comp[i + 1]] = f"{valor}"
                                                                varm_asbly[comp[i + 1]] = f"{memory}"
                                                                memory = memory + 8
                                                                valor = 0
                                                    else:
                                                        valor = comp[i + 3]
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  store {valor} to {memory} size 4\n')
                                                            varc_asbly[comp[i + 1]] = f"{valor}"
                                                            varm_asbly[comp[i + 1]] = f"{memory}"
                                                            memory = memory + 8
                                                            valor = 0
                                            if ';' in comp[i]:
                                                break


                if (comp[i] in varc_asbly or comp[i].replace(';', '') in varc_asbly or comp[i].replace('++', '').replace(';', '') in varc_asbly or comp[i].replace('--', '').replace(';', '') in varc_asbly) and comp[i - 1] != 'int' and comp[i - 1] != 'float' and comp[i - 1] != 'double':
                    if ';' in comp[i] and '++' in comp[i]:
                        valor = varm_asbly[comp[i].replace('++', '').replace(';', '')]
                    elif ';' in comp[i] and '--' in comp[i]:
                        valor = varm_asbly[comp[i].replace('--', '').replace(';', '')]
                    elif ';' in comp[i]:
                        valor = varm_asbly[comp[i].replace(';', '')]
                    else:
                        valor = varm_asbly[comp[i]]
                    if '=' in comp[i + 1]:
                        guardar = varm_asbly[comp[i]]
                    if '+' in comp[i - 1] or '-' in comp[i - 1] or '*' in comp[i - 1] or '/' in comp[i - 1] or '=' in comp[i - 1]:
                        if comp[i - 2] in varm_asbly:
                            if '=' in comp[i - 1]:
                                if ';' in comp[i]:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  load ${varm_asbly[comp[i].replace(";", "")]} r1\n  store r1 to {varm_asbly[comp[i - 2]]}\n')
                                else:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  load ${varm_asbly[comp[i]].replace(";", "")} r1\n')
                            if '+' in comp[i - 1]:
                                if ';' in comp[i]:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  add ${varm_asbly[comp[i].replace(";", "")]} r1\n  store r1 to {guardar}\n')
                                else:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  add ${varm_asbly[comp[i].replace(";", "")]} r1\n')
                            if '-' in comp[i - 1]:
                                if ';' in comp[i]:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  sub ${varm_asbly[comp[i].replace(";", "")]} r1\n  store r1 to {guardar}\n')
                                else:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  sub ${varm_asbly[comp[i].replace(";", "")]} r1\n')
                            if '*' in comp[i - 1]:
                                if ';' in comp[i]:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  mul ${varm_asbly[comp[i].replace(";", "")]} r1\n  store r1 to {guardar}\n')
                                else:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  mul ${varm_asbly[comp[i].replace(";", "")]} r1\n')
                            if '/' in comp[i - 1]:
                                if ';' in comp[i]:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  div ${varm_asbly[comp[i].replace(";", "")]} r1\n  store r1 to {guardar}\n')
                                else:
                                    with open(localarquivo, "a") as asbly:
                                        asbly.write(f'  div ${varm_asbly[comp[i].replace(";", "")]} r1\n')
                    if '++' in comp[i + 1] or '++' in comp[i]:
                        with open(localarquivo, "a") as asbly:
                            valor = varm_asbly[(comp[i].replace("++", "")).replace(";", "")]
                            asbly.write(f'  load ${valor}\n  inc r1\n  store r1 to {valor}\n')
                            valor = 0
                    elif '--' in comp[i + 1] or '--' in comp[i]:
                        with open(localarquivo, "a") as asbly:
                            asbly.write(f'  load ${valor}\n  dec r1\n  store r1 to {varm_asbly[comp[i].replace("--", "").replace(";", "")]}\n')
                            valor = 0
                    if '=' in comp[i + 1]:
                        art = 0
                        for k in range(len(comp)):
                            for p in range(len(comp)):
                                if k > i + 1:
                                    if comp[k] == '+' or comp[k] == '-' or comp[k] == '*' or comp[k] == '/' and k > i:
                                        if '1' in comp[k + 1] or '2' in comp[k + 1] or '3' in comp[k + 1] or '4' in comp[k + 1] or '5' in comp[k + 1] or '6' in comp[k + 1] or '7' in comp[k + 1] or '8' in comp[k + 1] or '9' in comp[k + 1] or '0' in comp[k + 1]:
                                            if '1' in comp[k - 1] or '2' in comp[k - 1] or '3' in comp[k - 1] or '4' in comp[k - 1] or '5' in comp[k - 1] or '6' in comp[k - 1] or '7' in comp[k - 1] or '8' in comp[k - 1] or '9' in comp[k - 1] or '0' in comp[k - 1]:
                                                if comp[k] == '+':
                                                    if art == 0:
                                                        if ';' in comp[k + 1]:
                                                            for l in comp[k + 1]:
                                                                if l == ';':
                                                                    guarda = comp[k + 1].replace(l, '')
                                                            with open(localarquivo, "a") as asbly:
                                                                asbly.write(f'  load {comp[k - 1]} r1\n  add {guarda} r1\n  store r1 to {memory}\n')
                                                                valor = comp[k - 1] + guarda
                                                                art = 0
                                                            break
                                                        else:
                                                            with open(localarquivo, "a") as asbly:
                                                                asbly.write(f'  load {comp[k - 1]} r1\n  add {comp[k + 1]} r1\n')
                                                                valor = comp[k - 1] + comp[k + 1]
                                                                art = art + 1
                                                    else:
                                                        if ';' in comp[k + 1]:
                                                            for l in comp[k + 1]:
                                                                if l == ';':
                                                                    guarda = comp[k + 1].replace(l, '')
                                                            with open(localarquivo, "a") as asbly:
                                                                asbly.write(f'  add {guarda} r1\n  store r1 to {memory}\n')
                                                                valor = 0
                                                                art = 0
                                                            break
                                                        else:
                                                            if comp[k - 1] != '=':
                                                                with open(localarquivo, "a") as asbly:
                                                                    asbly.write(f'  add {comp[k + 1]} r1\n')
                                                                    controlei = float(comp[k + 1])
                                                                    art = art + 1
                                                                    valor = 0
                                                                break
                                                elif comp[k] == '-':
                                                    if art == 0:
                                                        if ';' in comp[k + 1]:
                                                            for l in comp[k + 1]:
                                                                if l == ';':
                                                                    guarda = comp[k + 1].replace(l, '')
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  load {comp[k - 1]} r1\n  sub {guarda} r1\n  store r1 to {memory}\n')
                                                            valor = comp[k - 1] + guarda
                                                        break
                                                    else:
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  load {comp[k - 1]} r1\n')
                                                            valor = comp[k - 1] + comp[k + 1]
                                                            art = art + 1
                                                else:
                                                    if ';' in comp[k + 1]:
                                                        for l in comp[k + 1]:
                                                            if l == ';':
                                                                guarda = comp[k + 1].replace(l, '')
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  sub {guarda} r1\n  store r1 to {memory}\n')
                                                            valor = 0
                                                            art = 0
                                                        break
                                                    else:
                                                        if comp[k - 1] != '=':
                                                            with open(localarquivo, "a") as asbly:
                                                                asbly.write(f'  sub {comp[k + 1]} r1\n')
                                                                controlei = float(comp[k + 1])
                                                                art = art + 1
                                                                valor = 0
                                                            break
                                            elif comp[k] == '*':
                                                if art == 0:
                                                    if ';' in comp[k + 1]:
                                                        for l in comp[k + 1]:
                                                            if l == ';':
                                                                guarda = comp[k + 1].replace(l, '')
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  load {comp[k - 1]} r1\n  mul {guarda} r1\n  store r1 to {memory}\n')
                                                            valor = comp[k - 1] + guarda
                                                        break
                                                    else:
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  load {comp[k - 1]} r1\n')
                                                            valor = comp[k - 1] + comp[k + 1]
                                                            art = art + 1
                                                else:
                                                    if ';' in comp[k + 1]:
                                                        for l in comp[k + 1]:
                                                            if l == ';':
                                                                guarda = comp[k + 1].replace(l, '')
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  mul {guarda} r1\n  store r1 to {memory}\n')
                                                            valor = 0
                                                            art = 0
                                                        break
                                                    else:
                                                        if comp[k - 1] != '=':
                                                            with open(localarquivo, "a") as asbly:
                                                                asbly.write(f'  mul {comp[k + 1]} r1\n')
                                                                controlei = float(comp[k + 1])
                                                                art = art + 1
                                                                valor = 0
                                                            break
                                            elif comp[k] == '/':
                                                if art == 0:
                                                    if ';' in comp[k + 1]:
                                                        for l in comp[k + 1]:
                                                            if l == ';':
                                                                guarda = comp[k + 1].replace(l, '')
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  load {comp[k - 1]} r1\n  div {guarda} r1\n  store r1 to {memory}\n')
                                                            valor = comp[k - 1] + guarda
                                                        break
                                                    else:
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  load {comp[k - 1]} r1\n')
                                                            valor = comp[k - 1] + comp[k + 1]
                                                            art = art + 1
                                                else:
                                                    if ';' in comp[k + 1]:
                                                        for l in comp[k + 1]:
                                                            if l == ';':
                                                                guarda = comp[k + 1].replace(l, '')
                                                        with open(localarquivo, "a") as asbly:
                                                            asbly.write(f'  div {guarda} r1\n  store r1 to {memory}\n')
                                                            valor = 0
                                                            art = 0
                                                        break
                                                    else:
                                                        if comp[k - 1] != '=':
                                                            with open(localarquivo, "a") as asbly:
                                                                asbly.write(f'  div {comp[k + 1]} r1\n')
                                                                controlei = float(comp[k + 1])
                                                                art = art + 1
                                                                valor = 0
                                                            break
                    if ';' in comp[i]:
                        for k in comp[i]:
                            guarda = comp[i].replace(';', '')

                    if comp[i + 1] == '=':
                        if comp[i + 2] == '+' or comp[i + 2] == '-' or comp[i + 2] == '*' or comp[i + 2] == '/':
                            if ';' in comp[i]:
                                break
                if comp[i] == 'if':
                    if '(' in comp[i + 1]:
                        with open(localarquivo, "a") as asbly:
                            asbly.write(f'  load ${varm_asbly[comp[i + 1].replace("(", "")]} r2\n')
                        if ')' in comp[i + 3]:
                            with open(localarquivo, "a") as asbly:
                                asbly.write(f'  load ${varm_asbly[comp[i + 3].replace(")", "").replace("{", "")]} r3\n')
                        if '==' in comp[i + 2]:
                            with open(localarquivo, "a") as asbly:
                                asbly.write(f'  beq r2 r3\nL{L}:\n')
                                L = L + 1
                        elif '<' in comp[i + 2]:
                            with open(localarquivo, "a") as asbly:
                                asbly.write(f'  blt r2 r3\nL{L}:\n')
                                L = L + 1
                        elif '<=' in comp[i + 2]:
                            with open(localarquivo, "a") as asbly:
                                asbly.write(f'  ble r2 r3\nL{L}:\n')
                                L = L + 1
                        elif '>' in comp[i + 2]:
                            with open(localarquivo, "a") as asbly:
                                asbly.write(f'  bge r1 r3\nL{L}:\n')
                                L = L + 1
                        elif '>=' in comp[i + 2]:
                            with open(localarquivo, "a") as asbly:
                                asbly.write(f'  bgt r2 r3\nL{L}:\n')
                                L = L + 1
                        elif '!=' in comp[i + 2]:
                            with open(localarquivo, "a") as asbly:
                                asbly.write(f'  bne r2 r3\nL{L}:\n')
                                L = L + 1
                if '{' in comp[i]:
                    with open(localarquivo, "a") as asbly:
                        asbly.write(f'  push\n')
                if '}' in comp[i]:
                    with open(localarquivo, "a") as asbly:
                        asbly.write(f'  pop\n\n')
        controle = i
        if ';' in comp[i]:
            break

with open(localarquivo, "r") as asbly:
    print(asbly.read())

with open('C:\\CPU Rita e Tomas\\binario.txt', 'w') as bin:
    bin = bin

with open(localarquivo, 'r') as asbly:
    asbly = asbly.read()
    asbly = asbly.split()

for i in range(len(asbly)):
    if asbly[i] == 'main:':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0000110\n')

    if asbly[i] == 'store':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0100000\n')
            if asbly[i + 1] == 'r1':
                a = ''
            elif '$' in asbly[i + 1]:
                a = ''
            else:
                guardar = dec_bin_int(asbly[i + 1])
                for j in guardar:
                    bin.write(f'{j}\n')

    if asbly[i] == 'r1':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0001001\n')

    if asbly[i] == 'r2':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0001010\n')

    if asbly[i] == 'r3':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0001011\n')

    if '$' in asbly[i]:
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0010010\n')
            auxi = dec_bin_int(asbly[i].replace('$', ''))
            for j in auxi:
                bin.write(f'{j}\n')

    if asbly[i] == 'to':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0010000\n')
            guardar = dec_bin_int(asbly[i + 1])
            for i in range(len(guardar)):
                bin.write(f'{guardar[i]}\n')

    if asbly[i] == 'size':
        if asbly[i + 1] == '4':
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                bin.write('0010001\n')
                guardar = dec_bin_int('4')
                for j in guardar:
                    bin.write(f'{j}\n')
        elif asbly[i + 1] == '8':
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                bin.write('0010000\n')
                guardar = dec_bin_int('8')
                for j in guardar:
                    bin.write(f'{j}\n')

    if asbly[i] == 'load':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0100010\n')
        if '$' in asbly[i + 1]:
            z = ''
        else:
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                a = dec_bin_int(asbly[i + 1])
                for j in a:
                    bin.write(f'{j}\n')

    if asbly[i] == 'mov':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0100100\n')

    if asbly[i] == 'jump':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0100110\n')

    if asbly[i] == 'add':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1000000\n')
        if '$' in asbly[i + 1]:
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                bin.write('0010010\n')
                a = dec_bin_int(asbly[i + 1].replace('$', ''))
                for j in a:
                    bin.write(f'{j}\n')
        else:
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                a = dec_bin_int(asbly[i + 1])
                for j in a:
                    bin.write(f'{j}\n')

    if asbly[i] == 'sub':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1100000\n')
        if '$' in asbly[i + 1]:
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                bin.write('0010010\n')
                a = dec_bin_int(asbly[i + 1].replace('$', ''))
                for j in a:
                    bin.write(f'{j}\n')
        else:
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                a = dec_bin_int(asbly[i + 1])
                for j in a:
                    bin.write(f'{j}\n')

    if asbly[i] == 'mul':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1010000\n')
        if '$' in asbly[i + 1]:
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                bin.write('0010010\n')
                a = dec_bin_int(asbly[i + 1].replace('$', ''))
                for j in a:
                    bin.write(f'{j}\n')
        else:
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                a = dec_bin_int(asbly[i + 1])
                for j in a:
                    bin.write(f'{j}\n')

    if asbly[i] == 'div':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1110000\n')
        if '$' in asbly[i + 1]:
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                bin.write('0010010\n')
                a = dec_bin_int(asbly[i + 1].replace('$', ''))
                for j in a:
                    bin.write(f'{j}\n')
        else:
            with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
                a = dec_bin_int(asbly[i + 1])
                for j in a:
                    bin.write(f'{j}\n')

    if asbly[i] == 'inc':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1001000\n')

    if asbly[i] == 'dec':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1101000\n')

    if asbly[i] == 'beq':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1011000\n')

    if asbly[i] == 'bne':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1111000\n')

    if asbly[i] == 'blt':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1001100\n')

    if asbly[i] == 'ble':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1101100\n')

    if asbly[i] == 'bge':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1111100\n')

    if asbly[i] == 'bgt':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('1000100\n')

    if 'L' in asbly[i]:
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0000111\n')

    if asbly[i] == 'push':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0000100\n')

    if asbly[i] == 'pop':
        with open('C:\\CPU Rita e Tomas\\binario.txt', 'a') as bin:
            bin.write('0000101\n')
