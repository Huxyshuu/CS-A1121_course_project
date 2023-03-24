# Pipe flow

## Checkpoint 1 (21.3.2023)

Image of the current state of the program
![Image of the program](https://i.imgur.com/J1p30Bm.png)


### Existing features
- Adding pipes to the grid by clicking an empty square
- Deleting pipes by clicking them in the grid
- Switching between different placeable objects (4 pipes as of now)
- Clear grid button for clearing the entire grid of all present objects
- Two inputs for pressure at start and end points
- Start and end points are initialized at random positions marked in lightred
- Calculate button works, despite currently only adding the two given values together


### Planned features
- Feature to rotate or automatically have pipes rotate to form a proper pipeline
- Proper math calculation between two points
- Possibly more objects, such as a pump or a valve
- A pipe minigame
- Responsive layout or atleast window size


### Installation
Ideally the steps below would work:
1. Create a new folder for the project to be cloned into
2. Open a command terminal in that folder
3. Type:
```bash
git clone git@version.aalto.fi:tammh1/y2_2023_20296.git

or

git clone https://version.aalto.fi/gitlab/tammh1/y2_2023_20296.git
```
4. Make sure that you have a version of python 3.6.1 or above installed along with pip
5. Installing python is as simple as navigating to the download section on their official website: [Download Python](https://www.python.org/downloads/)

To install Pip:
1. Open cmd
2. Type the following in order:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
3. If the console recommends upgrading, type: 
```bash
pip install --upgrade pip
```

4. Open any preferred IDE (ex. PyCharm)
5. Open terminal and type: 
```bash
pip install PyQt6
```
6. Profit


### Usage
The program at its current state is not useful.


### Schedule
Estimated time spent on the project: ~20 hours
The initial planned schedule has not been followed, though progress seems to be ahead of the initial estimates.


### Other
The code behind adding objects to the grid has become very messy and hard to navigate. It's unclear what classes interact with eachother and how they are used.
