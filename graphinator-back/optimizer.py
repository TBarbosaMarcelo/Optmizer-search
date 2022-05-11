import re

TABELAS = [
    {
        "nome": "usuario",
        "colunas": ["idusuario", "nome", "logradouro", "numero", "bairro", "cep", "uf", "datanascimento"],
        "relac": []
    },
    {
        "nome": "contas",
        "colunas": ["idconta", "descricao", "tipoconta_idtipoconta", "usuario_idusuario", "saldoinicial"],
        "relac": []
    },
    {
        "nome": "tipoconta",
        "colunas": ["idtipoconta", "descricao"],
        "relac": []
    },
    {
        "nome": "movimentacao",
        "colunas": ["idmovimentacao", "datamovimentacao", "descricao", "tipomovimento_idtipomovimento", "categoria_idcategoria", "contas_idconta", "valor"],
        "relac": []
    },
    {
        "nome": "tipomovimento",
        "colunas": ["idtipomovimento", "descmovimentacao"],
        "relac": []
    },
    {
        "nome": "categoria",
        "colunas": ["idcategoria", "descategoria"],
        "relac": []
    }
]


# entrada = "SELECT idCategoria, desCategoria FROM Categoria JOIN movimentacao WHERE numero > 0 join alpha where bravo".lower()
# print(entrada)

def readCommand(entrada):
    print("\nCOMANDO: " + entrada)
    entrada = entrada.replace(";", "")

    try:
        tables_main = re.search('from (.*) join', entrada).group(1)
        print("\n TABELA MAIN IDENTIFICADAS : "+ str(tables_main.split(", ")))
    except:
        return "Tabela N Encontrada"

    try:
        tables_join = re.search('join (.*) where', entrada).group(1)
        print("\n TABELA JOIN IDENTIFICADAS : "+ str(tables_join.split(", ")))
    except:
        return "Join N Encontrados"

    try:
        columns = re.search('select (.*) from', entrada).group(1)
        print("\n COLUNAS IDENTIFICADAS : "+str(columns.split(", ")))
    except:
        return "Colunas N Encontradas"

    try:
        where_cond = re.search('where (.*)', entrada).group(1).replace(" join", ",")
        print("\n CONDICIONAIS IDENTIFICADAS : "+ str(where_cond.split(", ")))
    except:
        return "Condições Não Encontradas"

    tabelaExiste = False
    for tabela in TABELAS:
        if tabela["nome"].lower() in tables_main.split(", "):
            tabelaExiste = True
            print("tabela identificada\n")
            for coluna in columns.split(","):
                if coluna.strip() not in tabela["colunas"]:
                    print(f"coluna '{coluna.strip()}' NAO ASLKDNSLAJKND em '{tabela['nome']}'")
                else:
                    print(f"coluna '{coluna.strip()}' EXISTE em '{tabela['nome']}'")
    if not tabelaExiste:
        print("Tabela Não EXISTE")

    
    
    saida_atual = "π " + columns + "(σ " + where_cond +" (" + tables_main+ "|X|"+ tables_join + "))"
    print("\nSAIDA: " + saida_atual)
    #conditionals = re.search('where(.*)', entrada).group(1)
    #print("\n CONDIÇÕES IDENTIFICADAS : "+conditionals)

    return saida_atual

#saida_atual = "π" + columns + "(σ " + conditionals + " (" + tables1|X| tabela2 + "))"

# saida_ideal = "π COLUNA1, COLUNA2(σ SEXO=M(TABELA1))".lower()


# readCommand(entrada)


# projecao π -> SELECT
# selecao σ -> WHERE
# ^ v -> AND OR
