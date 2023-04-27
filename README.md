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
- ** Sam **: "Designed and implemented backend architecture for seamless multiplayer gameplay"
	- `Jira Task: Add functionality to create a new game on server 
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/pull-requests/3
		- jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/boards/3/backlog?issueParent=10049&selectedIssue=BR-49
	- `Jira Task: Handle routes for home page and play page, with respective post requests aswell
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/pull-requests/5
		- jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/boards/3/backlog?issueParent=10049&selectedIssue=BR-53
	- `Jira Task: Create socket architecture to recieve input and send output to client
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/pull-requests/10
		- jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/boards/3/backlog?issueParent=10049&selectedIssue=BR-50
	- `Jira Task: Implement functionality to use client input in game logic
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/pull-requests/8
		- jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/boards/3/backlog?issueParent=10049&selectedIssue=BR-52
	- `Jira Task: Write unit tests to ensure server architecture works as intended
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/pull-requests/23
		- jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/boards/3/backlog?issueParent=10049&selectedIssue=BR-54
		
Selah : "Create Home Page"
`Jira Task: Create Rules page from button on home page
bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/commits/fccc6f641104f96e43c69ca6e8f772668b12dd3b
jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/boards/3/backlog?issueParent=10073%2C10043%2C10051&selectedIssue=BR-43
`Jira Task: Create page layout using html
bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/commits/b21f3a54a35da638abf3fa5b33968fe640ecf6cd
jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/boards/3/backlog?issueParent=10073%2C10043%2C10051&selectedIssue=BR-40
`Jira Task: Play with friend button creating shareable url
bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/commits/d122d1c9c65a3608489afbf468c0528cd887b5af
jira referece: https://cs3398s23cardassians.atlassian.net/jira/software/projects/BR/boards/3/backlog?issueParent=10073%2C10043%2C10051&selectedIssue=BR-42
		
- ** Abigail Barrientos **: "Created the main play board where the users can play their cards"
	- `Jira Task: Display user and bot cards
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/13
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/BR-46?atlOrigin=eyJpIjoiODZkODhkYzAyMjg3NDQzNjhiYjdhODZiYTQ1MGQ3ZTciLCJwIjoiaiJ9
	- `Jira Task: Create new playing cards
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/9
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/BR-68?atlOrigin=eyJpIjoiN2VjNDdlMGEyMDI5NDk1NTliOWMzOTc5YTc2MmE2ZDEiLCJwIjoiaiJ9
	- `Jira Task: User Profile
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/22
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/BR-51?atlOrigin=eyJpIjoiZDM0OGUyNDY3MDM1NDMxODkzYTZjOGM1YzNhMTBlZDUiLCJwIjoiaiJ9
	- `Jira Task: User Settings
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/19
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/BR-55?atlOrigin=eyJpIjoiZTY0ZDhkOGUxODg2NDJhNDg0YzFlZDI0NmY2ODEyNDAiLCJwIjoiaiJ9
	- `Jira Task: Game Audio
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/14
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/BR-56?atlOrigin=eyJpIjoiMTc2MmNkMTAyYzYzNDU4NTk3Y2QzZDJmMjNjMWQ2YzMiLCJwIjoiaiJ9
	- `Jira Task: Display cards that the users have played
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/24
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/BR-48?atlOrigin=eyJpIjoiYzA5ZTNiMWM5ODY2NDliYjk1MmY4NmE5Mzc3ZDBiZjgiLCJwIjoiaiJ9
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
		
- ** Laiba **: "Created GameOver Page"
	- `Jira Task: Build Game Over POP-UP `
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/commits/eefff08659e7c8902f1b0ac97f044258d617930b 
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/BR-58?atlOrigin=eyJpIjoiOGUzN2Y5ZTdmOTQ3NDcxMDk4MDFhMmY1MzQwMjkzMGQiLCJwIjoiaiJ9
	- `Jira Task: Format Window Size `
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/commits/7642ee151f6d5985370a3d00f92ffab9a9d5b19f
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/BR-60?atlOrigin=eyJpIjoiZDYwYTRhNDg1ZTIwNGRkNzhlZDJhZDc5N2Y5MzY1OGUiLCJwIjoiaiJ9
	- `Jira Task: CSS TouchUP `
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/commits/a7cde8d5d5f98801e3f488acae949d0ebfc98c1a
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/BR-63?atlOrigin=eyJpIjoiYmVjZjZiMGU0YzJhNDhmMTljMmE4MGI2MjUzODRhYTYiLCJwIjoiaiJ9
	- `Jira Task: Connect POP-UP to gamescreen `
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/brave_rats/commits/ed047d48c5c795fdca53b8476a8f359ac331082f
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/BR-59?atlOrigin=eyJpIjoiMWZjOGQ0NGM4NGM4NDVkNGFjYmQwMzlmOWI4ZTgxZmUiLCJwIjoiaiJ9
	

