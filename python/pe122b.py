import collections

def doublesum(S):
    return set([p+q for p in S for q in S])

class sumtree:    
    def __init__(self):
        self.root=treenode(None,1)
        self.index={}

    def __iter__(self): #breadth-first search through tree
        nodequeue=collections.deque()
        nodequeue.append(self.root)
        while(len(nodequeue)>0):
            node=nodequeue.popleft()
            yield node
            for child in node.children:
                nodequeue.append(child)

    def levels(self): #yields lists of nodes, where each node is a level of the tree
        level=[self.root]
        while level!=[]:
            yield level
            level=reduce(lambda a,b:a+b,[node.children for node in level])

    def add(self,n): #assume 2...n-1 have already been added, otherwise, trouble
        if n in self.index:
            return false
        else:
            self.index[n]=[]
        for level in self.levels():
            for node in level:
                if n in doublesum(node.pathdata()):
                    new=treenode(node,n)
                    self.index[n].append(new)
            if self.index[n]!=[]: break
        return self.k(n)

    def k(self,n):
        return min([len(node.pathdata())-1 for node in self.index[n]])
            
    
class treenode:
    def __init__(self,parent,data):
        self.parent=parent
        self.data=data
        self.children=[]
        if self.parent!=None: self.parent.children.append(self)

    def pathdata(self):
        node=self
        path=[]
        while node:
            path+=[node.data]
            node=node.parent
        path.reverse()
        return path
                

    


def main():
    tree=sumtree()
    total=0
    for n in xrange(2,201):
        total+=tree.add(n)
    print total
    

def test():
    tree=sumtree()
    total=0
    for n in xrange(2,201):
        total+=tree.add(n)
        print n,tree.k(n),tree.index[n][0].pathdata()
    print total
    
test()
