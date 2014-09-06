import commands

#CFOP algorithm
def CFOP(listPattern) :
    pattern = ''
    for part in listPattern :
        pattern += ' '+part
    return commands.getstatusoutput('./lib/CFOP/CFOP'+pattern)[1]