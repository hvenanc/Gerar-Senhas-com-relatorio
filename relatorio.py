import os

def relatorio(index,password):
    if not os.path.exists("Relatorio_DB.csv"):
        file = open("Relatorio_DB.csv", "w+")
        with open("Relatorio_DB.csv", "a", encoding="utf-8") as file:
            file.write(
                f"Index,Senha\n"
            )
        file.close()
        
    with open("Relatorio_DB.csv", "a", encoding="utf-8") as file:
            file.write(
                f"{index},{password}"
                f"\n"
        )