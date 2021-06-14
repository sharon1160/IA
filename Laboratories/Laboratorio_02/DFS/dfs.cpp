#include<bits/stdc++.h>
#include <fstream>
using namespace std;

queue<string> frontier;
queue<string> reached;
queue<char> frontier2;
queue<char> reached2;

void clearC( queue<char> &q )
{
   queue<char> empty;
   swap( q, empty );
}

void clearS( queue<string> &q )
{
   queue<string> empty;
   swap( q, empty );
}

void printQueue(queue<string> q, ofstream &fichero)
{
  fichero<<"{";
	while (!q.empty()){
		fichero<<" "<<q.front();
		q.pop();
	}
	fichero<<" }"<<endl;
}

void sumarS(queue<string> &q, queue<string> &a)
{
  while (!a.empty()){
    q.push(a.front());
    a.pop();
  }
}

void sumarC(queue<char> &q, queue<char> &a)
{
  while (!a.empty()){
    q.push(a.front());
    a.pop();
  }
}

string ToString(char c)
{
  string s;
  s.push_back(c);
  return s;
}

string ToStringInt(int num)
{
  stringstream ss;
  ss<<num;
  string str = ss.str();
  return str;
}

class Graph
{
  public:
      map<char,vector<char>> adjList;
      void addEdge(char node1, char node2);
      map<char, int> depth(char node);
      void dfs(char start, char goal);
      void crearArchivoDot();
};

void Graph::addEdge(char node1, char node2)
{
  adjList[node1].push_back(node2);
  adjList[node2].push_back(node1);
}

map<char, int> Graph::depth(char start)
{
  map<char, int> depths;
  depths.insert({start,0});
  char current;
  queue<char> nodes;
  nodes.push(start);

  while(!nodes.empty())
  {
    current = nodes.front();
    nodes.pop();
    for (char node: adjList[current])
    {
      if(!depths[node] && (node != start))
      {
        depths[node] = depths[current] - 1;
        nodes.push(node);
      }
    }
  }
  return depths;
}

void Graph::dfs(char start, char goal)
{
  ofstream fichero("pasos_DFS.txt");
  
  fichero<<"DFS - Nodo seleccionado "<<goal<<endl;
  fichero<<"Alumna: Sharon Chullunquía Rosas "<<endl;
  fichero<<endl;
  int paso = 1;
  map<char, bool> visited;
  map<char, int> depths = depth(start);
  char node = start;
  if(node == goal){
      fichero<<goal<<endl;
      return;
  }

  frontier.push(ToString(start)+"("+ToStringInt(depths[start])+")");
  //reached.push(ToString(start)+"("+ToStringInt(depth)+")");
  frontier2.push(start);
  //reached2.push(start);

  fichero<<"Paso "<<paso<<endl;
  fichero<<"Frontier = ";
  printQueue(frontier,fichero);
  fichero<<"Reached = ";
  printQueue(reached,fichero);
  fichero<<"--------------------------------------------------------------------------------------------";
  fichero<<endl;

  visited[start] = true;
  while(!frontier2.empty()){
      node = frontier2.front();
      frontier.pop();
      frontier2.pop();
      queue<char> f2 = frontier2;
      queue<string> f = frontier;

      clearS(frontier);
      clearC(frontier2);

   
      reached2.push(node);
      reached.push(ToString(node)+"("+ToStringInt(depths[node])+")");
      
      for(char vecino: adjList[node])
      {
          if(!visited[vecino])
          {
              frontier2.push(vecino);
              frontier.push(ToString(vecino)+"("+ToStringInt(depths[vecino])+")");
              visited[vecino] = true;
          }
      }
      sumarC(frontier2,f2);
      sumarS(frontier,f);

      paso++;
      fichero<<endl;
      fichero<<"Paso "<<paso<<endl;
      fichero<<"Frontier = ";
      printQueue(frontier,fichero);
      fichero<<"Reached = ";
      printQueue(reached,fichero);
      fichero<<"--------------------------------------------------------------------------------------------";
      fichero<<endl;

      if(node == goal){
        fichero<<"\n"<<node<<endl;
        return;
      }
  }
  fichero.close();
}

void Graph::crearArchivoDot(){
  ofstream salida;
  string nombreArchivo = "DFS"; 
  map<char, bool> visited;
  salida.open(nombreArchivo + ".dot", ios::out);
  if (salida.is_open()){
      salida << "graph ";
      salida << nombreArchivo << " {\n";
      visited[reached2.front()] = true;
      while (!reached2.empty()){
          for(char vecino: adjList[reached2.front()]){
              if(!visited[vecino]){
                  salida<<reached2.front()<<" -- "<<vecino<<";\n";
                  visited[vecino] = true;
              }
          }
          reached2.pop();
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

    g.dfs('A','S');
    // Arbol final
    g.crearArchivoDot();
  
    return 0;
}