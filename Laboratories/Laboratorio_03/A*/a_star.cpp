#include<iostream>
#include<map>
#include<algorithm>
#include<vector>
#include<fstream>
#include<string>
using namespace std;

class Graph{
public:
  map<char,map<char, int>> graph;

  void connect(char a, char b, int distance){
    graph[a][b]=distance;
  }

  int get(char a, char b){
    return graph[a][b];
  }

  map<char, int> get(char a){
    return graph[a];
  }
};

class Node{
  public:
    char name;
    Node* parent;
    int f, g, h;
    Node(char _name){
      name = _name;
      parent = nullptr;
      f = 0;
      g = 0;
      h = 0;
    }

    bool operator==(Node other){
      return name == other.name;
    }

    bool operator<(Node other){
      return f < other.f;
    }


};

vector<Node*> path(Node* a, Node* b){
  vector<Node*> result;
  Node* temp = a;
  while (!(temp == b)) {
    result.push_back(temp);
    temp = temp->parent;
  
  }
  result.push_back(b);
  reverse(result.begin(), result.end());

  return result;
}

string printPath(vector<Node*> nodes){
  string s = "";
  for (int i=0; i<nodes.size()-1; i++) {
    s+=nodes[i]->name;
  }
  return s;

}

void print(vector<Node*> nodes, Node* startNode, ofstream &fichero){
  fichero<<"{ ";
  for(auto element : nodes) {
    fichero << element->name << "-("<<printPath(path(element,startNode))<<")("
         << element->g << ", " << element->h <<", " << element->f << ") ";
  }
  fichero<<"}";
  fichero<<endl;
}

int minimo(vector<Node*> open)
{
  int pos = 0;
  int minf = open[0]->f;

  for(int i=1; i< open.size(); i++)
  {
    if(open[i]->f < minf)
    {
      pos = i;
    }
  }
  return pos;
}

void aStar(Graph g, map<char, int> heuristics, char start, char goal){
  ofstream fichero("iteraciones_A_star.txt");
  fichero<<"A*"<<endl;
  fichero<<"Alumna: Sharon Chullunquía Rosas"<<endl;
  fichero<<"Nodo Buscado: "<<goal<<endl;
  fichero<<"--------------------------------------------------------------------------------------------"<<endl;

  vector<Node*> open;
  vector<Node*> closed;
  Node* startNode = new Node(start);
  Node* goalNode = new Node(goal);

  startNode->g = 0;
  startNode->h = heuristics[startNode->name];
  startNode->f = startNode->g + startNode->h;

  open.push_back(startNode);

  fichero<<endl;
  fichero<<"Open = ";
  print(open, startNode,fichero);
  fichero<<"Closed = ";
  print(closed, startNode,fichero);
  fichero<<"--------------------------------------------------------------------------------------------"<<endl;
  fichero<<endl;

  int count = 1;
  
  while(!open.empty()){

    int min = minimo(open);

    Node* currentNode = open[min];

    fichero<<"Iteración "<<count<<endl;

    if(currentNode->name == goalNode->name){
      fichero<<"Se encontró el elemento"<<endl;
      fichero<<"Open = ";
      print(open, startNode,fichero);
      fichero<<"Closed = ";
      print(closed, startNode,fichero);
      fichero<<"--------------------------------------------------------------------------------------------"<<endl;
      fichero<<endl;

      fichero<<"Camino Final: ";
      for(auto element: closed){
        fichero<<element->name<<" -> ";
      }
      fichero<<goalNode->name<<endl;
      fichero<<endl;
      return;
    }
    
    open.erase(open.begin()+min);
    closed.push_back(currentNode);

    map<char, int> vecinos = g.graph[currentNode->name];

    
    for(auto element : vecinos){
      Node* vecino = new Node(element.first);
      vecino->parent = currentNode;
      vecino->g = currentNode->g + g.get(currentNode->name, vecino->name);
      vecino->h = heuristics[vecino->name];
      vecino->f = vecino->g +vecino->h;

      bool flag = false;
      for(auto element: open){
        if(vecino == element){
          flag = true;
          break;
        }
      }

      if(flag==false){ 
        open.push_back(vecino);
      }
      for(auto element: open){ 
        if(vecino == element && vecino->f < element->f){
          open.push_back(vecino);
          break;
        }
      }
      fichero<<"Open = ";
      print(open, startNode,fichero);
      fichero<<"Closed = ";
      print(closed, startNode,fichero);
      fichero<<endl;
    
    }
    fichero<<"--------------------------------------------------------------------------------------------"<<endl;
    fichero<<endl;
    count++;

  }

}

int main(){
  Graph g;
  g.connect('M', 'Y', 6);
  g.connect('M', 'P', 3);
  g.connect('Y', 'L', 3);
  g.connect('Y', 'X', 2);
  g.connect('P', 'R', 1);
  g.connect('P', 'N', 7);
  g.connect('L', 'Z', 5);
  g.connect('X', 'Z', 8);
  g.connect('R', 'W', 3);
  g.connect('N', 'W', 2);
  g.connect('Z', 'Q', 5);
  g.connect('W', 'Q', 3);

  map<char,int> heuristics;
  heuristics['M'] = 10;
  heuristics['Y'] = 8;
  heuristics['P'] = 6;
  heuristics['L'] = 5;
  heuristics['X'] = 7;
  heuristics['R'] = 5;
  heuristics['N'] = 3;
  heuristics['Z'] = 3;
  heuristics['W'] = 1;
  heuristics['Q'] = 0;

  char start, goal;

  start = 'M';
  goal = 'Q';

  aStar(g,heuristics,start,goal);
  return 0;
}