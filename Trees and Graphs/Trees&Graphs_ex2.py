def add_edge(adj, src, dest):
 
    adj[src].append(dest);
    adj[dest].append(src);







def Modifed_BFS(adj, src, dest, v, pred, dist):

    queue = []
    visited = [False for i in range(v)]

    for i in range(v):
        dist[i] = 1000000
        pred[i] = -1

    #NORMAL BFS
    #updaing first node which is src
    visited[src] = True
    dist[src] = 0
    queue.append(src)


    while(len(queue) != 0):
        node = queue.pop()
        #neighbhours of node
        for neighbor in adj[node] :
            if visited[neighbor] == False:
                visited[neighbor] = True
                dist[neighbor] = dist[node] + 1
                pred[neighbor] = node
                queue.append(neighbor)

            if neighbor == dest:
                return True
            
    return False





if __name__=='__main__':
     
    # no. of vertices
    v = 8;
  
    # array of vectors is used to store the graph
    # in the form of an adjacency list
    adj = [[] for i in range(v)];
  
    # Creating graph given in the above diagram.
    # add_edge function takes adjacency list, source
    # and destination vertex as argument and forms
    # an edge between them.
    add_edge(adj, 0, 1);
    add_edge(adj, 0, 3);
    add_edge(adj, 1, 2);
    add_edge(adj, 3, 4);
    add_edge(adj, 3, 7);
    add_edge(adj, 4, 5);
    add_edge(adj, 4, 6);
    add_edge(adj, 4, 7);
    add_edge(adj, 5, 6);
    add_edge(adj, 6, 7);
    source = 0
    dest = 7;


    #Code starts here
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)]
    
    if (Modifed_BFS(adj, source, dest, v, pred, dist) == False):
        print("Given source and destination are not connected")



    path = []
    curr = dest
    path.append(curr)

    while(pred[curr] != -1):
        path.append(pred[curr])
        curr = pred[curr]


    #reverse the path array to make it from src to dest

    path.reverse()

    print("Shortest path length is : " + str(dist[dest]), end = '\n')
    print(f"And the path is : {path} ")
