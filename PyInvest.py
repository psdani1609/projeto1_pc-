#Bibliotecas

import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Entradas

Capital = float(input('Capital inicial: '))
Aporte = float(input('Aporte Mensal: '))
Meses = int(input('Prazo (meses): '))
CDI_Anual = float(input('CDI Anual (%) ')) /100
PercentualCDB = float(input('Percentual do CDI (%) ')) /100 
PercentualLCI = float(input('Percentual do LCI (%) ')) /100
TaxaFundoInvestimentoImobiliario = float(input('Rentabilidade mensal FII (%) '))/100
Meta = float(input('Meta financeira (R$) '))

#Conversão CDI
CDI_Mensal = math.pow((1+CDI_Anual), 1/12) -1

#Total Investido
TotalInvestido = Capital + (Aporte * Meses)

#CDB
TaxaCDB = CDI_Mensal * PercentualCDB
MontanteCDB = (Capital * math.pow((1 + TaxaCDB), Meses ) + (Aporte * Meses))
LucroCDB = MontanteCDB - TotalInvestido
MontanteCDB_Liquido = TotalInvestido + (LucroCDB * 0.85)

#LCI
TaxaLCI = CDI_Mensal * PercentualLCI
MontanteLCI = (Capital * math.pow(1+ TaxaLCI, Meses) + (Aporte * Meses))

#Poupança
TaxaPoupanca = 0.005
MontantePoupanca = (Capital * math.pow(1 + TaxaPoupanca) ,Meses + (Aporte * Meses))

#FII - Simulações

