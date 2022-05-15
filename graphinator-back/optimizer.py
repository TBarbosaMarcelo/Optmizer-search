import re

TABELAS = {
    "usuario": {
        "nome": "usuario",
        "colunas": ["idusuario", "nome", "logradouro", "numero", "bairro", "cep", "uf", "datanascimento"],
        "relac": []
    },
    "contas": {
        "nome": "contas",
        "colunas": ["idconta", "descricao", "tipoconta_idtipoconta", "usuario_idusuario", "saldoinicial"],
        "relac": []
    },
    "tipoconta": {
        "nome": "tipoconta",
        "colunas": ["idtipoconta", "descricao"],
        "relac": []
    },
    "movimentacao": {
        "nome": "movimentacao",
        "colunas": ["idmovimentacao", "datamovimentacao", "descricao", "tipomovimento_idtipomovimento", "categoria_idcategoria", "contas_idconta", "valor"],
        "relac": []
    },
    "tipomovimento": {
        "nome": "tipomovimento",
        "colunas": ["idtipomovimento", "descmovimentacao"],
        "relac": []
    },
    "categoria": {
        "nome": "categoria",
        "colunas": ["idcategoria", "descategoria"],
        "relac": []
    }
}

avb_tables = TABELAS.keys()
avb_columns = []

for tabela in TABELAS.keys():
    for column in TABELAS[tabela]["colunas"]:
        avb_columns.append(column)

# entrada = "SELECT idCategoria, desCategoria FROM Categoria JOIN movimentacao WHERE numero > 0 join alpha where bravo".lower()
# print(entrada)

def readCommand(entrada):
    print("\nCOMANDO: " + entrada)
    entrada = entrada.replace(";", "")

    try:
        tables_main = re.search('from (\w*) join', entrada).group(1)
        print("\n TABELA MAIN IDENTIFICADAS : "+ str(tables_main.split(", ")))
    except:
        return "Tabela N Encontrada", "0. ERROR"

    try:
        tables_join = re.search('join (.*) where', entrada).group(1).replace(" where", "")
        tables_join = tables_join.split("join")

        print("\n TABELA JOIN IDENTIFICADAS : "+ str(tables_join))
    except:
        return "Join N Encontrados", "0. ERROR"

    try:
        columns = re.search('select (.*) from', entrada).group(1)
        print("\n COLUNAS IDENTIFICADAS : "+str(columns.split(", ")))
    except:
        return "Colunas N Encontradas", "0. ERROR"

    try:
        where_cond = re.search('where (.*)', entrada).group(1).replace(" and", "x")
        where_cond = where_cond.split("x")
        print("\n CONDICIONAIS IDENTIFICADAS : "+ str(where_cond))
    except:
        return "Condições Não Encontradas", "0. ERROR"

    # Checando Existencia de Tabelas

    for table in tables_main.split(","):
        if table.strip() not in avb_tables:
            return f"SQL ERROR: Tabela '{table.strip()}' Não Identificada", "0. ERROR"
    
    for table in tables_join:
        table = table.strip().split(" ")[0]
        if table.strip() not in avb_tables:
            return f"SQL ERROR: Tabela '{table.strip()}' Não Identificada", "0. ERROR"
    
    for column in columns.split(","):
        if column.strip() not in avb_columns:
            return f"SQL ERROR: Coluna '{column.strip()}' Não Identificada", "0. ERROR"


    # Checando Existencia de Tabelas

    sepTabelas = {}
    sepConds = {}

    for tabela in tables_main.split(","):
        sepTabelas[tabela] = [TABELAS[tabela]["colunas"][0]]
        sepConds[tabela] = []
    
    for tabela in tables_join:
        tabela = tabela.strip().split(" ")[0]
        sepTabelas[tabela] = [TABELAS[tabela]["colunas"][0]]
        sepConds[tabela] = []

    for tabela in tables_main.split(","):
        for coluna in columns.split(","):
            if coluna.strip() in TABELAS[tabela]["colunas"]:
                sepTabelas[tabela].append(coluna.strip())
    
    for tabela in tables_join:
        tabela = tabela.strip().split(" ")[0]
        for coluna in columns.split(","):
            if coluna.strip() in TABELAS[tabela]["colunas"]:
                sepTabelas[tabela].append(coluna.strip()), "0. ERROR"
    
    print(sepTabelas)

    for tabela in sepConds.keys():
        for cond in where_cond:
            cond = cond.strip()
            if cond.split(" ")[0] in TABELAS[tabela]["colunas"]:
                sepConds[tabela].append(cond)

    print("\n", sepConds, "\n")

    saida_atual = "π " + columns + "\n" # + "(σ " + where_cond

    exec = []
    exec.append("π " + columns + "(nxt)")

    joins = ""
    for join in tables_join:
        joins += "("
    
    for i, tabela in enumerate(sepTabelas.keys()):
        if len(sepConds[tabela]):
            joins += "(π " + str(sepTabelas[tabela]).replace("[", "").replace("]", "").replace("'", "")

            joins += f"(σ {(' and '.join(sepConds[tabela])).replace('(', '').replace(')', '')} ({tabela})))\n"

            exec.insert(0, "π " + str(sepTabelas[tabela]).replace("[", "").replace("]", "").replace("'", "") + " (nxt)")
            exec.insert(0, f"(σ {(' and '.join(sepConds[tabela])).replace('(', '').replace(')', '')} ({tabela})))")
        else:
            joins += "(π " + str(sepTabelas[tabela]).replace("[", "").replace("]", "").replace("'", "") + f"({tabela}))"

            exec.insert(0, "π " + str(sepTabelas[tabela]).replace("[", "").replace("]", "").replace("'", "") + f"({tabela}))")

        if i >= len(tables_main.split(",")):
            joins += f" on {' '.join(tables_join[(len(sepTabelas.keys())-i)-1].split(' ')[2:])})\n"
        
        if i < len(sepTabelas.keys())-1:
            print(i, len(sepTabelas.keys())-1)
            joins += "|X|"
            exec.insert(0, "|X|(nxt)")

    saida_atual += joins

    aux = []
    exec.reverse()
    for i, e in enumerate(exec):
        aux.append(f"{i+1}. {e}\n")

    print("".join(aux))

    saida_atual = saida_atual.replace("and", "^")

    print("\nSAIDA: " + saida_atual)

    return saida_atual, "".join(aux)


# projecao π -> SELECT
# selecao σ -> WHERE
# ^ v -> AND OR
