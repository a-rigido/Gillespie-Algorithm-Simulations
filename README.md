# Gillespie-Algorithm-Simulations

Python scripts utilizing the Gillespie algorithm to simulate the behaviour of stochastic models.

## Computational Background:

The focus of these scripts is the implementation of the Gillespie Algorithm, also know as the Stochastic Simulation Algorithm, created by Daniel Gillespie over 40 years ago. Gillespie reasoned that deterministic rate equations for biochemical reactions could not be accurate due to the sheer number of molecules at play and could be more accurately simulated using randomness coupled with the laws of probability. This method has been widely used in studying chemical reactions and systems since its introduction as the Gillespie Algorithm is considered physically accurate for a system in which the molecules are sufficiently dilute and well-mixed. The algorithm despite being quite powerful can be summarized easily by the following steps.

### Steps:

1.  Set up the parameters of the simulation (Rates, molecules, RNG, etc.)
2.  Stochastic Determination of the Reaction by Use of RNG and Reaction Probabiltiy.
3.  Update Parameters
4.  Take Exponential Time-Step Forward Based on All Rates
5.  Iterate from Step 2.

By doing this correctly, the Gillespie algorithms provides the user with a solution from the probability mass function that that solves the famous master equation, which is a set of differential equations that describe a system behaviour at a given time based on probability.

### Limitations:

Although the Gillespie algorithms is a simply, yet powerful tool to tackle complex systems, it must be noted that the algorithm is not without its flaws. Most notably, this algorithm needs a very good random number generator in order to be  reliable,band as previously noted, the Gillespie Algorithm is only considered physically accurate when molecules are sufficiently dilute and well-mixed. On top of that, as the systems being stimulated get larger and larger, the more taxing the simulations can be on a computer. It should also be noted that the algorithm can be used for non-reaction simulations, although it may not always be advantageous to use over a deterministic model as random events don’t necessarily govern those systems.

## Physical Background:

### Case 1: The Irreversible Enzymatic Reaction

It would be disadvantageous for any cell to allow chemical reactions to just follow suit towards equilibrium because it is far better to control the association/dissociation of chemical species by switching the reaction on and off as cell conditions require. This is why the body is full of enzymes, which are biological catalysts that lower the energy barrier require for a chemical reactionto take place without being consumed in the reaction itself. By doing this, reactions can occur much faster and on-command, which is of course advantageous for the cell and why evolution has implemented these catalysts  into  manyliving  systems.   A  proposed  model  for  the  enzymatic  reaction  is  given  by the following equation:

E + S ←→ ES → E + P,

where E is the amount of enzyme molecules, S is the amount of substrate molecules, ES is the amount of Enzyme-Substrate complex molecules, and P is the amount of product molecules. It should be noted that it has been assumed that the rate constants will remain constant despite changes in the cell, and the the reverse production formation rate is negligible as the product tends to be more thermodynamically stable than the substrate/intermediates. With all this in mind, the script shown will use a Gillespie algorithm to predict the behaviour of the irreversible enzymatic reaction shown below:


#### End Result from Script

![](https://github.com/a-rigido/Gillespie-Algorithm-Simulations/blob/master/irrEnzymaticReaction.png)

### Case 2: SIR Model

The SIR model is a model that simulates the spread of disease and recovery of a population after exposure to a pathogen. It is a simply model of infectious disease based on a differential equation model that can be summarised in the following equation:

S → I → R,

where S is for the susceptible population, I is for the Infected population, and R is for the recovered population. In this  particular simulation, there will also be a rate of birth to increase the S population, a death rate for the I population, and those that recover from the pathogen will remain immune to it for the rest of their lives. Of course this is one of the simple scenarios regarding this flavour of epidemiological model and can easily be made more complex, but the main reason for exploring this simulation again is to show how the Gillespie algorithm can be used to stochastically stimulated a non-chemical reaction scenario, showing the diversity of the method.

#### End Result from Script

![](https://github.com/a-rigido/Gillespie-Algorithm-Simulations/blob/master/SIRmodel.png)


<p align="center">
Copyright (c) 2019 Alex Rigido
</p> 
