# Problem 4.7 - Build Order

# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). 
# All of a project's dependencies must be built before the project is. 
# Find a build order thar will allow the projects to be built. 
# If there is no valid build order, return an error.

# Example:

# Inputs:
#   projects: a, b, c, d, e, f
#   dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

# Output: f, e, a, b, d, c

# ---------------------------------

# The pairs look similar to a directed graph
# There has to be a way to visit all points on the graph starting at one point.
# An invalid list of projects would be a graph that could not visit a point

