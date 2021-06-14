#include<queue>
#include<fstream>
#include<map>
using namespace std;

queue<char> open;
queue<char> closed;

queue<char> purgar(queue<char> &open, char node)
{
    queue<char> nQueue;
    while(!open.empty()){
        if(open.front() != node)
            nQueue.push(open.front());
        open.pop();
    }
    return nQueue;
}

void printQueue(queue<char> q, ofstream &fichero, map<char,int> heuristic)
{
    fichero<<"{";
	while (!q.empty()){
		fichero<<" "<<q.front()<<"("<<heuristic[q.front()]<<")";
		q.pop();
	}
	fichero<<" }"<<endl;
}

char min(queue<char> q, map<char,int> heuristic)
{
    int min = heuristic[q.front()];
    char mink = q.front();
    while(!q.empty()){
        if(min > heuristic[q.front()]){
            min = heuristic[q.front()];
            mink = q.front();
        }
        q.pop();
    }
    return mink;
}

class Graph
{
    private:
        bool EsDirigido;
        map<char,vector<char>> adjList;
        map<char,int> heuristic;
    public:
        void addEdge(char node1, char node2);
        void addHeu(char node, int value);
        void gbfs(char start, char goal);
        void crearArchivoDot();
        Graph(bool _EsDirigido)
        {
            bool EsDirigido = _EsDirigido;
        }
};


void Graph::addEdge(char node1, char node2)
{
    adjList[node1].push_back(node2);
    if(!EsDirigido)
        adjList[node2].push_back(node1);
}

void Graph::addHeu(char node, int value)
{
    heuristic[node] = value;
}

void Graph::gbfs(char start, char goal)
{
    ofstream fichero("iteraciones_GBFS.txt");
    map<char, bool> visited;
    bool find = false;

    fichero<<"Greedy Best-First Search"<<endl;
    fichero<<"Alumna: Sharon Chullunquía Rosas "<<endl;
    fichero<<"Nodo Buscado: "<<goal<<endl;
    fichero<<"--------------------------------------------------------------------------------------------"<<endl;
    fichero<<endl;

    open.push(start);
    visited[start] = true;

    fichero<<"Open = ";
    printQueue(open,fichero,heuristic);
    fichero<<"Closed = ";
    printQueue(closed,fichero,heuristic);
    fichero<<endl;
    fichero<<"--------------------------------------------------------------------------------------------"<<endl;
    fichero<<endl;

    int it = 1;
    char node;
    while(!open.empty()){
        fichero<<"Iteración "<<it<<endl;
        node = min(open,heuristic);
        open = purgar(open, node);
        closed.push(node);

        fichero<<"Open = ";
        printQueue(open,fichero,heuristic);
        fichero<<"Closed = ";
        printQueue(closed,fichero,heuristic);
        fichero<<endl;

        if(node == goal){
            find = true;
            break;
        }
        else{
            for(char vecino: adjList[node])
            {
                if(vecino == goal){
                    closed.push(vecino);
                    fichero<<"Open = ";
                    printQueue(open,fichero,heuristic);
                    fichero<<"Closed = ";
                    printQueue(closed,fichero,heuristic);
                    fichero<<endl;
                    find = true;
                    break;
                }
                else if(!visited[vecino])
                {
                    open.push(vecino);
                    visited[vecino]=true;
                }
                fichero<<"Open = ";
                printQueue(open,fichero,heuristic);
                fichero<<"Closed = ";
                printQueue(closed,fichero,heuristic);
                fichero<<endl;
            }
            fichero<<"--------------------------------------------------------------------------------------------"<<endl;
            fichero<<endl;
            visited[node]=true;
        }
        if(find) break;
        it++;
    }
    fichero<<"Se encontró el elemento "<<endl;
    fichero<<"Camino Final = ";
    printQueue(closed,fichero,heuristic);
    fichero.close();
}

int main()
{   
    bool EsDirigido = true;
    Graph g(EsDirigido);
    g.addEdge('M', 'Y');
    g.addEdge('M', 'P');
    g.addEdge('Y', 'L');
    g.addEdge('Y', 'X');
    g.addEdge('P', 'R');
    g.addEdge('P', 'N');
    g.addEdge('L', 'Z');
    g.addEdge('X', 'Z');
    g.addEdge('R', 'W');
    g.addEdge('N', 'W');
    g.addEdge('Z', 'Q');
    g.addEdge('W', 'Q');

    g.addHeu('M',10);
    g.addHeu('Y',8);
    g.addHeu('P',6);
    g.addHeu('L',5);
    g.addHeu('X',7);
    g.addHeu('R',5);
    g.addHeu('N',3);
    g.addHeu('Z',3);
    g.addHeu('W',1);
    g.addHeu('Q',0);

    g.gbfs('M','Q');
  
    return 0;
}