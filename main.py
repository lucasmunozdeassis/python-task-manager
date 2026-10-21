from classes import IncluirTarefa,listatarefas
import json

while True:
    tarefa = input("Insira a tarefa (ou digite 'sair' para terminar): ")
    
    if tarefa.lower() == 'sair':
        break
        
    statustarefa = input("Insira o status desta tarefa: ")
    
    IncluirTarefa.incluir(tarefa, statustarefa)
    print("Tarefa adicionada com sucesso!\n")

print("\nLista final de tarefas:")
print(listatarefas)

with open("tarefas.txt", "w", encoding="utf-8") as arquivo_txt:
    json.dump(listatarefas, arquivo_txt, ensure_ascii=False, indent=4)

print("Arquivo 'listatarefas.txt' criado com sucesso!")