import string
class Equacalc:
    def __init__(self):
        var = 0
        Raddvar = ''
        Rmulvar = ''
        Rvarlist = []
        Laddvar = ''
        Lmulvar = ''
        Lvarlist = []
        tempvar = 0
        templisty = []
        newequa1 = 0
        negmulflag = 0
        negmulflag2 = 0
        Laddsubliketerms = 0
        Raddsubliketerms = 0
        Lmuldivliketerms = 0
        Rmuldivliketerms = 0
        Lmuldivlist = []
        Rmuldivlist = []
        Lmulvarlist = []
        Rmulvarlist = []
        alphabet = list(string.ascii_lowercase)
        strint = ''
        self.onlyOnce = 1
        Rblanky = []
        Lblanky = []
        Lbint = 0
        Lbvar = 0
        Llisty = []
        Rlisty = []
        variable = 'n'
        equation = str(raw_input('Type Equation: '))
        print equation
        for i in equation:
            if i in alphabet:
                variable = i
        equa = ''
        for i in equation:
            equa += i
            if i == '=':
                break
        equa2 = ''
        flag = False
        for i in equation:
            if flag:
                equa2 += i
            if i == '=':
                flag = True
        equa2 += '='
        for j in range(len(equa)):
            if self.onlyOnce == 1:
                self.onlyOnce = 0
                if equa[0] == '0' or equa[0] == '1' or equa[0] == '2' or equa[0] == '3' or equa[0] == '4' or equa[0] == '5' or equa[0] == '6' or equa[0] == '7' or equa[0] == '8' or equa[0] == '9' or equa[0] == '-':
                    increment = 0
                    while equa[increment] != '+':
                        increment += 1
                        if equa[increment] == '-' or equa[increment] == '=' or equa[increment] == '*':
                            break
                    temp = ''
                    temp += equa[j:increment]
                    if equa[increment] == '*' and not temp.startswith('*'):
                        temp = '*' + temp
                    Lblanky.append(temp)
            elif equa[j] == '+' or equa[j] == '-' or equa[j] == '*':
                increment = j
                while equa[increment] != '=':
                    if negmulflag == 1:
                        negmulflag = 0
                        break
                    increment += 1
                    if equa[increment] == '+' or equa[increment] == '-' or equa[increment] == '*':
                        if equa[j] == '*' and (equa[j+1] == '-' or equa[j+1] == '+'):
                            while equa[increment] != '=':
                                negmulflag = 1
                                increment += 1
                                if equa[increment] == '+' or equa[increment] == '-' or equa[increment] == '*':
                                    print 'hi'
                                    break
                        break
                temp = ''
                temp += equa[j:increment]
                if equa[increment] == '*' and not temp.startswith('*'):
                    temp = '*' + temp
                    Lmuldivlist.append(temp)
                elif temp != '':
                    Lblanky.append(temp)
        self.onlyOnce = 1
        for i in range(len(equa2)):
            if self.onlyOnce == 1:
                self.onlyOnce = 0
                if equa2[0] == '0' or equa2[0] == '1' or equa2[0] == '2' or equa2[0] == '3' or equa2[0] == '4' or equa2[0] == '5' or equa2[0] == '6' or equa2[0] == '7' or equa2[0] == '8' or equa2[0] == '9' or equa2[0] == '-':
                    increment = 0
                    while equa2[increment] != '+':
                        increment += 1
                        if equa2[increment] == '-' or equa2[increment] == '=' or equa2[increment] == '*':
                            break

                    temp = ''
                    temp += equa2[i:increment]
                    if equa2[increment] == '*' and not temp.startswith('*'):
                        temp = '*' + temp
                    Rblanky.append(temp)
            elif equa2[i] == '+' or equa2[i] == '-' or equa2[i] == '*':
                increment = i
                while equa2[increment] != '=':
                    if negmulflag2 == 1:
                        negmulflag2 = 0
                        break
                    increment += 1
                    if equa2[increment] == '+' or equa2[increment] == '-' or equa2[increment] == '*':
                        if equa2[i] == '*' and (equa2[i+1] == '-' or equa2[i+1] == '+'):
                            while equa2[increment] != '=':
                                negmulflag2 = 1
                                increment += 1
                                if equa2[increment] == '+' or equa2[increment] == '-' or equa2[increment] == '*':
                                    print 'hi'
                                    break
                        elif equa2[i] == '+' and (equa2[i+1] == '-' or equa2[i+1] == '+'):
                            while equa2[increment] != '=':
                                negmulflag2 = 1
                                increment += 1
                                if equa2[increment] == '+' or equa2[increment] == '-' or equa2[increment] == '*':
                                    print 'hi'
                                    break
                        break
                temp = ''
                temp += equa2[i:increment]
                if equa2[increment] == '*' and not temp.startswith('*'):
                    temp = '*' + temp
                    Rmuldivlist.append(temp)
                elif temp != '':
                    Rblanky.append(temp)

        for i in Lblanky:
            j = i
            intflag = True
            strint = ''
            if j[0] == '+' and j[-1] not in alphabet:
                strint = j
                Llisty.append(int(strint))
                intflag = False
            if j[0] == '*' and j[-1] not in alphabet:
                strint = list(j)
                strint.remove(strint[0])
                strint = ''.join(strint)
                Lmuldivlist.append(int(strint))
                intflag = False
            if intflag:
                if j[0] == '-' and j[-1] not in alphabet:
                    strint = j
                    Llisty.append(int(strint))
                elif j[-1] not in alphabet:
                    if j[0] != '+' or j[0] != '-' or j[0] != '*':
                        Llisty.append(int(j))
                elif j[-1] in alphabet:
                    tempjlist = list(j)
                    tempjlist.remove(tempjlist[-1])
                    strtempj = ''.join(tempjlist)
                    if strtempj == '-':
                        strtempj = '-1'
                    elif strtempj == '+':
                        strtempj = '+1'
                    if strtempj.startswith('*'):
                        tempwar2 = list(strtempj)
                        tempwar2.remove(tempwar2[0])
                        strtempj = int(''.join(tempwar2))
                        Lmulvarlist.append(strtempj)
                    else:
                        inttempj = int(strtempj)
                        Lvarlist.append(inttempj)

        for i in Rblanky:
            j = i
            intflag = True
            strint = ''
            if j[0] == '+' and j[-1] not in alphabet:
                if j[1] == '-':
                    j = j[1:]
                    Rlisty.append(int(j))
                else:
                    strint = j
                    Rlisty.append(int(strint))
                    intflag = True
            elif j[0] == '*' and j[-1] not in alphabet:
                strint = list(j)
                strint.remove(strint[0])
                strint = ''.join(strint)
                Rmuldivlist.append(int(strint))
                intflag = False
            elif intflag:
                if j[0] == '-' and j[-1] not in alphabet:
                    strint = j
                    Rlisty.append(int(strint))
                elif j[-1] not in alphabet:
                    if j[0] != '+' or j[0] != '-' or j[0] != '*':
                        Rlisty.append(int(j))
                elif j[-1] in alphabet:
                    tempjlist = list(j)
                    tempjlist.remove(tempjlist[-1])
                    strtempj = ''.join(tempjlist)
                    if strtempj == '-':
                        strtempj = '-1'
                    elif strtempj == '+':
                        strtempj = '+1'
                    if strtempj.startswith('*'):
                        tempwar2 = list(strtempj)
                        tempwar2.remove(tempwar2[0])
                        strtempj = int(''.join(tempwar2))
                        Rmulvarlist.append(strtempj)
                    else:
                        inttempj = int(strtempj)
                        Rvarlist.append(inttempj)

        tempvar = 0
        for i in Llisty:
            tempvar += i
        Laddsubliketerms = str(tempvar)
        tempvar = 1
        if Lmuldivlist != []:
            for i in Lmuldivlist:
                tempvar *= i
            Lmuldivliketerms = str(tempvar)
        tempvar = 0
        for i in Lvarlist:
            tempvar += i
        Laddvar = str(tempvar)
        Laddvar += variable
        tempvar = 1
        if Lmulvarlist != []:
            for i in Lmulvarlist:
                tempvar *= i
            Lmulvar = str(tempvar)
        Lmulvar += variable
        tempvar = 1
        if Rmulvarlist != []:
            for i in Rmulvarlist:
                tempvar *= i
            Rmulvar = str(tempvar)
        Rmulvar += variable
        tempvar = 0
        for i in Rlisty:
            tempvar += i
        Raddsubliketerms = str(tempvar)
        tempvar = 1
        if Rmuldivlist != []:
            for i in Rmuldivlist:
                tempvar *= i
            Rmuldivliketerms = str(tempvar)
        tempvar = 0
        for i in Rvarlist:
            tempvar += i
        Raddvar = str(tempvar)
        Raddvar += variable

        Raddtemp = int(Raddsubliketerms)
        Rmultemp = int(Rmuldivliketerms)
        Laddtemp = int(Laddsubliketerms)
        #if Lmuldivliketerms[0] == '*' and Lmuldivliketerms[1] == '-':
        #   Lmuldivliketerms = Lmuldivliketerms[1:]
        Lmultemp = int(Lmuldivliketerms)
        Raddsubliketerms = str(Raddtemp + Rmultemp)
        Laddsubliketerms = str(Laddtemp + Lmultemp)

        if Raddsubliketerms == '0':
            Raddsubliketerms = ''
        elif Raddsubliketerms != '0':
            Raddsubliketerms = '+' + Raddsubliketerms
            if Raddtemp == 0:
                Raddsubliketerms = Raddsubliketerms[1:]
                Raddsubliketerms = '*' + Raddsubliketerms
        if Laddsubliketerms == '0':
            Laddsubliketerms = ''
        elif Laddsubliketerms != '0':
            Laddsubliketerms = '+' + Laddsubliketerms
            if Laddtemp == 0:
                Laddsubliketerms = Laddsubliketerms[1:]
                Laddsubliketerms = '*' + Laddsubliketerms

        temp0var = '0' + variable

        if Laddvar == temp0var:
           Laddvar = ''
        elif Laddvar != temp0var:
           Laddvar = '+' + Laddvar
        if Raddvar == temp0var:
           Raddvar = ''
        elif Raddvar != temp0var:
           Raddvar = '+' + Raddvar
        if Lmulvar == variable:
           Lmulvar = ''
        elif Lmulvar != variable:
           Lmulvar = '+' + Lmulvar
        if Rmulvar == variable:
           Rmulvar = ''
        elif Rmulvar != variable:
           Rmulvar = '+' + Rmulvar

        if Lmulvar == '' and Rmulvar != '':
            newequa1 = str(Laddvar + Lmulvar + Laddsubliketerms + '=' + Rmulvar + '^' + str(len(Rmulvarlist)) + Raddvar + Raddsubliketerms)
        elif Lmulvar != '' and Rmulvar == '':
            newequa1 = str(Laddvar + Lmulvar + '^' + str(len(Lmulvarlist)) + Laddsubliketerms + '=' + Rmulvar + Raddvar + Raddsubliketerms)
        elif Lmulvar == '' and Rmulvar == '':
            newequa1 = str(Laddvar + Lmulvar + Laddsubliketerms + '=' + Rmulvar + Raddvar + Raddsubliketerms)
        elif Lmulvar != '' and Rmulvar != '':
            newequa1 = str(Laddvar + Lmulvar + '^' + str(len(Lmulvarlist)) + Laddsubliketerms + '=' + Rmulvar + '^' + str(len(Rmulvarlist)) + Raddvar + Raddsubliketerms)

        if newequa1.endswith('='):
            newequa1 += '0'
        print newequa1
        newequa2 = ''
        newequa3 = ''
        for i in newequa1:
            newequa2 += i
            if i == '=':
                break
        flag = False
        for i in newequa1:
            if flag:
                newequa3 += i
            if i == '=':
                flag = True
        newequa3 += '='

        Raddvar = ''
        Rmulvar = ''
        Rvarlist = []
        Laddvar = ''
        Lmulvar = ''
        Lvarlist = []
        tempvar = 0
        templisty = []
        newequa1 = 0
        negmulflag = 0
        negmulflag2 = 0
        Laddsubliketerms = 0
        Raddsubliketerms = 0
        Lmuldivliketerms = 0
        Rmuldivliketerms = 0
        Lmuldivlist = []
        Rmuldivlist = []
        Lmulvarlist = []
        Rmulvarlist = []
        alphabet = list(string.ascii_lowercase)
        strint = ''
        self.onlyOnce = 1
        Rblanky = []
        Lblanky = []
        Lbint = 0
        Lbvar = 0
        Llisty = []
        Rlisty = []

        for j in range(len(newequa2)):
            if self.onlyOnce == 1:
                self.onlyOnce = 0
                if newequa2[0] == '0' or newequa2[0] == '1' or newequa2[0] == '2' or newequa2[0] == '3' or newequa2[0] == '4' or newequa2[0] == '5' or newequa2[0] == '6' or newequa2[0] == '7' or newequa2[0] == '8' or newequa2[0] == '9' or newequa2[0] == '-' or newequa2[0] == '+':
                    increment = 0
                    while True:
                        increment += 1
                        if newequa2[increment] == '-' or newequa2[increment] == '=' or newequa2[increment] == '*' or newequa2[increment] == '+':
                            break
                    temp = ''
                    temp += newequa2[j:increment]
                    if newequa2[increment] == '*' and not temp.startswith('*'):
                        temp = '*' + temp
                    Lblanky.append(temp)
            elif newequa2[j] == '+' or newequa2[j] == '-' or newequa2[j] == '*':
                increment = j
                while newequa2[increment] != '=':
                    if negmulflag == 1:
                        negmulflag = 0
                        break
                    increment += 1
                    if newequa2[increment] == '+' or newequa2[increment] == '-' or newequa2[increment] == '*':
                        if newequa2[j] == '*' and (newequa2[j+1] == '-' or newequa2[j+1] == '+'):
                            while newequa2[increment] != '=':
                                negmulflag = 1
                                increment += 1
                                if newequa2[increment] == '+' or newequa2[increment] == '-' or newequa2[increment] == '*':
                                    print 'hi'
                                    break
                        if newequa2[j] == '+' and (newequa2[j+1] == '-'):
                            while newequa2[increment] != '=':
                                negmulflag = 1
                                increment += 1
                                if newequa2[increment] == '+' or newequa2[increment] == '-' or newequa2[increment] == '*':
                                    print 'hi'
                                    break
                        break
                temp = ''
                temp += newequa2[j:increment]
                if newequa2[increment] == '*' and not temp.startswith('*'):
                    temp = '*' + temp
                    Lmuldivlist.append(temp)
                elif newequa2[increment] == '+' and newequa2[increment+1] == '-':
                    temp = temp[1:]
                    Lblanky.append(temp)
                elif temp != '':
                    Lblanky.append(temp)
        self.onlyOnce = 1
        for i in range(len(newequa3)):
            if self.onlyOnce == 1:
                self.onlyOnce = 0
                if newequa3[0] == '0' or newequa3[0] == '1' or newequa3[0] == '2' or newequa3[0] == '3' or newequa3[0] == '4' or newequa3[0] == '5' or newequa3[0] == '6' or newequa3[0] == '7' or newequa3[0] == '8' or newequa3[0] == '9' or newequa3[0] == '-' or newequa2[0] == '+':
                    increment = 0
                    while True:
                        increment += 1
                        if newequa3[increment] == '-' or newequa3[increment] == '=' or newequa3[increment] == '*' or newequa3[increment] == '+':
                            break
                    temp = ''
                    temp += newequa3[i:increment]
                    if newequa3[increment] == '*' and not temp.startswith('*'):
                        temp = '*' + temp
                    Rblanky.append(temp)
            elif newequa3[i] == '+' or newequa3[i] == '-' or newequa3[i] == '*':
                increment = i
                while newequa3[increment] != '=':
                    if negmulflag2 == 1:
                        negmulflag2 = 0
                        break
                    increment += 1
                    if newequa3[increment] == '+' or newequa3[increment] == '-' or newequa3[increment] == '*':
                        if newequa3[i] == '*' and (newequa3[i+1] == '-' or newequa3[i+1] == '+'):
                            while newequa3[increment] != '=':
                                negmulflag2 = 1
                                increment += 1
                                if newequa3[increment] == '+' or newequa3[increment] == '-' or newequa3[increment] == '*':
                                    print 'hi'
                                    break
                        elif newequa3[i] == '+' and (newequa3[i+1] == '-' or newequa3[i+1] == '+'):
                            while newequa3[increment] != '=':
                                negmulflag2 = 1
                                increment += 1
                                if newequa3[increment] == '+' or newequa3[increment] == '-' or newequa3[increment] == '*':
                                    print 'hi'
                                    break
                        break
                temp = ''
                temp += newequa3[i:increment]
                if newequa3[increment] == '*' and not temp.startswith('*'):
                    temp = '*' + temp
                    Rmuldivlist.append(temp)
                elif temp != '':
                    Rblanky.append(temp)

        if len(Rblanky) == 2 and len(Lblanky) == 2:
            lblankyint = int(Lblanky[1])
            temprblanky = Rblanky[1]
            if temprblanky[0] == '+' and temprblanky[1] == '-':
                temprblanky = temprblanky[1:]
            rblankyint = int(temprblanky)
            total = rblankyint - lblankyint
            Rblanky.remove(Rblanky[1])
            Rblanky.append(total)
            Lblanky.remove(Lblanky[1])
            rbstr = Rblanky[0]
            lbstr = Lblanky[0]

            increment = 0
            for i in rbstr:
                increment += 1
                if i == variable:
                    break
            rbint = int(rbstr[0:increment-1])

            increment = 0
            for i in lbstr:
                increment += 1
                if i == variable:
                    break
            lbint = int(lbstr[0:increment-1])

            rlbtotal = lbint - rbint
            rlbtotalstr = str(str(rlbtotal) + variable)
            Lblanky.remove(Lblanky[0])
            Rblanky.remove(Rblanky[0])
            Lblanky.append(rlbtotalstr)

            newequa4 = str(Lblanky[0] + "=" + str(Rblanky[0]))
            print newequa4
            totalfinal = float(Rblanky[0]) / float(rlbtotal)
            print variable + '=' + str(totalfinal)

        elif len(Rblanky) == 1 and len(Lblanky) == 2:
            templblanky = str(Lblanky[0])
            templblanky2 = str(Lblanky[1])
            if templblanky[0] == '*' and templblanky2[0] == '*':
                templblanky = str(Lblanky[0])
                templblanky = templblanky[1:]
                templblanky2 = str(Lblanky[1])
                templblanky2 = templblanky2[1:]
                increment = 0
                for i in templblanky:
                    increment += 1
                    if i == 'n':
                        break
                templblanky = templblanky[0:increment-1]
                multvariable = int(templblanky) * int(templblanky2)
                multvariablestr = str(str(multvariable) + 'n')
                newequa4 = multvariablestr + '=' + Rblanky[0]
                print newequa4
                totalfinal = float(Rblanky[0]) / float(multvariable)
                newequa5 = 'n' + '=' + str(totalfinal)
                print newequa5
            else:
                templblanky = str(Lblanky[0])
                templblanky = templblanky[1:]
                templblanky2 = str(Rblanky[0])
                templblanky2 = templblanky2[1:]
                increment = 0
                for i in templblanky:
                    increment += 1
                    if i == 'n':
                        break
                templblanky = templblanky[0:increment - 1]
                multvariable = int(templblanky) - int(templblanky2)
                multvariablestr = str(str(multvariable) + 'n')
                addtotal = int(templblanky) - int(templblanky2)
                Rblanky.remove(Rblanky[0])
                Rblanky.append(addtotal)
                Lblanky.remove(Lblanky[1])
                newequa4 = str(str(Lblanky[0]) + '=' + str(Rblanky[0]))
                print newequa4
                totalfinal = float(Rblanky[0]) / float(multvariable)
                newequa5 = str('n' + '=' + str(totalfinal))
                print newequa5

        elif len(Rblanky) == 2 and len(Lblanky) == 1:
            temprblanky = str(Rblanky[0])
            temprblanky2 = str(Rblanky[1])
            if temprblanky[0] == '*' and temprblanky2[0] == '*':
                temprblanky = str(Rblanky[0])
                temprblanky = temprblanky[1:]
                temprblanky2 = str(Rblanky[1])
                temprblanky2 = temprblanky2[1:]
                increment = 0
                for i in temprblanky:
                    increment += 1
                    if i == 'n':
                        break
                temprblanky = temprblanky[0:increment-1]
                multvariable = int(temprblanky) * int(temprblanky2)
                multvariablestr = str(str(multvariable) + 'n')
                newequa4 = multvariablestr + '=' + Lblanky[0]
                print newequa4
                totalfinal = float(Lblanky[0]) / float(multvariable)
                newequa5 = 'n' + '=' + str(totalfinal)
                print newequa5
            else:
                templblanky = str(Rblanky[0])
                templblanky = templblanky[1:]
                templblanky2 = str(Lblanky[0])
                templblanky2 = templblanky2[1:]
                increment = 0
                for i in templblanky:
                    increment += 1
                    if i == 'n':
                        break
                templblanky.replace(variable, '')
                templblanky2.replace(variable, '')
                multvariable = int(templblanky) - int(templblanky2)
                multvariablestr = str(str(multvariable) + 'n')
                addtotal = int(templblanky) - int(templblanky2)
                Lblanky.remove(Lblanky[0])
                Lblanky.append(addtotal)
                Rblanky.remove(Rblanky[1])
                newequa4 = str(str(Rblanky[0]) + '=' + str(Lblanky[0]))
                print newequa4
                totalfinal = float(Lblanky[0]) / float(multvariable)
                newequa5 = str('n' + '=' + str(totalfinal))
                print newequa5
        elif len(Rblanky) == 1 and len(Lblanky) == 1:
            templblanky = str(Rblanky[0])
            templblanky2 = str(Lblanky[0])
            if templblanky[-1] in alphabet:
                increment = 0
                for i in templblanky:
                    increment += 1
                    if i == 'n':
                        break
                templblanky = templblanky[0:increment-1]
                finaltotal = float(templblanky2) / float(templblanky)
                newequa4 = str('n' + '=' + str(finaltotal))
                print newequa4
            else:
                increment = 0
                for i in templblanky2:
                    increment += 1
                    if i == 'n':
                        break
                templblanky2 = templblanky2[0:increment - 1]
                finaltotal = float(templblanky) / float(templblanky2)
                newequa4 = str('n' + '=' + str(finaltotal))
                print newequa4

ecalc = Equacalc()

#Please Halp