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
MontantePoupanca = (Capital * math.pow(1 + TaxaPoupanca , Meses) + (Aporte * Meses))

#Simulações
Simulacao1 = (Capital * math.pow((TaxaFundoInvestimentoImobiliario + random.uniform (-0.03,0.03) ) , Meses) + (Aporte * Meses))
Simulacao2 = (Capital * math.pow((TaxaFundoInvestimentoImobiliario + random.uniform (-0.03,0.03) ) , Meses) + (Aporte * Meses))
Simulacao3 = (Capital * math.pow((TaxaFundoInvestimentoImobiliario + random.uniform (-0.03,0.03) ) , Meses) + (Aporte * Meses))
Simulacao4 = (Capital * math.pow((TaxaFundoInvestimentoImobiliario + random.uniform (-0.03,0.03) ) , Meses) + (Aporte * Meses))
Simulacao5 = (Capital * math.pow((TaxaFundoInvestimentoImobiliario + random.uniform (-0.03,0.03) ) , Meses) + (Aporte * Meses))

ValorFundoInvestimentoImobiliario = {Simulacao1, Simulacao2, Simulacao3, Simulacao4, Simulacao5}

MediaFII = statistics.mean (ValorFundoInvestimentoImobiliario)
MedianaFii = statistics.median (ValorFundoInvestimentoImobiliario)
DesvioPadraoFII = statistics.stdev (ValorFundoInvestimentoImobiliario)

ValorFinalFii = MediaFII

#Simulação das datas

DataSimulacao = datetime.datetime.now()
DiasParaResgate = Meses * 30
DataParaResgate = DataSimulacao + datetime.timedelta(days = DiasParaResgate)

#MetaFinanceira

MetaAtingida = ValorFinalFii >= Meta

#Formatação/Saidaseilanaosei

CapitalF = locale.currency(Capital,grouping=True)
TotalInvestidoF = locale.currency(TotalInvestido,grouping=True)
CdbF = locale.currency(MontanteCDB_Liquido,grouping=True)
LciF = locale.currency(MontanteLCI,grouping=True)
PoupancaF = locale.currency(MontantePoupanca,grouping=True)
FiiF = locale.currency(ValorFinalFii,grouping=True)
MediaFiiF = locale.currency(MediaFII,grouping=True)
DesvioPadraoFIIF = locale.currency(DesvioPadraoFII,grouping=True)

#Gráfico



