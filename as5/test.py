import subEval
td = {'1.txt':'alpha_plain', '2.txt':'beta_plain', '3.txt':'delta_plain', '4':'epsilon_plain', '5.txt':'gamma_plain'}

for i in td:
    print(subEval.evalFile(i, td[i]))
