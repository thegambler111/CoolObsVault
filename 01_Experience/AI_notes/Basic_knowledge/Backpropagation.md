# Backpropagation
- [Source](https://twitter.com/karpathy/status/1559672719414681601)
- [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0)






# Backpropagation problems
## Leaky abstraction
>**The problem with Backpropagation is that it is a** [**leaky abstraction**](https://en.wikipedia.org/wiki/Leaky_abstraction)**.**

In other words, it is easy to fall into the trap of abstracting away the learning process — believing that you can simply stack arbitrary layers together and backprop will "magically make them work" on your data. So lets look at a few explicit examples where this is not the case in quite unintuitive ways.


## Vanishing gradients on sigmoids

## Dying ReLUs

## Exploding gradients in RNNs

## Spotted in the Wild: DQN Clipping




















# 

---
Status: #writing

Tags: #machine_learning #basic_ai_knowledge #backpropagation

References:
- [# Yes you should understand backprop](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b)
- [CS231n lecture on backprop](https://www.youtube.com/watch?v=i94OvYb6noo); [Full course](http://cs231n.stanford.edu/)
- [# PyTorch Autograd Explained - In-depth Tutorial](https://www.youtube.com/watch?v=MswxJw-8PvE)
- [# Looking Inside The Blackbox — How To Trick A Neural Network](https://towardsdatascience.com/peering-inside-the-blackbox-how-to-trick-a-neural-network-757c90a88a73)


Related: [[01_Experience/AI_notes/Pytorch/Backpropagation in Pytorch]]
