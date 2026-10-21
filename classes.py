
listatarefas = {}

class IncluirTarefa:
    def __init__(self, tarefa, status):
        self.tarefa = tarefa
        self.status = status

    @staticmethod
    def incluir(tarefa, status):
        listatarefas[tarefa] = status

