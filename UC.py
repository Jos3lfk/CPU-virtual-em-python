import ULA
import Registradores as rg
import sys


with open('C:\\CPU Rita e Tomas\\memoria.txt', 'w') as mem:
    mem = mem

with open('C:\\CPU Rita e Tomas\\binario.txt', 'r') as arquivo:
    conteudo = arquivo.read()

feixe = conteudo.split()

global auxiliar_bin_dec

def bin_dec_float(bin):
    cont = 0
    for l in range(len(bin)):
        if len(bin[l]) == 8:
            cont = 1
            global auxiliar_bin_dec
            auxiliar_bin_dec = 1
    if cont == 1:
        g1 = ''
        g2 = ''
        for k in range(len(bin)):
            a = len(bin[k])
            if a == 8:
                for j in range(len(bin)):
                    if j < k:
                        g1 += bin[j]
                    elif j >= k:
                        g2 += bin[j]
        g1 = str(bin_dec_float(g1))
        g2 = str(bin_dec_float(g2))
        dec = g1 + '.' + g2
        return dec
    else:
        a = bin
        sinal = 0
        if a.startswith('0'):
            sinal = 1
        else:
            sinal = -1
        bin = bin[1:]
        binario = ''
        for i in bin:
            binario = binario + i
        i = 0
        binario = int(binario)
        dec = 0
        n = 20
        while n >= 0:
            resto = binario % 10
            dec = dec + (resto * (2**i))
            n = n - 1
            i = i + 1
            binario = binario // 10
        dec = dec * sinal
        return dec


def bin_dec_int(bin):
    if '.' in bin:
        return 1
    else:
        if bin == []:
            return 1
        a = str(bin[0])
        sinal = 0
        if a.startswith('0'):
            sinal = 1
        else:
            sinal = -1
        bin[0] = bin[0][1:]
        binario = ''
        for i in bin:
            if i != '':
                aux3 = str(i)
                binario = str(binario + aux3)
        i = 0
        binario = int(binario)
        dec = 0
        n = 20
        while n >= 0:
            resto = binario % 10
            dec = dec + (resto * (2**i))
            n = n - 1
            i = i + 1
            binario = binario // 10
        dec = dec * sinal
        return dec


def dec_bin_int(decimal):
    decimal = str(decimal)
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


def store(a, b, c, d):
    with open('C:\\CPU Rita e Tomas\\memoria.txt', 'r') as mem:
        mem = mem.read()
    mem = mem.split()
    if mem == []:
        with open('C:\\CPU Rita e Tomas\\memoria.txt', 'w') as mem:
            for i in a:
                mem.write(f'{i}\n')
        with open('C:\\CPU Rita e Tomas\\memoria.txt', 'r') as memoria:
            memoria = memoria.read()
    else:
        if d == 1:
            with open('C:\\CPU Rita e Tomas\\memoria.txt', 'r') as mem:
                mem = mem.read()
            mem = mem.split()
            auxiliar = ''
            for i in range(len(mem)):
                if i == b:
                    j = 0
                    mem[i] = f'{a[j]}\n'
                    j = j + 1
            with open('C:\\CPU Rita e Tomas\\memoria.txt', 'w') as memoria:
                for i in mem:
                    memoria.write(f'{i}\n')
                for i in a:
                    memoria.write(f'{i}\n')
        else:
            auxi= 0
            for i in range(len(mem)):
                if i == b:
                    for j in range(len(mem)):
                        if j >= i and j <= i + c - 1:
                            mem[j] = a[auxi]
                            auxi = auxi + 1

            with open('C:\\CPU Rita e Tomas\\memoria.txt', 'w') as memoria:
                for f in mem:
                    memoria.write(f'{f}\n')



boolean = False
end = []
sizend = {}
binario = ''
valor = []
auxend = 0
auxend1 = 0
aux1 = 0
size = []
cache = {}
rg.r1 = 0
rg.r2 = 0
rg.r3 =0
UnidadeLogica = ULA.InstrucoesLa(rg.r1, valor, rg.r2, rg.r3)


