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
	



## Sprint 1 (OLD PROJECT)
## Contributions
- ** Sam **: "Created UI elements for goal tracking and push notification features"
	- `Jira Task: Design and implement a UI for users to configure their push notification preferences.`
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/mot/src/UI-for-push-notification-settings/
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/MOT-9
	- `Jira Task: Implement push notification functionality based on user preferences.`
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/src/push-notification-functionality/
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/MOT-10
	- `Jira Task: Design and implement a UI for users to set and manage their goals.`
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/src/UI-for-goals/
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/MOT-8
	- `Jira Task: Write unit tests to ensure that push notification and goal tracking functionality work as expected.`
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/src/unit-tests-for-push-notifications/
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/MOT-12
		
- ** Selah **: "Create UI elements for list of apps to block"
	- `Jira Task: Create a list that displays list of apps on users phone and allows them to select which apps they want to block`
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/mot/branch/feature/MOT-22
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/MOT-22?atlOrigin=eyJpIjoiZWZhNWQwZDdhYjAzNDY5ZWJmNDk0ZmQ1NjRmNWRkZWUiLCJwIjoiaiJ9
	- `Jira Task: Identify key features and functions to determine app layout`
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/commits/572dd501e333b36bc6ac538ce97682c3556961a7
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/MOT-23?atlOrigin=eyJpIjoiYjRhNmUxMmQwMTQ2NDVmYzhiMDZkYTA0YTcxMjljYmQiLCJwIjoiaiJ9
	- `Jira Task: Familiarize with Swift language and Xcode`
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/commits/572dd501e333b36bc6ac538ce97682c3556961a7
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/MOT-28?atlOrigin=eyJpIjoiYjQwMTlkYTU0MDFkNGY3MTkzODE3NGNmMjg3N2JmNjUiLCJwIjoiaiJ9
	- `Jira Task: allow user to input their list of apps`
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/branch/Selah-Boyle/contentviewswift-edited-online-with-bitb-1679262115450
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/MOT-29?atlOrigin=eyJpIjoiYzdjZWQzMzFkOTUzNDgyM2E5MjU5MWFiODE5ZjQ2ZGUiLCJwIjoiaiJ9
		
- ** Abigail Barrientos **: "Implemented timer UI"
	- `Jira Task: Display a ring around the timer`
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/mot/branch/feature/Timer_UI
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/MOT-24?atlOrigin=eyJpIjoiYzRjZWU5NzY2OGZkNDk5NzlkMWFiMzBlZTEyNDc1NzkiLCJwIjoiaiJ9
	- `Jira Task: Implement a start and stop blocking button`
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/branch/feature/Start_and_StopButton
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/MOT-18?atlOrigin=eyJpIjoiYjhjMDlhN2M2ZTJkNGM1NjkzNGNjZDdlN2YwYWRkYWQiLCJwIjoiaiJ9
	- `Jira Task: Allow user to edit timer`
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/branch/feature/Edit_Timer
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/MOT-19?atlOrigin=eyJpIjoiNWYyNGJmNjMwNmM4NGZkMWEwODQzYzliOTdjMThiYWMiLCJwIjoiaiJ9
		
- ** Ethan Wintill **: Implented screen time tracking UI
	- `Jira Task: Determine what data will be collected and stored
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/mot/commits/2c88fe14ceb96f91afdfdcc8c2c76e2c755017ea
		- jira reference: https://cs3398s23cardassians.atlassian.net/jira/software/projects/MOT/boards/3?assignee=63cf0915d73cd1e44e216d3c&selectedIssue=MOT-13
	- `Jira Task: Design the user interface for displaying screen time data
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/commits/82ea296641edd25e9f07a9271b23e0265e02172b
		- jira referece:  https://cs3398s23cardassians.atlassian.net/jira/software/projects/MOT/boards/3?assignee=63cf0915d73cd1e44e216d3c&selectedIssue=MOT-16
	- `Jira Task: Implement the user interface for displaying screen time data`
		- reference: https://bitbucket.org/cs3398s23cardassians/mot/src/UI-for-Screen-time-tracking/
		- jira reference: https://cs3398s23cardassians.atlassian.net/jira/software/projects/MOT/boards/3?assignee=63cf0915d73cd1e44e216d3c&selectedIssue=MOT-17
		
- ** Laiba **: "Created Social Features for the Feed "
	- `Jira Task: Implement Social Features for the feed`
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/mot/src/social-features/
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/MOT-31
	
## Next Steps For Sprint 2

