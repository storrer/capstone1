# Star Charts Website – Project Proposal
## Goal
I propose to create a Flask web application and website where users can obtain a star chart of the night sky. From any one location on Earth the stars and constellations visible in the night sky change over time. This change is due to the rotation of the Earth on its axis and its orbit around the Sun. Therefore, the creation of an accurate and undistorted star chart requires the location of the observer and the date and time of the observations. My application will generate star charts for users that accurately depict and label prominent astronomical objects and constellations visible from the user’s location.

## Users and Data
Everyone on Earth is a potential user of this site.
The application will use astronomical data that includes the position of the stars and planets in the night sky, and the names of astronomical objects such as stars and constellations.
I would like the website to appeal to all users, but there is an historical bias in the naming of constellations and stars by astronomers. The names given to astronomical objects by cultures outside of the European and Arabic star/constellation naming system are not usually presented with star charts. If the data is available, I would like to add these "alternative" star and constellation names to the star charts that my application generates.

## Development 
I intend to use GitHub's automated Kanban board to manage work on this project. That means I will write issues and link them to pull requests and they will close automatically when the pull request is merged into my main branch.

I also intend to use daily stand-ups to plan my work on a day-to-day basis. The method I use for stand ups is to identify three things:
1. What I have done since the last stand up.
2. Would I intend to do between now and the next stand up.
3. What is blocking me from completing the work I plan to do.

## Database and Security 
The database for the website will primarily store a user profile model  contains standard login credential fields as well as application specific fields such as user's location, preferences, and saved or "favorited" star charts.

Sensitive information stored in the database, such as user credentials and their preferred observation locations, will be encrypted.

## User Flow
When the user visits the site they will find a simple homepage with a navigation bar and a form. From the homepage users can submit the form and they will get a star chart for the location they submitted in the form. Users can use links on the nav bar to go to there profile page, log in, or register for an account.
Once a star chart is generated for the user a message will ask the user if they want to save the image to their profile. If the user is logged in this will allow them to save the star chart to a favorites list. If the user is not logged in they will be redirected to a login page. At the login page they will be able to enter their credentials. New users will find links for signing up on all relevant pages.
A user may visit their profile page via a link in the nav bar. Their user profile will contain a list of their saved star charts. This list can be edited by the user. Individual star charts can be deleted or given custom names by the user.

>Created by Chris Storrer