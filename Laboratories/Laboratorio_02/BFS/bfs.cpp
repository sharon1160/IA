#include<bits/stdc++.h>
#include <fstream>
using namespace std;

queue<char> frontier;
queue<char> reached;

void printQueue(queue<char> q, ofstream &fichero)
{
    fichero<<"{";
	while (!q.empty()){
		fichero<<" "<<q.front();
		q.pop();
	}
	fichero<<" }"<<endl;
}

class Graph
{
    public:
        map<char,vector<char>> adjList;
        void addEdge(char node1, char node2);
        void bfs(char start, char goal);
        void crearArchivoDot();
};

void Graph::addEdge(char node1, char node2)
{
    adjList[node1].push_back(node2);
    adjList[node2].push_back(node1);
}

void Graph::bfs(char start, char goal)
{
    ofstream fichero("pasos_BFS.txt");

    fichero<<"BFS - Nodo seleccionado "<<goal<<endl;
    fichero<<"Alumna: Sharon Chullunquía Rosas "<<endl;
    fichero<<endl;
    int paso = 1;
    map<char, bool> visited;
    char node = start;
    if(node == goal){
        fichero<<goal<<endl;
        return;
    }

    frontier.push(start);
    reached.push(start);

    fichero<<"Paso "<<paso<<endl;
    fichero<<"Frontier = ";
    printQueue(frontier,fichero);
    fichero<<"Reached = ";
    printQueue(reached,fichero);
    fichero<<"--------------------------------------------------------------------------------------------";
    fichero<<endl;

    visited[start] = true;
    while(!frontier.empty()){
        node = frontier.front();
        frontier.pop();

        for(char vecino: adjList[node])
        {
            if(!visited[vecino])
            {
                reached.push(vecino);
                frontier.push(vecino);
                visited[vecino] = true;
            }
            if(vecino == goal)
            {
                fichero<<endl;
                fichero<<node<<"->"<<vecino<<endl;
                fichero.close();
                return;
            } 
        }
        paso++;
        fichero<<endl;
        fichero<<"Paso "<<paso<<endl;
        fichero<<"Frontier = ";
        printQueue(frontier,fichero);
        fichero<<"Reached = ";
        printQueue(reached,fichero);
        fichero<<"--------------------------------------------------------------------------------------------";
        fichero<<endl;
    }
    fichero.close();
}

// Funcion para graficar el grafo
void Graph::crearArchivoDot(){
    ofstream salida;
    string nombreArchivo = "BFS"; 
    map<char, bool> visited;
    salida.open(nombreArchivo + ".dot", ios::out);
    if (salida.is_open()){
        salida << "graph ";
        salida << nombreArchivo << " {\n";
        visited[reached.front()] = true;
        while (!reached.empty()){
            for(char vecino: adjList[reached.front()]){
                if(!visited[vecino]){
                    salida<<reached.front()<<" -- "<<vecino<<";\n";
                    visited[vecino] = true;
                }
            }
            reached.pop();
        }
        salida << "}\n";
        salida.close();
        string comando = "dot " + nombreArchivo + ".dot -o " + nombreArchivo + ".pdf -Tpdf";
        system(comando.c_str());
    }else{
        cout << endl << "No se pudo crear archivo" << endl;
    }
}


int main()
{
    Graph g;
    g.addEdge('A', 'B');
    g.addEdge('A', 'C');
    g.addEdge('B', 'D');
    g.addEdge('B', 'E');
    g.addEdge('C', 'F');
    g.addEdge('C', 'G');
    g.addEdge('E', 'H');
    g.addEdge('G', 'I');
    g.addEdge('G', 'J');

    g.bfs('A','S');
    // Arbol final
    g.crearArchivoDot();
  
    return 0;
}