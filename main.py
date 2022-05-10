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


entrada = "SELECT idCategoria, desCategoria FROM Categoria JOIN movimentacao WHERE numero > 0".lower()
# print(entrada)

def readCommand(entrada):
    print("\nCOMANDO: " + entrada)

    tables = re.search('from (.*)', entrada).group(1).replace(" join", ",")
    print("\n TABELAS IDENTIFICADAS : "+ str(tables.split(", ")))

    columns = re.search('select (.*) from', entrada).group(1)
    print("\n COLUNAS IDENTIFICADAS : "+str(columns.split(", ")))

    where_cond = re.search('from (.*)', entrada).group(1).replace(" join", ",")
    print("\n TABELAS IDENTIFICADAS : "+ str(where_cond.split(", ")))

    tabelaExiste = False
    for tabela in TABELAS:
        if tabela["nome"].lower() in tables.split(", "):
            tabelaExiste = True
            print("tabela identificada\n")
            for coluna in columns.split(","):
                if coluna.strip() not in tabela["colunas"]:
                    print(f"coluna '{coluna.strip()}' NAO ASLKDNSLAJKND em '{tabela['nome']}'")
                else:
                    print(f"coluna '{coluna.strip()}' EXISTE em '{tabela['nome']}'")
    if not tabelaExiste:
        print("Tabela Não EXISTE")

    
    
    saida_atual = "π " + columns + "(" + " (" + tables + "))"
    print("\nSAIDA: " + saida_atual)
    #conditionals = re.search('where(.*)', entrada).group(1)
    #print("\n CONDIÇÕES IDENTIFICADAS : "+conditionals)

#saida_atual = "π" + columns + "(σ" + conditionals + " (" + tables1|X| tabela2 + "))"

saida_ideal = "π COLUNA1, COLUNA2(σ SEXO=M(TABELA1))".lower()


readCommand(entrada)


# projecao π -> SELECT
# selecao σ -> WHERE
# ^ v -> AND OR