for n in range(len(feixe)):

    if feixe[n] == '0000110':
        # main
        boolean = True

    if feixe[n] == '0100000':
        # store
        if boolean == True:
            end = []
            valor = []
            if feixe[n + 1] == '0001001':
                #r1
                if feixe[n + 2] == '0010000':
                    #to
                    end = []
                    for l in range(len(feixe)):
                        if l > n + 2 and  l < n + 7:
                            end.append(feixe[l])
                    end = bin_dec_int(end)
                    if '.' in str(rg.r1):
                        rg.r1 = dec_bin_int(rg.r1)
                        store(rg.r1, end, 8, 0)
                    else:
                        rg.r1 = dec_bin_int(rg.r1)
                        store(rg.r1, end, 4, 0)
            else:
                aux = 0
                auxend = 0
                auxsize = 0
                end = []
                valor = []
                size = []
                for j in range(len(feixe)):
                    if j > n and feixe[j] == '0010000':
                        #to
                        aux = j
                        auxend = j + 1
                        break
                for j in range(len(feixe)):
                    if j > n and j < aux:
                        valor.append(feixe[j])
                for j in range(len(feixe)):
                    if j >= auxend and j < auxend + 4:
                        end += [feixe[j]]
                    if j == auxend + 4:
                        break
                for j in range(len(feixe)):
                    if j > n and feixe[j] == '0010001':
                        #size
                        auxsize = j + 1
                        break
                for j in range(len(feixe)):
                    if j > auxsize and j < auxsize + 5:
                        size.append(feixe[j])
                size = bin_dec_int(size)
                end = bin_dec_int(end)
                auxv = 0
                for j in range(len(valor)):
                    if len(valor[j]) > 6:
                        auxv = 1
                if auxv == 1:
                    guardar = bin_dec_float(valor)
                else:
                    guardar = bin_dec_int(valor)
                    guardar = dec_bin_int(guardar)
                    valor = guardar
                if guardar == 1:
                    guardar = bin_dec_float(valor)
                cache[end] = f'{guardar}'
                store(valor, end, size, 1)
                end = []

    if feixe[n] == '0100010':
        # load
        end = []
        valor = []
        registrador = 0
        if boolean == True:
            if feixe[n + 1] == '0010010':
                #$
                for i in range(len(feixe)):
                    if i > n + 1 and i < n + 6:
                        end.append(feixe[i])
                if feixe[n + 6] == '0001001':
                    registrador = 1
                elif feixe[n + 6] == '0001010':
                    registrador = 2
                elif feixe[n + 6] == '0001011':
                    registrador = 3
                end = bin_dec_int(end)
                with open('C:\\CPU Rita e Tomas\\memoria.txt', 'r') as mem:
                    mem = mem.read()
                    mem = mem.split()
                for i in range(len(mem)):
                    if i >= end and i < end + 8:
                        valor.append(mem[i])
                aux = 0
                for i in range(len(valor)):
                    if len(valor[i]) == 8:
                        aux = 1
                if aux == 0:
                    valor = bin_dec_int(valor)
                    valor = int(valor)
                else:
                    valor = bin_dec_float(valor)
                    valor = float(valor)
                if registrador == 1:
                    rg.r1 = valor
                elif registrador == 2:
                    rg.r2 = valor
                elif registrador == 3:
                    rg.r3 = valor
            else:
                aux = []
                valor = []
                for j in range(len(feixe)):
                    if j > n and j < n + 5:
                        aux.append(feixe[j])
                valor = aux
                aux = 0
                for i in valor:
                    if len(i) == 8:
                        aux = 1
                if aux == 0:
                    valor = bin_dec_int(valor)
                else:
                    valor = bin_dec_float(valor)
                rg.r1 = valor

    if feixe[n] == '0100100':
        # mov
        if boolean == True:
            a = ''

    if feixe[n] == '0100110':
        # jump
        if boolean == True:
            a = ''

    if feixe[n] == '1000000':
        #add
        if boolean == True:
            if feixe[n + 1] == '0010010':
                #$
                end = []
                valor = []
                for i in range(len(feixe)):
                    if i > n + 1 and i < n + 6:
                        end.append(feixe[i])
                end = bin_dec_int(end)
                with open('C:\\CPU Rita e Tomas\\memoria.txt', 'r') as mem:
                    mem = mem.read()
                    mem = mem.split()
                for i in range(len(mem)):
                    if i >= end and i < end + 8:
                        valor.append(mem[i])
                aux = 0
                for i in range(len(valor)):
                    if len(valor[i]) == 8:
                        aux = 1
                guardar_valor = []
                if aux == 0:
                    guardar_valor = valor
                    valor = []
                    for i in range(len(guardar_valor)):
                        if i < 4:
                            valor.append(guardar_valor[i])
                    valor = bin_dec_int(valor)
                    valor = int(valor)
                else:
                    valor = bin_dec_float(valor)
                    valor = float(valor)
            else:
                valor = []
                aux = 0
                for i in range(len(feixe)):
                    if i > n and i < n + 8:
                        valor.append(feixe[i])
                for i in range(len(valor)):
                    if len(valor[i]) == 8:
                        aux = 1
                guardar_valor = valor
                valor = []
                if aux != 1:
                    for i in range(len(guardar_valor)):
                        if i < 4:
                            valor.append(guardar_valor[i])
                if aux == 0:
                    valor = bin_dec_int(valor)
                    valor = int(valor)
                else:
                    valor = bin_dec_float(valor)
                    valor = float(valor)
            UnidadeLogica = ULA.InstrucoesLa(rg.r1, valor, 0, 0)
            rg.r1 = UnidadeLogica.add()

    if feixe[n] == '1100000':
        # sub
        if boolean == True:
            if feixe[n + 1] == '0010010':
                # $
                end = []
                valor = []
                for i in range(len(feixe)):
                    if i > n + 1 and i < n + 6:
                        end.append(feixe[i])
                end = bin_dec_int(end)
                with open('C:\\CPU Rita e Tomas\\memoria.txt', 'r') as mem:
                    mem = mem.read()
                    mem = mem.split()
                for i in range(len(mem)):
                    if i >= end and i < end + 8:
                        valor.append(mem[i])
                aux = 0
                for i in range(len(valor)):
                    if len(valor[i]) == 8:
                        aux = 1
                guardar_valor = []
                if aux == 0:
                    guardar_valor = valor
                    valor = []
                    for i in range(len(guardar_valor)):
                        if i < 4:
                            valor.append(guardar_valor[i])
                    valor = bin_dec_int(valor)
                    valor = int(valor)
                else:
                    valor = bin_dec_float(valor)
                    valor = float(valor)
            else:
                valor = []
                aux = 0
                for i in range(len(feixe)):
                    if i > n and i < n + 8:
                        valor.append(feixe[i])
                for i in range(len(valor)):
                    if len(valor[i]) == 8:
                        aux = 1
                guardar_valor = valor
                valor = []
                if aux != 1:
                    for i in range(len(guardar_valor)):
                        if i < 4:
                            valor.append(guardar_valor[i])
                if aux == 0:
                    valor = bin_dec_int(valor)
                    valor = int(valor)
                else:
                    valor = bin_dec_float(valor)
                    valor = float(valor)
            UnidadeLogica = ULA.InstrucoesLa(rg.r1, valor, 0, 0)
            rg.r1 = UnidadeLogica.sub()

    if feixe[n] == '1010000':
        # mul
        if boolean == True:
            if feixe[n + 1] == '0010010':
                # $
                end = []
                valor = []
                for i in range(len(feixe)):
                    if i > n + 1 and i < n + 6:
                        end.append(feixe[i])
                end = bin_dec_int(end)
                with open('C:\\CPU Rita e Tomas\\memoria.txt', 'r') as mem:
                    mem = mem.read()
                    mem = mem.split()
                for i in range(len(mem)):
                    if i >= end and i < end + 8:
                        valor.append(mem[i])
                aux = 0
                for i in range(len(valor)):
                    if len(valor[i]) == 8:
                        aux = 1
                guardar_valor = []
                if aux == 0:
                    guardar_valor = valor
                    valor = []
                    for i in range(len(guardar_valor)):
                        if i < 4:
                            valor.append(guardar_valor[i])
                    valor = bin_dec_int(valor)
                    valor = int(valor)
                else:
                    valor = bin_dec_float(valor)
                    valor = float(valor)
            else:
                valor = []
                aux = 0
                for i in range(len(feixe)):
                    if i > n and i < n + 8:
                        valor.append(feixe[i])
                for i in range(len(valor)):
                    if len(valor[i]) == 8:
                        aux = 1
                guardar_valor = valor
                valor = []
                if aux != 1:
                    for i in range(len(guardar_valor)):
                        if i < 4:
                            valor.append(guardar_valor[i])
                if aux == 0:
                    valor = bin_dec_int(valor)
                    valor = int(valor)
                else:
                    valor = bin_dec_float(valor)
                    valor = float(valor)
            UnidadeLogica = ULA.InstrucoesLa(rg.r1, valor, 0, 0)
            rg.r1 = UnidadeLogica.mul()

    if feixe[n] == '1110000':
        # div
        if boolean == True:
            if feixe[n + 1] == '0010010':
                # $
                end = []
                valor = []
                for i in range(len(feixe)):
                    if i > n + 1 and i < n + 6:
                        end.append(feixe[i])
                end = bin_dec_int(end)
                with open('C:\\CPU Rita e Tomas\\memoria.txt', 'r') as mem:
                    mem = mem.read()
                    mem = mem.split()
                for i in range(len(mem)):
                    if i >= end and i < end + 8:
                        valor.append(mem[i])
                aux = 0
                for i in range(len(valor)):
                    if len(valor[i]) == 8:
                        aux = 1
                guardar_valor = []
                if aux == 0:
                    guardar_valor = valor
                    valor = []
                    for i in range(len(guardar_valor)):
                        if i < 4:
                            valor.append(guardar_valor[i])
                    valor = bin_dec_int(valor)
                    valor = int(valor)
                else:
                    valor = bin_dec_float(valor)
                    valor = float(valor)
            else:
                valor = []
                aux = 0
                for i in range(len(feixe)):
                    if i > n and i < n + 8:
                        valor.append(feixe[i])
                for i in range(len(valor)):
                    if len(valor[i]) == 8:
                        aux = 1
                guardar_valor = valor
                valor = []
                if aux != 1:
                    for i in range(len(guardar_valor)):
                        if i < 4:
                            valor.append(guardar_valor[i])
                if aux == 0:
                    valor = bin_dec_int(valor)
                    valor = int(valor)
                else:
                    valor = bin_dec_float(valor)
                    valor = float(valor)
            UnidadeLogica = ULA.InstrucoesLa(rg.r1, valor, 0, 0)
            rg.r1 = UnidadeLogica.div()

    if feixe[n] == '1001000':
        # inc
        if boolean == True:
            UnidadeLogica = ULA.InstrucoesLa(rg.r1, 0, 0, 0)
            rg.r1 = UnidadeLogica.inc()

    if feixe[n] == '1101000':
        # dec
        if boolean == True:
            UnidadeLogica = ULA.InstrucoesLa(rg.r1, 0, 0, 0)
            rg.r1 = UnidadeLogica.dec()

    if feixe[n] == '1011000':
        #beq
        if boolean == True:
            UnidadeLogica = ULA.InstrucoesLa(0, 0, rg.r2, rg.r3)
            boolean = UnidadeLogica.beq()

    if feixe[n] == '1111000':
        # bne
        if boolean == True:
            UnidadeLogica = ULA.InstrucoesLa(0, 0, rg.r2, rg.r3)
            boolean = UnidadeLogica.bne()

    if feixe[n] == '1001100':
        # blt
        if boolean == True:
            UnidadeLogica = ULA.InstrucoesLa(0, 0, rg.r2, rg.r3)
            boolean = UnidadeLogica.blt()

    if feixe[n] == '1101100':
        # ble
        if boolean == True:
            UnidadeLogica = ULA.InstrucoesLa(0, 0, rg.r2, rg.r3)
            boolean = UnidadeLogica.ble()

    if feixe[n] == '1111100':
        # bge
        if boolean == True:
            UnidadeLogica = ULA.InstrucoesLa(0, 0, rg.r2, rg.r3)
            boolean = UnidadeLogica.bge()

    if feixe[n] == '1000100':
        # bgt
        if boolean == True:
            UnidadeLogica = ULA.InstrucoesLa(0, 0, rg.r2, rg.r3)
            boolean = UnidadeLogica.bgt()

    if feixe[n] == '0000100':
        # push
        a = ''

    if feixe[n] == '0000101':
        # pop
        if boolean == False:
            boolean = True

    if feixe[n] == '0000111':
        # L{n}
        if boolean == True:
            a = ''

with open('C:\\CPU Rita e Tomas\\memoria.txt', 'r') as mem:
    mem = mem.read()

    print(mem)