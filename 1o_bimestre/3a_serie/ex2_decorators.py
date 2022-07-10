def table_env_decorate(funcao):
    def table_environment(infos, row):
        print("\\begin{table}[h]")
        funcao(infos, rows)
        print("\\end{table}")
    return table_environment


def infos_decorate(funcao):
    def table_information(infos, rows):
        for info in infos:
            print("\t" + info)
        funcao(infos, rows)
    return table_information


@table_env_decorate
@infos_decorate
def create_table(infos, rows):
    print("\t\\begin{tabular}{cc}")
    print("\t\t\\toprule")
    for produto, preco in rows.items():
        print("\t\t", produto, "&", preco, "\\\\")
    print("\t\t\\bottomrule")
    print("\t\\end{tabular}")

infos = ["\\centering",
         "\\caption{Table title}",
         "\\label{tab:product_prices}"]

rows = {"Product" : "Price",
              "A" : "5",
              "B" : "10"}

create_table(infos, rows)