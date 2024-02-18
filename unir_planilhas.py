####################
# UNINDO PLANILHAS #
####################

# Biblioteca utilizada: pandas
# OBS: Caso não tenha a biblioteca instalada, executar o comando "pip install pandas" no terminal

# Importando biblioteca pandas
import pandas as pd

# Carregando os dados das duas planilhas
funcionarios_sul = pd.read_excel('Funcionarios_Sede_Sul.xlsx')
funcionarios_norte = pd.read_excel('Funcionarios_Sede_Norte.xlsx')

# Realizando a união dos dados
funcionarios_consolidado = pd.concat([funcionarios_sul, funcionarios_norte])

# Exibe os dados unidos
print(funcionarios_consolidado)

# Salva os dados unidos em uma nova planilha
funcionarios_consolidado.to_excel('Funcionarios_Consolidado.xlsx', index=False)
