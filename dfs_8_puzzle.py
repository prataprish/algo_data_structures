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

class boardMap: #tree containing possible solutions

    class node: #node structure for tree

        def __init__(self,config,parent=None):
            self.size = len(config)
            if (math.sqrt(self.size) - round(math.sqrt(self.size)) != 0) or (math.sqrt(self.size) < 2) or (sorted(config) != list(range(0,self.size))):
                self.game = False
            else:
                self.game = True
                self.config = config
                self.parent = parent
                self.depth = 0
                self.moves = []
                self.children = []
                self.parent = None
                self.parentMove = None
                pos = self.config.index(0) # choose priority for moves
                if pos > -1:
                    if pos not in [ 0,1,2 ]:
                        (self.moves).append({ 'move':'UP','value':-3 })
                    if pos not in [ 6,7,8 ]:
                        (self.moves).append({ 'move':'DOWN','value':3 })
                    if pos not in [ 0,3,6 ]:
                        (self.moves).append({ 'move':'LEFT','value':-1 })
                    if pos not in [ 2,5,8 ]:
                        (self.moves).append({ 'move':'RIGHT','value':1 })


    def insertChildren(self,tree,pre,stack,fontier=None,action=None):

        self.cost = self.cost + 1

        for i in tree.moves:
            temp = swapped(tree.config,tree.config.index(0),tree.config.index(0) + i['value'])
            if ''.join(list(map(str,temp))) not in pre:
                pre.add(''.join(list(map(str,temp))))
                a = self.node(temp)
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

    def __init__(self,startNode,cost=0):
        self.root = self.node(startNode)
        self.maps = set()
        self.cost = cost
        self.depth = 0

    def dfs(self):
        self.maps.add(''.join(list(map(str,self.root.config))))
        stack = [self.root]
        while stack != []:
            a = stack.pop()
            if a != None:
                if a.config == list(range(0,9)):
                    ans = { }
                    cost = 0
                    path = []

                    while a != self.root:
                        cost = cost + 1
                        path.append(a.parentMove)
                        a = a.parent
                    ans['path_to_goal'] = list(reversed(path))
                    ans['nodes_expanded'] = self.cost
                    ans['cost_of_path'] = cost
                    ans['running_time'] = time.time() - start #running time ends
                    ans['max_search_depth'] = self.depth
                    return ans
            a.moves.reverse()
            self.insertChildren(a,self.maps,stack)



state = [1,2,3,4,5,0,6,7,8] #state of game
start = time.time() #running time starts
ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
game = boardMap(state)
ans = None
if(game.root.game == True):
    
    ans = game.astar()

    print(ans)


else:
    print('Game not initialised')
