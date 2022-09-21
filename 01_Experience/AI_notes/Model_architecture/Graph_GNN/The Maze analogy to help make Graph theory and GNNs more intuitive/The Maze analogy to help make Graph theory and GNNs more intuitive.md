# 6 strategies for navigating a maze

- Top 6 strategies for navigating a maze:
	- Walking
	- Coloring the way
	- Squeezing through
	- Using a map
	- Destroying walls
	- Using wings.

# Walk and look around
- Walk and look around: simply walk randomly and look at the corners next to you (GCN, GAT), and the path in-between corners (MPNN).
- But different corners look the same (WL-test), it is easy to get lost (over-smoothing) and not reach its destination (over-squashing).

![[01_Experience/AI_notes/Model_architecture/Graph_GNN/The Maze analogy to help make Graph theory and GNNs more intuitive/Walk and look around.png]]


# Color your way
- Color your way: unique structures in the maze are colored differently (CW, subgraph ID, structural encoding). When walking, color-code your way to know where you passed (node coloring, non-overlapping MPNNs).
- But there are so many colors, it can be confusing!

![[01_Experience/AI_notes/Model_architecture/Graph_GNN/The Maze analogy to help make Graph theory and GNNs more intuitive/Color your way.png]]


# Squeeze through narrow paths
- Squeeze through narrow paths: 
	- Some paths connect different neighborhoods or communities in the graph/maze, but they are narrow
	- They are information bottlenecks and increase over-squashing
	- => Increase their hidden-dim or add parallel paths.
- But how to find these edges?

![[01_Experience/AI_notes/Model_architecture/Graph_GNN/The Maze analogy to help make Graph theory and GNNs more intuitive/Squeeze through narrow paths.png]]


# Use a map
- Use a map: 
	- Positional encoding such as Laplacian eigenvectors provide a map of the maze. 
	- Navigate using the main cardinal directions (DGN) your position (SAN, LSPE) and relative distances (Graphormer)
- But the map is bad:
	- Some parts are hard to read
	- Others are misleading

![[01_Experience/AI_notes/Model_architecture/Graph_GNN/The Maze analogy to help make Graph theory and GNNs more intuitive/Use a map.png]]



# Destroy walls
- Destroy walls: Rewiring a maze/graph by destroying walls/adding edges can help connect paths that should be close but are very far apart (GRAND and spectral modification).
- But destroy too many walls and your maze falls apart.

![[01_Experience/AI_notes/Model_architecture/Graph_GNN/The Maze analogy to help make Graph theory and GNNs more intuitive/Destroy walls.png]]


# Use wings
- Use wings: Simply move from one point to another point in the maze/graph using a fully-connected Transformer (SAN, Graphormer).
- But flying takes a lot of energy O(N^2), and without a good map and good coloring, you will get lost!
	- => Before flying, learn to read the map (SAN)!

![[01_Experience/AI_notes/Model_architecture/Graph_GNN/The Maze analogy to help make Graph theory and GNNs more intuitive/Use wings.png]]



# Listen to the echo with spectral methods
- Knock, yell, and listen to the echo with spectral methods! Look at the resonance of different sub-structures, or build spectral filters.
- But the relations are hard to understand: different structures can sound similar or vice-versa. Location becomes ambiguous.

![[01_Experience/AI_notes/Model_architecture/Graph_GNN/The Maze analogy to help make Graph theory and GNNs more intuitive/Listen to the echo with spectral methods.png]]


# 

---
- Status: #done 

- Tags: #GNN #graph

- References:
	- [Source](https://twitter.com/dom_beaini/status/1499019741234704385)

- Related:
	- 
