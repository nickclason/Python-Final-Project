from pypaths import astar


def path_find():
    finder = astar.pathfinder()
    return finder((0, 5), (8, 2))
