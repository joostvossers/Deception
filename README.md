# Deception
Deception Detection in the Werewolf Game. Trends in Interactive Intelligent Environments (5DV210) at Umeå University, 2023.

Fanny Danelid, `fada0025` and Joost Vossers, `joge0053`

This repository is part of the project for the course Trends in Interactive Intelligent Environments (5DV210) at Umeå University.

The aim was to extend abstract argumentation frameworks to include trust values for each argument in order to determine the underlying level of deception.
This is all done in the context of the Werewolf game where players are supposed to hide information and act in a deceptive manner in order to win the game.
We create an observer with incomplete information that uses trust values to reason and make decisions about which players are being deceptive.

The argument construction, reasoning, and decision making are all done in the `werewolf.py` file. Example input is present in `input/game.json` and `input/context.json`. The first file should contain the arguments and attacks, while the second should contain rules for updating the trust values as well as observations about the game.

All input should be placed in the `input` folder.