- ** Sam **:
	- For the upcoming sprint I will focus on starting my tasks as soon as possible to ensure that I am not waiting till the last minute
	- Before we begin sprint 2, I want to discuss with my team members the possibility of switching to a different project because the learning curve for our current project turned out to be very ambitious
	- As an improvement to the team's overall productivity, I will organize more team meetings in the Alkek library to ensure everyone is on the same page and making contributions
	- As far as improvements to the codebase itself, if we decide to stay with the current project, I will work on making the UI more pretty and responsive as well as more engaging for users.
- ** Selah **:
	- I will think more about my tasks and limit the scope of each task to make it more achievable in each sprint.
	- As a team decide on a different project or minimizing the scope of our current project to make it achievable with the amount of time and team member knowledge and ability.
	- Allow more time for research and learning curve for any new languages or technologies we decide to use.
- ** Abigail Barrientos **:
	- Figure out what portion of the code keeps the timer running when stop button is pressed
	- Edit code so that the user can change the time intervals
	- Start reasearch on how to implement pop up in app.
- ** Ethan Wintill **:
	- Before any more code is done, I want to decide with my group whether we will be switching projects, or greatly simplifying the current one.
	- Add functionality to connect the goal UI to the progress UI, if we stay on the same project.
	- Write a flowchart with my group showing the screen transitions we want at the end of the spring, something like this: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F297237644134196394%2F&psig=AOvVaw0l69g3FynIHYA8_-h3mVK5&ust=1679435111013000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCJCi9L296_0CFQAAAAAdAAAAABAE
- ** Laiba **:
	- Starting Work way sooner and becoming more organized in handling my workload as I am dropping a class to decrease workload
	- Discuss Sam's idea of possibly changing project 
	- more organization and discussion including reasonable task devision to make sure we don't over estimate abilities to get tasks done as a team
	- for code starting sooner will allow me to lok more in detail in issues and find solutions and even come to teamamates sooner to help resolve and make progress 

___

## Sprint 2
## Contributions
- ** Sam **: "Created UI elements for goal tracking and push notification features"
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
		
- ** Selah **: "Create UI elements for list of apps to block"
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
		
- ** Abigail Barrientos **: "Implemented timer UI"
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 		
- ** Ethan Wintill **: Connected front and backends, implemented socketio architecture. 
	- `Jira Task: Get sockets working so that two clients can play each other
		- bitbucket reference:https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/1
		- jira reference: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/issues/BR-64
	- `Jira Task: Add functionality so that only first two to use game link are in the game
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/2
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/BR-65
	- `Jira Task: generalize the backend for multiple games concurrently
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/7
		- jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/issues/BR-67
	- `Jira Task: send data relevant to clients for each card played
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/4
		- jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/issues/BR-66
		
- ** Laiba **: "Created Social Features for the Feed "
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 
	- `Jira Task: 
		- bitbucket reference: 
		- jira referece: 

## Next Steps For Sprint 3

- ** Sam **:
	- For the upcoming sprint I will focus on starting my tasks as soon as possible to ensure that I am not waiting till the last minute
	- Before we begin sprint 2, I want to discuss with my team members the possibility of switching to a different project because the learning curve for our current project turned out to be very ambitious
	- As an improvement to the team's overall productivity, I will organize more team meetings in the Alkek library to ensure everyone is on the same page and making contributions
	- As far as improvements to the codebase itself, if we decide to stay with the current project, I will work on making the UI more pretty and responsive as well as more engaging for users.
- ** Selah **:
	- I will think more about my tasks and limit the scope of each task to make it more achievable in each sprint.
	- As a team decide on a different project or minimizing the scope of our current project to make it achievable with the amount of time and team member knowledge and ability.
	- Allow more time for research and learning curve for any new languages or technologies we decide to use.
- ** Abigail Barrientos **:
	- Figure out what portion of the code keeps the timer running when stop button is pressed
	- Edit code so that the user can change the time intervals
	- Start reasearch on how to implement pop up in app.
- ** Ethan Wintill **:
	- I want to make sure I am still on the same page as the rest of my team, because I have a schedule conflict with our normal meetings. I plan on taking asking in the groupme when everyone's free and announce when I'm working in bing so anyone on campus can swing by.
- ** Laiba **:
	- Starting Work way sooner and becoming more organized in handling my workload as I am dropping a class to decrease workload
	- Discuss Sam's idea of possibly changing project 
	- more organization and discussion including reasonable task devision to make sure we don't over estimate abilities to get tasks done as a team
	- for code starting sooner will allow me to lok more in detail in issues and find solutions and even come to teamamates sooner to help resolve and make progress 

___

## Acknowledgements
- This project is based on Brave Rats, by Seiji Kanai. [](https://blueorangegames.eu/en/games/braverats/)
- Brave Rats images and gameplay owned by respective copyright owners.
