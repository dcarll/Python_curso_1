from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays
from calendar import monthrange #pegar os dias da semana

setlocale(LC_ALL, "pt_BT.utf-8")
dt = datetime.now()
mes_atual = int(dt.strftime("%m"))

formatacao1 = dt.strftime("%A, %d de %B de %Y")
formatacao2 = dt.strftime("%d/%m/%Y %H:%M:%S")
print(formatacao1)
# print(formatacao2)
print(mdays[1:])
print(f'Mês: {mes_atual}, \nMês contém: {mdays[mes_atual]} dias')

print(monthrange(2022, 2)) #exibe  número correspondente a semana e quantos dias ele contem, os numero das semana vão de 0 a 6
print("-"*40)

ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)