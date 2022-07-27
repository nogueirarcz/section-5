from datetime import datetime, timedelta
from time import strptime

datavar = datetime(2022, 7, 26, 23, 58, 56)
print(datavar)

# Formatar padrão
print(datavar.strftime('%d/%m/%Y %H:%M:%S'))

# Formatar String para Date
datavar = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(datavar)

# Timestamp
print(datavar.timestamp())

# Converter data a partir do timestamp
datavar = datetime.fromtimestamp(555729200.0)
print(datavar)

print('----- ---- ---- ---- ---- ----')

# ----- ---- ---- ---- ---- ----

# timedelta
datavar = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
print(datavar)

# Adicionando 5 dias a essa data
datavar = datavar + timedelta(days=5)
print(datavar)

# Comparando datas
data1 = datetime.strptime('20/05/1987 21:00:00', '%d/%m/%Y %H:%M:%S')
data2 = datetime.strptime('27/05/1987 21:12:00', '%d/%m/%Y %H:%M:%S')
dif = data2 - data1
print(dif)

print(data2 > data1)
print(data2 < data1)
print(data2 == data1)
print(data2 != data1)
