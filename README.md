# Towards Deception Detection in Multiplayer Dialogue Games using Trust-Based Argumentation  
Umeå University, 2023.

Joost Vossers <br>
Fanny Danelid <br>
Andreas Brännström <br>
Juan Carlos Nieves

This repository is a simplified implementation of the proposed deception detection framework presented in the paper.

The aim is to extend abstract argumentation frameworks to include trust values for each argument in order to determine the underlying level of deception.
This implementation has been developed in the context of the game of Werewolf, where players are supposed to hide information and act in a deceptive manner in order to win the game.
We create an observer agent with incomplete information that uses trust values to reason and make decisions about which agents are being deceptive.

The argument construction, reasoning, and decision making are all done in the `werewolf.py` file. Example input is present in `input/game.json` and `input/context.json`. The program first asks the user to submit an input file containing the arguments and attacks, and then for one containing rules for updating the trust values as well as observations about the game. Additional example input files are present as well.

The code is structured as follows:
* `Initialisation`: Here, the system asks for the names of the input files, which should be present in the `input` folder. Subsequently, the content of the files is read and saved, and some values are initialised as well.
* `Main Process`: The main loop of the game goes through each day of the input file. The arguments are extracted from the input and the trust values, attack levels, and deception levels are calculated.
* `Deception`: The deception levels are calculated by comparing the positions of the arguments in the ordered lists of trust values and attack levels.
* `Output`: The user is presented with the computed trust values and attack levels, as well as the argument deemed most deceptive.
* `Trust Updating`: The trust values are updated according to the provided inference rules, based on the available context information. The updates are printed as output to the user in order to make the system more transparent.
