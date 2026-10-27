from flask import Flask, redirect, request, url_for, render_template
import json

app = Flask(__name__)

@app.route("/concluir", methods=["POST"])
def concluir():
    titulo_tarefa = request.form.get("titulo")
    
    try:
        with open("tarefas.json", "r", encoding="utf-8") as f:
            lista_tarefas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_tarefas = []
        
    for tarefa in lista_tarefas:
        if tarefa.get("titulo") == titulo_tarefa:
            tarefa["status"] = "concluído"
            break  
            
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(lista_tarefas, f, ensure_ascii=False, indent=4)
        
    return redirect(url_for("home"))

@app.route("/desconcluir", methods=["POST"])
def desconcluir():
    titulo_tarefa = request.form.get("titulo")
    
    try:
        with open("tarefas.json", "r", encoding="utf-8") as f:
            lista_tarefas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_tarefas = []
        
    for tarefa in lista_tarefas:
        if tarefa.get("titulo") == titulo_tarefa:
            tarefa["status"] = "Pendente"
            break  
            
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(lista_tarefas, f, ensure_ascii=False, indent=4)
        
    return redirect(url_for("home"))


@app.route("/")
def home():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as f:
            lista_tarefas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_tarefas = []
        
    return render_template("index.html", tarefas=lista_tarefas)

@app.route("/formulario", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        first_name = request.form.get("fname")
        status = request.form.get("status")
        
        nova_tarefa = {"titulo": first_name, "status": status}
        
        try:
            with open("tarefas.json", "r", encoding="utf-8") as f:
                lista_tarefas = json.load(f)
            if not isinstance(lista_tarefas, list):
                lista_tarefas = []
        except (FileNotFoundError, json.JSONDecodeError):
            lista_tarefas = []

        lista_tarefas.append(nova_tarefa)
        
        with open("tarefas.json", "w", encoding="utf-8") as f:
            json.dump(lista_tarefas, f, ensure_ascii=False, indent=4)
            
        return redirect(url_for("home"))
        
    return render_template("form.html")


@app.route("/deletar", methods=["POST"])
def deletar():
    titulo_para_apagar = request.form.get("titulo")
    
    try:
        with open("tarefas.json", "r", encoding="utf-8") as f:
            lista_tarefas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_tarefas = []
        
    lista_tarefas = [t for t in lista_tarefas if t.get("titulo") != titulo_para_apagar]
    
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(lista_tarefas, f, ensure_ascii=False, indent=4)
        
    return redirect(url_for("home"))