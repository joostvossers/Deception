# Detecting Deception in the Werewolf Game using Trust-Based Argumentation Frameworks  
Trends in Interactive Intelligent Environments (5DV210) at Umeå University, 2023.

Fanny Danelid, `fada0025`  
Joost Vossers, `joge0053`

This repository is part of the project for the course Trends in Interactive Intelligent Environments (5DV210) at Umeå University.

The aim was to extend abstract argumentation frameworks to include trust values for each argument in order to determine the underlying level of deception.
This is all done in the context of the Werewolf game where players are supposed to hide information and act in a deceptive manner in order to win the game.
We create an observer with incomplete information that uses trust values to reason and make decisions about which players are being deceptive.

The argument construction, reasoning, and decision making are all done in the `werewolf.py` file. Example input is present in `input/game.json` and `input/context.json`. The first file should contain the arguments and attacks, while the second should contain rules for updating the trust values as well as observations about the game. Additional input files are present as well, containing input constructed from real transcripts of games of Werewolf.

The code is structured as follows:
* `Initialisation`: Here, the system asks for the names of the input files, which should be present in the `input` folder. Subsequently, the content of the files is read and saved, and some values are initialised as well.
* `Main Process`: The main loop of the game goes through each day of the input file. The arguments are extracted from the input and the trust values, attack levels, and deception levels are calculated.
* `Deception`: The deception levels are calculated by comparing the positions of the arguments in the ordered lists of trust values and attack levels.
* `Output`: The user is presented with the computes trust values and attack levels, as well as the argument deemed most deceptive.
* `Trust Updating`: The trust values are updated following the provided inference rules, based on the available context information. The updates are printed as output to the user in order to make the system more transparent.
