# Virus Simulation (An Agent-Based Modeling Approach)

## Getting Started
1. Install python 3.7 or above using either miniconda (https://docs.conda.io/en/latest/miniconda.html) or the standard python package (https://www.python.org/downloads/)
2. Once python is installed, in a shell window, navigate to the root dir of this repo and run:
    ```bash
    pip install -r requirements.txt
    ```
3. Once the requirements are installed, run the script using:
    ```bash
    python app/simulation.py
    ```

## Simulation Parameters
The simulation is broken into the environment (`simulation.py`) and the agents (`agents.py`). The environment populates the environment with the agents and at each iteration, the agents make a decision as to where they will travel in the space. Each agent in the environment has two 'modes' for operating: (1) random step or (2) avoidance step. In (1), the agent will execute a sort of random work (e.g. Brownian motion) and take a step size determined by the parameter `step`. In avoidance step mode, the agents are aware of each other and will take a step in the direction that maximizes the distance between themselves and a 20 unit radius or a random step if there are no immediate indivuals nearby. At the beginning of the simulation, one of the agents is randomly selected as the infected agent. If the infected agent is within the `socdistance` of any other agents, then the uninfected agents become infected. 


## Disclaimer
This is demonstrated as a showcase of developing agent-based models in Python, where large-scale behavior can be **QUALITATIVELY** observed. No expertise in the field of  infectious disease epidemiology is assumed here. 


## Additional Information
For more on agent-based modeling, please visit the following links:
- https://www.pnas.org/content/99/suppl_3/7280
- https://www.frontiersin.org/articles/10.3389/fevo.2018.00237/full