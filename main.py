import re


entrada = "SELECT COLUNA1,COLUNA2 FROM TABELA1".lower()
# print(entrada)


columns = re.search('select(.*)from', entrada).group(1)
print("\n COLUNAS IDENTIFICADAS : "+columns)

if("join" in entrada):
    tables = re.search('from(.*)inner', entrada).group(1)
    print("\n TABELAS IDENTIFICADAS : "+tables)

    
    conditionals = re.search('on(.*)', entrada).group(1)
    print("\n CONDIÇÕES IDENTIFICADAS : "+conditionals)

else:
    tables = re.search('from(.*)where', entrada).group(1)
    print("\n TABELAS IDENTIFICADAS : "+tables)

    conditionals = re.search('where(.*)', entrada).group(1)
    print("\n CONDIÇÕES IDENTIFICADAS : "+conditionals)

saida_atual = "π" + columns + "(σ" + conditionals + " (" + tables + "))"
saida_ideal = "π COLUNA1, COLUNA2(σ SEXO=M(TABELA1))".lower()
print("\n VERSAO ALGEBRICA: "+ saida_atual)
# projecao π -> SELECT
# selecao σ -> WHERE
# ^ v -> AND OR
