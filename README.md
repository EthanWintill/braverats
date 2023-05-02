# Brave Rats #
Authors: Abigail Barrientos, Sam Bryant, Ethan Wintill, Laiba Janat, Selah Boyle

## Overview
Brave Rats is a quick, 2 player card game similar to war that is all about reading your opponent. Each player starts with 8 cards and puts one of them down to face the opponent. The card with the highest power usually wins, however each card has a special ability that greatly affects the outcome of the game. The first player to reach 4 victories wins the game.
We have implemented this game in to an online browser card game. Users can play private matches with their friends, or play against a bot to hone their skills.

The current version of the game is hosted at <a href="https://braverats.herokuapp.com/">braverats.herokuapp.com</a>

## Technologies used
- ** Flask **
- ** SocketIO **
- ** Gunicorn **
- ** JQuery **
- ** Bootstrap **

## Setup
- ** Install Dependencies **:
	- `Python`
		- Go to python.org
		- Choose the download for your hardware
		- Ensure download is complete by running "python --version" in your terminal
	- `Clone Project`
		- Create a new directory to install the project
		- Run "git clone https://bitbucket.org/cs3398s23cardassians/brave_rats/src/main/"
		- Ensure all files are cloned on your system
	- `Set Up Environment (optional)`
		- Run "pip install virtualenv"
		- Run "virtualenv venv" to create a new environment in your directory
		- Run "source venv/bin/activate" to enter your virtual environment
	- `Install Project Dependencies`
		- Run "pip install -r requirements.txt" in the root folder of the cloned project
		- After this is complete, you are ready to host a local server
- ** Run Server **:
	- `Using Gunicorn`
		- In your terminal, run the following command to start the server:
		- "gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:app"
		- You should see in the console that the server is running with a url (usually localhost) to visit the site
	- ## Done! You are ready to play on you local machine!
	


## Acknowledgements
- This project is based on Brave Rats, by Seiji Kanai. [](https://blueorangegames.eu/en/games/braverats/)
- Brave Rats images and gameplay owned by respective copyright owners.
