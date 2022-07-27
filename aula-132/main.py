from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

# Configurando localização de acordo com o sistema operacional
setlocale(LC_ALL, '')

# Configurando para padrão brasileiro
setlocale(LC_ALL, 'pt_BR.utf-8')

# Capturando a data atual
date_now = datetime.now()

# Formatando a data
date_format = date_now.strftime('%A, %d de %B de %Y')
print(date_format)

# Capturando o último dia do mês
month = int(date_now.strftime('%m'))

# mdays é uma lista
print(type(mdays))

print('O último dia do mês é {}'.format(mdays[month]))
