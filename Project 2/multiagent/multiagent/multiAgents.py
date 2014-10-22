# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import sys, random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        #print legalMoves
        legalMoves.remove('Stop')

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        sucGameState = currentGameState.generatePacmanSuccessor(action)
        capsuleList =  sucGameState.getCapsules()
        #print action
        newPos = sucGameState.getPacmanPosition()
        #print newPos
        newFood = sucGameState.getFood()
        #print newFood
        #print ""
        #print len(newFood.asList())
        newGhostStates = sucGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #print newScaredTimes
        #print sucGameState.getScore()
            
        minScore = -sys.maxint -1
        
        if sucGameState.isWin():
            return sys.maxint
        if sucGameState.isLose():
            return minScore
            
        distFromGhost = sys.maxint
        ghostDistList = [] #Stores distance to each ghost 
        isActive = [] #Stores bool value : Whether ghost is active or not. Ghosts kill when active
        
        for ghost in newGhostStates:
            distFromGhost = manhattanDistance(newPos, ghost.getPosition())
            if (ghost.scaredTimer==0): #Ghost is currently active
                isActive.append(True)
                ghostDistList.append(distFromGhost) 
                if distFromGhost < 2: # Return min score if ghost is close : We want pacman to run from the ghost 
                    return minScore
            else:
                isActive.append(False)
                ghostDistList.append(-distFromGhost) #You may want to go closer to the ghost 
                   
           
        foodLeft = len(newFood.asList()) #You want less food left      
        distToFood = 0
        for food in newFood.asList():
            distToFood += manhattanDistance(newPos, food)
            
        for capsule in capsuleList:
            #print manhattanDistance(newPos, capsule)
            if manhattanDistance(newPos, capsule) < 1:
                #print "CLOSE"
                return sys.maxint
        
        "*** YOUR CODE HERE ***"
        return sucGameState.getScore() + (float(sum(ghostDistList))/distToFood)

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """
    
    # Max function of Min-Max algorithm
    def maxAgent(self, gameState, depth):
      
      # this function maximises the score of PacMan
      #By default the PacMan will stop
      action_to_be_performed = Directions.STOP
      #for Win/Lose state or zero depth we can return direction
      if  gameState.isWin() or gameState.isLose() or depth==0:
        return [self.evaluationFunction(gameState), action_to_be_performed]
      allowedMoves = gameState.getLegalActions(0)
      # get rid of "STOP" action from list of allowed moves
      actionList = [action for action in allowedMoves if action != 'Stop' ]
      maxVal = float("-inf")
      for action in actionList:
        # Now for all the actions in action list call minAgen with depth=depth-1
        returnedVal = self.minAgent(gameState.generateSuccessor(0,action), depth-1)
        if(returnedVal[0] > maxVal):
          maxVal = returnedVal[0]
          action_to_be_performed = action
      return [maxVal, action_to_be_performed]


    # Min function of Min-Max algorithm
    def minAgent(self, gameState, depth):
      
      action_to_be_performed = Directions.STOP
      if gameState.isWin() or gameState.isLose() or depth==0 :
        return [self.evaluationFunction(gameState), Directions.STOP]
      agentCount = gameState.getNumAgents()
      minVal = float("inf")
      #perform same action for all the ghost since for every ghost 
      for i in range(1,agentCount):
        allowedMoves = gameState.getLegalActions(i)
        # get rid of "STOP" action from list of allowed moves
        actionList = [action for action in allowedMoves if action != 'Stop' ]
        for action in actionList:
          # Now for all the actions in action list call maxAgent for all ghost with same depth to play their move
          returnedVal =  self.maxAgent(gameState.generateSuccessor(i,action), depth)
          if(returnedVal[0] < minVal):
            minVal = returnedVal[0]
            action_to_be_perfored = action
      return [minVal, action_to_be_performed]

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        return self.maxAgent(gameState, self.depth)[1]
        util.raiseNotDefined()
        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    # Max function of Min-Max algorithm
    def maxAgent(self, gameState, depth, a, b):
      
      # this function maximises the score of PacMan
      #By default the PacMan will stop
      action_to_be_performed = Directions.STOP
      #for Win/Lose state or zero depth we can return direction
      #print depth
      if  gameState.isWin() or gameState.isLose() or depth<=0:
        return [self.evaluationFunction(gameState), action_to_be_performed]
      allowedMoves = gameState.getLegalActions(0)
      # get rid of "STOP" action from list of allowed moves
      actionList = [action for action in allowedMoves if action != 'Stop' ]
      maxVal = float("-inf")
      for action in actionList:
        # Now for all the actions in action list call minAgen with depth=depth-1
        returnedVal = self.minAgent(gameState.generateSuccessor(0,action), depth-1, a, b)
        if(returnedVal[0] > maxVal):
          maxVal = returnedVal[0]
          action_to_be_performed = action
        if maxVal > b:
          return [maxVal, action_to_be_performed]
        a = max(a,maxVal)
      return [maxVal, action_to_be_performed]


    # Min function of Min-Max algorithm
    def minAgent(self, gameState, depth, a, b):
      
      action_to_be_performed = Directions.STOP
      #print depth
      if gameState.isWin() or gameState.isLose() or depth<=0 :
        return [self.evaluationFunction(gameState), Directions.STOP]
      agentCount = gameState.getNumAgents()
      minVal = float("inf")
      #perform same action for all the ghost since for every ghost 
      for i in range(1,agentCount):
        allowedMoves = gameState.getLegalActions(i)
        # get rid of "STOP" action from list of allowed moves
        actionList = [action for action in allowedMoves if action != 'Stop' ]
        for action in actionList:
          # Now for all the actions in action list call maxAgent for all ghost with same depth to play their move
          returnedVal =  self.maxAgent(gameState.generateSuccessor(i,action), depth, a, b)
          if(returnedVal[0] < minVal):
            minVal = returnedVal[0]
            action_to_be_perfored = action
          if minVal < a:
            return [minVal, action_to_be_performed]
          b = min(b, minVal)
      return [minVal, action_to_be_performed]

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        minVal = float("-inf")
        maxVal = float("inf")
        return self.maxAgent(gameState, self.depth, minVal, maxVal)[1]
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

