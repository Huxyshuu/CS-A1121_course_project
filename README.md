# Pipe flow - Hugo Tamm

## Introduction
### Final project (12.05.2023)
Pictures of the project

![Picture of the program](https://i.imgur.com/wMXlqTV.png)

![Picture of the unit-testing](https://i.imgur.com/KC58IRA.png)
![Picture of the UML diagram](https://i.imgur.com/T2PbnL8.png)
The pipe flow program is a simulation created for the calculations of flow speed through a pipe system. Given the starting and ending points, their heights and pressure, we can calculate the flow speed using extended Bernoulli's equation.

## File and folder structure
- There are three folders in the repository,
    - Code, which contains all of the source code for the program as well as unit-testing in the file named projectTest.py
    - Documents, which contain both the initial program plan and the final documentation of the entire project
    - Images, which contain necessary image files for the program to work, such as the icons for pipes

## Installation
Ideally the steps below would work for the installation:
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
6. The program should now open up when the main.py file is  booted through an IDE or any console

## Usage
The program can be used in 3 simple steps:
1. Choose the heights for both the starting and ending points (A and B)
2. Build a pipesystem to connect these points
3. Enter desired pressure values in kPa units and click "Calculate Flow!"-button
4. For further use, the grid can be cleared to build a new pipesystem, though currently it doesn't impact the calculation results at all :(

## Existing features
- Adding pipes to the grid by clicking an empty square
- Deleting pipes by clicking them in the grid
- Switching between different placeable objects (4 pipes)
- Clear grid button for clearing the entire grid of all present objects
- Rotate button for rotating the pipes
- Two inputs for pressure at start and end points
- Start and end points are initialized at random positions and can be moved by clicking on the colored area of the grid
- Calculate button works, despite the calculations most likely being inaccurate

## Checkpoints have been moved
Checkpoints have been moved to another README file called 'README_OLD', allowing for this to be the main README containing all the information of the current and the final state of the project.
