import sys
import math
import copy
import time
import os
import resource


def swapped(arr,init,end):
    arr = list(arr)
    arr[init],arr[end] = arr[end],arr[init]
    return arr

class boardMap:

    class node:

        def __init__(self,config,n,parent=None):
            self.size = len(config)
            if (math.sqrt(self.size) - round(math.sqrt(self.size)) != 0) or (math.sqrt(self.size) < 2) or (sorted(config) != list(range(0,self.size))):
                self.game = False
            else:
                self.game = True
                m = int(math.sqrt(n))
                self.config = config
                cost = 0
                for i in range(1,n):
                    pos = self.config.index(i)
                    cost += abs(i%m - pos%m) + abs(int(i/m) - int(pos/m))
                self.cost = cost
                self.parent = parent
                self.depth = 0
                self.moves = []
                self.children = []
                self.parent = None
                self.parentMove = None
                pos = self.config.index(0)
                if pos > -1:
                    if pos not in list(range(0,m)):
                        (self.moves).append({ 'move':'UP','value':-m })
                    if pos not in list(range(n-m-1,n)):
                        (self.moves).append({ 'move':'DOWN','value':m })
                    if pos not in list(range(0,n,m)):
                        (self.moves).append({ 'move':'LEFT','value':-1 })
                    if pos not in list(range(m-1,n,m)):
                        (self.moves).append({ 'move':'RIGHT','value':1 })


    def insertChildren(self,tree,pre,stack,n,fontier=None,action=None):

        self.cost = self.cost + 1

        for i in tree.moves:
            temp = swapped(tree.config,tree.config.index(0),tree.config.index(0) + i['value'])
            if ''.join(list(map(str,temp))) not in pre:
                pre.add(''.join(list(map(str,temp))))
                a = self.node(temp,n)
                a.parent = tree
                a.depth = tree.depth + 1
                if a.depth > self.depth:
                    self.depth = a.depth
                a.parentMove = i['move']
                (tree.children).append(a)
                stack.append(a)
                if fontier != None:
                    fontier.append(a.cost + a.depth)
        if fontier != None:
            if len(fontier) != 0:
                return fontier.index(min(fontier))

    def __init__(self,startNode,n,cost=0):
        self.root = self.node(startNode,n)
        self.maps = set()
        self.cost = cost
        self.depth = 0

    def astar(self,n):
        self.maps.add(''.join(list(map(str,self.root.config))))
        stack = [ self.root ]
        fontier = [self.root.cost]
        action = 0
        while stack != []:
            a = stack.pop(action)
            fontier.pop(action)
            if a != None:
                if a.config == list(range(0,n)):
                    ans = { }
                    cost = 0
                    path = []
                    ans['max_search_depth'] = self.depth
                    while a != self.root:
                        cost = cost + 1
                        path.append(a.parentMove)
                        a = a.parent
                    ans['path_to_goal'] = list(reversed(path))
                    ans['nodes_expanded'] = self.cost
                    ans['cost_of_path'] = cost
                    ans['running_time'] = time.time() - start
                    return ans
            action = self.insertChildren(a,self.maps,stack,n,fontier,action)



state = [8,6,4,2,1,3,5,7,0 ]
start = time.time()
ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
game = boardMap(state,9)
ans = None
if(game.root.game == True):
    
    ans = game.astar(9)

    print(ans)


else:
    print('Game not initialised')
