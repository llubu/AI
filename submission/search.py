# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
import sys # for MAXINT to be used in UCS

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  
  from game import Directions
  South = Directions.SOUTH
  West = Directions.WEST
  North = Directions.NORTH
  East = Directions.EAST
  
  state = util.Stack() # Keeps track of the state till now
  parent_rel = dict()  # Dict to keep track of parent of a given node 
  path = dict()        # To keep track of the direction of a node to reconstruct the path 
  out_path = list()    # To return the reconstruct path
  visited = set()      # To keep track of visited node
  
  init_place = (-1, -1) # To denote the initial state to make the path reconstruct loop terminate
  state.push(problem.getStartState()) #initial state of the problem
  parent_rel[problem.getStartState()] = init_place
  path[problem.getStartState()] = "NULL"
  visited.add(problem.getStartState())
  target = 0
  
  while not state.isEmpty():
      tmp_goal = state.pop()
      children = problem.getSuccessors(tmp_goal)
      #print type(children)
      #children.reverse()
      #print children
      for child in children:
          if child[0] not in visited:
              if (problem.isGoalState(child[0])):
                  target = child[0]
                  parent_rel[child[0]] = tmp_goal
                  path[child[0]] = child[1]
                  break
              else:
                  state.push(child[0])
                  visited.add(child[0])
                  parent_rel[child[0]] = tmp_goal
                  path[child[0]] = child[1]
              
  #Reconstructing Path from initial state to goal state
  print "Came out of first loop"
  print target, parent_rel[target], path[target]
  if target == 0:
      return []
  else:
      while (parent_rel[target] != init_place):
          out_path.append(path[target])
          target = parent_rel[target]
          
  out_path.reverse() # reversing since we are moving back from goal to initial state
  return out_path
  #util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  
  from game import Directions
  South = Directions.SOUTH
  West = Directions.WEST
  North = Directions.NORTH
  East = Directions.EAST
  
  state = util.Queue() # Keeps track of the state till now
  parent_rel = dict()  # Dict to keep track of parent of a given node 
  path = dict()        # To keep track of the direction of a node to reconstruct the path 
  out_path = list()    # To return the reconstruct path
  visited = set()      # To keep track of visited node
  
  init_place = (-1, -1)
  state.push(problem.getStartState()) #initial state of the problem
  parent_rel[problem.getStartState()] = init_place
  path[problem.getStartState()] = "NULL"
  visited.add(problem.getStartState())
  target = 0
  
  while not state.isEmpty():
      tmp_goal = state.pop()
      children = problem.getSuccessors(tmp_goal)
      #print type(children)
      #children.reverse()
      #print children
      for child in children:
          if child[0] not in visited:
              if (problem.isGoalState(child[0])):
                  target = child[0]
                  parent_rel[child[0]] = tmp_goal
                  path[child[0]] = child[1]
                  break
              else:
                  state.push(child[0])
                  visited.add(child[0])
                  parent_rel[child[0]] = tmp_goal
                  path[child[0]] = child[1]
              
  #Reconstructing Path from initial state to goal state
  print "Came out of first loop"
  #print target, parent_rel[target], path[target]
  if target == 0:
      return []
  else:
      while (parent_rel[target] != init_place):
          out_path.append(path[target])
          target = parent_rel[target]
          
  out_path.reverse() # reversing since we are moving back from goal to initial state
  return out_path

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  
  from game import Directions
  South = Directions.SOUTH
  West = Directions.WEST
  North = Directions.NORTH
  East = Directions.EAST
  
  state = util.PriorityQueue() # Keeps track of the state till now
  parent_rel = dict()  # Dict to keep track of parent of a given node 
  path = dict()        # To keep track of the direction of a node to reconstruct the path 
  out_path = list()    # To return the reconstruct path
  visited = set()      # To keep track of visited node
  cost = dict()        # Keeps tarck of the cost to reach to that node cost to rach parent + its cost to reach from parent
   
  init_place = (-1, -1)
  state.push(problem.getStartState(), 0) #initial state of the problem
  parent_rel[problem.getStartState()] = init_place
  path[problem.getStartState()] = "NULL"
  target = 0
  cost[problem.getStartState()] = 0     # cost to reach itself should be 0
  target_cost = float("inf")
  #print target_cost
    
  while not state.isEmpty():
      tmp_goal = state.pop()
      #print tmp_goal, cost[tmp_goal]
      #print tmp_goal
      
      if tmp_goal in visited:
          #print "YO YO"
          continue
          
      children = problem.getSuccessors(tmp_goal)
      visited.add(tmp_goal)
      #print type(children)
      #children.reverse()
      #print children
      if cost[tmp_goal] > target_cost:
          #print "NONO", cost[tmp_goal], tmp_goal, target_cost
          break
      for child in children:
          #print "CHILD LOOP", child
          if child[0] not in visited:
              #print "CHILD --1"
              if problem.isGoalState(child[0]):
                  if (cost[tmp_goal] +child[2] < target_cost):
                      target = child[0]
                      parent_rel[child[0]] = tmp_goal
                      path[child[0]] = child[1]
                      cost[child[0]] = cost[tmp_goal] + child[2] # cost to reach from tmp_goal to its child
                      target_cost = cost[tmp_goal] + child[2]
                   #   print "Target Cost", target_cost
                      break
              else:
                  #print "In else"
                  state.push(child[0], cost[tmp_goal] + child[2])
                  parent_rel[child[0]] = tmp_goal
                  path[child[0]] = child[1]
                  cost[child[0]] = cost[tmp_goal] + child[2] # cost to reach from tmp_goal to its child
                  #print child[2], cost[child[0]]
                             
  #Reconstructing Path from initial state to goal state
  #print "Came out of first loop"
  #print target 
  #parent_rel[target], path[target]
  if target == 0:
      return []
  else: # Traverse back till initial node is found
      while (parent_rel[target] != init_place):
          out_path.append(path[target])
          target = parent_rel[target]
          
  out_path.reverse() # reversing since we are moving back from goal to initial state
  return out_path
  

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  
  from game import Directions
  South = Directions.SOUTH
  West = Directions.WEST
  North = Directions.NORTH
  East = Directions.EAST
  
  state = util.PriorityQueue() # Keeps track of the state till now
  parent_rel = dict()  # Dict to keep track of parent of a given node 
  path = dict()        # To keep track of the direction of a node to reconstruct the path 
  out_path = list()    # To return the reconstruct path
  visited = set()      # To keep track of visited node
  cost = dict()        # Keeps tarck of the cost to reach to that node
   
  init_place = (-1, -1)
  state.push(problem.getStartState(), 0) #initial state of the problem
  parent_rel[problem.getStartState()] = init_place
  path[problem.getStartState()] = "NULL"
  #visited.add(problem.getStartState())
  target = 0
  cost[problem.getStartState()] = 0     # cost to reach itself should be 0
  target_cost = float("inf")
    
  while not state.isEmpty():
      tmp_goal = state.pop()
      #print tmp_goal
      
      if tmp_goal in visited:
          #print "YO YO"
          continue
          
      children = problem.getSuccessors(tmp_goal)
      visited.add(tmp_goal)
      #print type(children)
      #children.reverse()
      #print children
      if cost[tmp_goal] + heuristic(tmp_goal,problem) > target_cost:
          #print "NONO"
          break
      for child in children:
          #print "CHILD LOOP"
          if child[0] not in visited:
              if problem.isGoalState(child[0]):
                  if (cost[tmp_goal] + child[2] < target_cost):
                      target = child[0]
                      parent_rel[child[0]] = tmp_goal
                      path[child[0]] = child[1]
                      cost[child[0]] = cost[tmp_goal] + child[2] # cost to reach from tmp_goal to its child
                      target_cost = cost[tmp_goal] + child[2]
                      print "Target Cost", target_cost
                      break
              else:
                  state.push(child[0], heuristic(child[0],problem) + cost[tmp_goal] + child[2])
                  #visited.add(child[0])
                  parent_rel[child[0]] = tmp_goal
                  path[child[0]] = child[1]
                  cost[child[0]] = cost[tmp_goal] + child[2] # cost to reach from tmp_goal to its child
                             
  #Reconstructing Path from initial state to goal state
  print "Came out of first loop"
  print target 
  #parent_rel[target], path[target]
  if target == 0:
      return []
  else: # Traverse back till initial node is found
      while (parent_rel[target] != init_place):
          out_path.append(path[target])
          target = parent_rel[target]
          
  out_path.reverse() # reversing since we are moving back from goal to initial state
  return out_path
  
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch