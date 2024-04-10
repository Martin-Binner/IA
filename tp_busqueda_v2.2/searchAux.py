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

class SearchProblem:
    """
    This class outlines the nodes of a search problem, but doesn't implement
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

def search(problem, fringe):
    initial_state = problem.getStartState()
    initial_actions = []
    initial_candidate = (initial_state, initial_actions)
    fringe.push(initial_candidate)
    closed_set = set()
    while not fringe.isEmpty():
        candidate = fringe.pop()
        state, actions = candidate
        if problem.isGoalState(state):
            return actions
        if state not in closed_set:
            closed_set.add(state)
            candidate_successors = problem.getSuccessors(state)
            candidate_successors = filter(lambda x: x[0] not in closed_set, candidate_successors)
            candidate_successors = map(lambda x: (x[0], actions + [x[1]]), candidate_successors)
            for candidate in candidate_successors:
                fringe.push(candidate)

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    nodes = util.Stack()
    exploreds = []
    
    start = problem.getStartState()

    nodes.push((start, []))

    while not nodes.isEmpty():
        node, actions = nodes.pop()

        if node not in exploreds:
            exploreds.append(node)

        if problem.isGoalState(node):
            return actions
        else:

            for successor, succAct, succCost in problem.getSuccessors(node):
                newActions = actions + [succAct]
                newNode = (successor, newActions)
                nodes.push(newNode)
    return actions

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    nodes = util.Queue()
    exploreds = set()
    actions = []
    initCost = 0

    start = problem.getStartState()

    nodes.push((start, actions, initCost))

    while not nodes.isEmpty():
        node, actions, cost = nodes.pop()

        if node not in exploreds:
            exploreds.add(node)

        if problem.isGoalState(node):
            return actions
        
        for successor, succAct, succCost in problem.getSuccessors(node):
            newActions = actions + [succAct]
            newCost = cost + succCost
            newNode = (successor, newActions, newCost)
            nodes.push(newNode)

def uniformCostSearch(problem):
    "Search the node of least total cost first."
    nodes = util.PriorityQueue()
    exploreds = dict()
    actions = []
    initCost = 0

    start = problem.getStartState()

    nodes.push((start, actions, initCost))

    while not nodes.isEmpty():
        node, actions, cost = nodes.pop()

        if node in exploreds.keys or cost < exploreds[node]:
            exploreds[node] = cost

        if problem.isGoalState(node):
            return actions
        
        
        for successor, succAct, succCost in problem.getSuccessors(node):
            newActions = actions + [succAct]
            newCost = cost + succCost
            newNode = (successor, newActions, newCost)
            nodes.push(newNode)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    nodes = util.PriorityQueue()
    exploreds = []
    actions = []
    initCost = 0

    start = problem.getStartState()

    nodes.push((start, actions, initCost))

    while not nodes.isEmpty():
        node, actions, cost = nodes.pop()

        exploreds[node] = cost

        if problem.isGoalState(node):
            return actions
        
        
        exploreFlag = 0
        for successor, succAct, succCost in problem.getSuccessors(node):
            newActions = actions + [succAct]
            newCost = problem.getCostOfActions(newActions)
            newNode = (successor, newActions, newCost)
            nodes.push(newNode)

            for explored, exploredCost in exploreds:
                if node == explored and newCost >= exploredCost:
                    exploreFlag = 1
            if not exploreFlag:
                nodes.push(newNode, newCost + heuristic(node, problem))
                exploreds.append((node, newCost))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
