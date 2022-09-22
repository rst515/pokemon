# Pokémon Crawler

This app has been created for the CybSafe Django Challenge

**Application Requirements:**

1. Build an application that can discover all the Pokémon from the PokeAPI
2. Store Pokémon (design your own schema) and some attributes:
    - a. Pokémon name
    - b. Description
    - c. Choose some of it's characteristics like: Stats, Abilities, Movements etc ... maximum 5
3. Demonstrate or consider your approach to testing / TDD.

The code can be sent as a public or private git repo.
Spend no more than 2 hours on this, we might like Pokémon but we appreciate you have other things to do, so leave plenty for us to talk about face to face.

**How the criteria has been met**

1. A script ```refresh.py``` uses the ```pokebase``` wrapper library to access the Pokemon API. It finds how many entries there are and iterates over them, saving each to the Pokemon database model (since the task was intended to take a few hours the number has been limited to the first 100).
2. A Django project has been created from the Boilerplate provided, it has a Pokemon model and schema for storing the data.  Image, name, height, abilities and number of moves are stored.  Class-based views were implemented using basic html templates: a paginated ListView for all entries and a DetailView for individual entries (access via /pokemon_id primary key in url). The DetailView shows the full abilities list.
3. A test-driven approach to development was taken.  Tests are in ```tests.py```, they  check connection to the API and simulate saving entries to the database. If this project were further developed and had its own API endpoints for CRUD, tests for these could be added.

## Design notes
Used the Boilerplate provided and built the Docker image.
Added 'crawler' app to the Django project.
Considered using the raw API but then also evaluated the Python [wrapper libraries](https://pokeapi.co/docs/v2#wrap).
[PokeBase](https://github.com/PokeAPI/pokebase) seemed the simplest to use - added to requirements.txt.
Created a basic web page to show the results, so that the sprite could be rendered (could not find a way to do this in Admin view).
Enable Django Admin so the database can be managed that way too.
After experimenting with a function-based view to consume the API and finding it timed out due to the number of items, a script was created to get the API data and save it in the database. This script can run in the background and wile the app is being used.  Runscript is a one of the django-extensions and has been added to requirements.txt.
This can be run using the command

```docker-compose run --rm web sh -c "python manage.py runscript refresh"```

## Implementation
- Built Docker Boilerplate image
- Tests created and ran
- Model created
- Tests ran again
- API data collected
- Registered model in Admin
- Templates created

## Scaling
The following considerations have been given to performance at scale, to ensure good performance for the user of this service and users of the API
- pagination of results from the database
- it would perhaps be preferable to check for new pokemon and only add new ones to the database (not implemented but could be added)
- an option to refresh the whole database is possible with the ```refresh.py``` script (editing required, see comments in that file)
In practice, it may be preferable to consume the API from the source, or saving selected information, rather than saving a copy of everything.

## Testing
Took a test-driven approach to implementation, with unit tests to check the API works and test saving to the database.
Tests are in the tests.py file.  All tests passed.

## Further developments
Conscious that this challenge was to take a few hours I am noting other things that could be implemented to improve the project:
- Trigger update of the database to add new items from a button in the ListView template.
- Trigger refresh of whole database from a button in the ListView template.
- Review choice of data collected - there may be more useful or interesting information that users might want to have in the database.

## To use
1. Clone the repo.
2. Build the Docker container with ```docker build .``` inside the project directory.
3. Run the Django migrate function with ```docker-compose run --rm web sh -c "python manage.py migrate"```
4. Populate the database with ```docker-compose run --rm web sh -c "python manage.py runscript refresh"``` (will return first 100, see comments in ```refresh.py``` to change).
5. Run the Django server with ```docker-compose up -d``` (runs in detatched background mode).
6. Navigate to http://127.0.0.1:8000/ or http://127.0.0.1:8000/admin in the web browser to see the Pokemon.
7. Run ```docker-compose down``` to stop the server.