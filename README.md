# dino_ai
A Reinforcement Learning Program outfitted with NeuroEvolution that can learn to play the Dino Game.
Update: Compatibility with Windows not tested.

## Requirements
- Python3.12 or higher (64-bit)
- Ability for GUI popups to appear
- Ability for creation of Python Virtual Environments (VENV's)
- Ability to run Bash files **(See WSL if on Windows)**

## Installation
Clone this repository either by CLI or Zip.
Due to its GUI usage, this program will not work in Github Codespaces.

1. Make sure executable permissions are enabled for the Bash Script:
```chmod +x /path/to/repo/dinogame.sh```
2. Run the bash file in the main folder named dinogame.sh like so:
```./path/to/repo/dinogame.sh```

## Usage
If it is your first running the script, it will ask you for the amount of cores to alocate the ML computations on. All runs after that will read your value from config.txt in the base folder.

Nothing else needs to be done for most use cases. The simple bash script will check for a venv and install the needed packages automatically. It will also check for any models or checkpoints from past runs and render the best-scoring generation whose weights were stored.

### Customization
The directory is split into three sections. Upon entering the DinoGame dir, there exists gym_best.py and gym_solver.py. The former reads any models being stored and renders the GUI on one induvidual of that population. The latter trains the Reinforcement Learning model on the game and stores the weights of the model after 50 generations. These values can be tweaked and fine-tuned. If you can ameliorate the model, please feel free to discuss your findings with me at jayakvv@gmail.com. 

The game environment is built in the game Python module within the DinoGame folder. There exists two classes: Dinosaur (within dinosaur.py), and DinosaurGame (within DinosaurGame.py). Dinosaur calculates the physics of the jump at each time interval and contains attributes of the Dinosaur. DanisaurGame contains all other game elements including drawing, colliding, score-keeping, and includes what the model is observing when playing the game.

## Future Improvements
1. Better Speed Function (how fast the dinosaur runs)
2. Better Variables (timesteps, generations, episodes, etc.)
3. Ducking Feature
4. Incorporation into Chrome Dino Game