## Next Steps For Sprint 3

- ** Sam **:
	- For this next sprint I will add more features such as user logins and database functionality
	- I will work quickly to ensure that our goals are reached by the end of the sprint
Selah :
I will start and finish my tasks very early in the sprint.
Communicate with team members on what I'm currently doing.
Allow more time for merging and implementing team members code to work in sync with mine.
- ** Abigail Barrientos **:
	- For this sprint my task is to create a button in the main screen that allows the user to play with a bot. I will also be incharge of making the code for that bot.
	- Another task that I need to work on is giving the user the option to play with anyone who is currently searching for another player.
	-  The last thing I will need to work on for this sprint is allowing the user to select a profile picture in their account page.
- ** Ethan Wintill **:
	- I want to make sure I am still on the same page as the rest of my team, because I have a schedule conflict with our normal meetings. I plan on taking asking in the groupme when everyone's free and announce when I'm working in bing so anyone on campus can swing by.
- ** Laiba **:
	- Assigned 3 front end tasks 
	- do a multiple commits a day and 1 push atleast no matter how small the change 
	- more open communication about workload help if needed 
___

## Sprint 3 
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
		
- ** Selah **:
	- `Jira Task: Make a simpler sharing link`
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/commits/a113d9a3eff028195664a4804731e122d0eaa8a0
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/BR-78?atlOrigin=eyJpIjoiM2QwYjg3ZDE2YzAxNDQxZWEwZWMxZTc1NDYxZjY0MmEiLCJwIjoiaiJ9
	- `Jira Task: Display points for user and opponent`
		- reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/30
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/BR-74?atlOrigin=eyJpIjoiZGFlZGY0YWY2NjcwNDgyYWJmZGFkMTdlZTdkNzFlNjYiLCJwIjoiaiJ9
	- `Jira Task: First player mode main screen`
		- reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/37
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/BR-81?atlOrigin=eyJpIjoiNmY1ZDE3ZmMzZGU0NGE5MDk0OTMxYjY0YTllNmEzOWMiLCJwIjoiaiJ9
- ** Abigail Barrientos **: 
	- `Jira Task: First Player Mode Bot`
		- bitbucket reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/31
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/BR-82?atlOrigin=eyJpIjoiYmY1Y2YwY2E4NTg0NDI4OWE3OWMzOTZkMDQ3MTA1MzYiLCJwIjoiaiJ9
	- `Jira Task: Account Page to Database`
		- reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/36
		- jira referece: https://cs3398s23cardassians.atlassian.net/browse/BR-83?atlOrigin=eyJpIjoiNmEzNDQ3ZmNlY2I2NDFhNzg5N2JjNzJmMDM0OTU3MDEiLCJwIjoiaiJ9
	- `Jira Task: Select User profile picture`
		- reference: https://bitbucket.org/cs3398s23cardassians/%7B74c95d59-a787-4de7-ad93-16c74b62959a%7D/pull-requests/29
		- jira reference: https://cs3398s23cardassians.atlassian.net/browse/BR-92?atlOrigin=eyJpIjoiNzgxMTA5OTAwNzg1NGRhNmI4NzY5OTgyNjQyYWUwNTIiLCJwIjoiaiJ9
		
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



## Next Steps For Sprint 4

- ** Sam **:
	- For this next sprint I will add more features such as user logins and database functionality
	- I will work quickly to ensure that our goals are reached by the end of the sprint
- ** Selah ** :
	- Make the the rules page and flow of the game more aesthetically pleasing.
	- Alow more time for research.
	- Allow more time for merging and implementing team members code to work in sync with mine.
- ** Abigail Barrientos **:
	- For the next version I would have liked to have include social cues for the player to click the cards. Currently the user recives no prompt to click on the cards. It would be helpful to have a notification that tells them to click a card.
	- Another thing to add would be sound effects for clicking the cards and when the user wins or loses. 
	-  The last thing I will need to work on for this sprint is allowing the user to select a difficulty for the first player bot. 
- ** Ethan Wintill **:
	- I want to make sure I am still on the same page as the rest of my team, because I have a schedule conflict with our normal meetings. I plan on taking asking in the groupme when everyone's free and announce when I'm working in bing so anyone on campus can swing by.
- ** Laiba **:
	- Assigned 3 front end tasks 
	- do a multiple commits a day and 1 push atleast no matter how small the change 
	- more open communication about workload help if needed 
___

## Acknowledgements
- This project is based on Brave Rats, by Seiji Kanai. [](https://blueorangegames.eu/en/games/braverats/)
- Brave Rats images and gameplay owned by respective copyright owners.
