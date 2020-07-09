package br.com;

import br.com.tarefas.ArrayTarefas;
import br.com.tarefas.Tarefa;

public class App {
    
    public static void main(String[] args) {
        // String nome = "Ian";
        // System.out.println("Hello Codenation " + nome);

        System.out.println("Minhas tarefas");
        System.out.println("---------------------");

        ArrayTarefas tarefas = new ArrayTarefas(3);
        Tarefa tarefa1 = new Tarefa ( "Regar as Plantas");
        Tarefa tarefa2 = new Tarefa ( "Estudar");
        Tarefa tarefa3 = new Tarefa ( "Trabalhar");
        tarefas.adicionar(tarefa1);
        tarefas.adicionar(tarefa2);
        tarefas.adicionar(tarefa3);
        tarefas.exibirTarefas();
    }
}

