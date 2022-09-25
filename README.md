# Pokémon Crawler v2

This app has been created for the CybSafe Django Challenge

## Updates in version 2
This version uses the base API rather than a wrapper and processes all API data not just a sample.
A model method has been added to handle adding API data to the database and this is callable from the listview template.
The tests have been updated.

*models.py, urls.py & views.py*
1. function for updating database from API added to model and view added to handle it.

*tests.py & refresh.py*
1. ```requests``` imported and used to test connection to the API with status code 200.
2. ```pokebase``` removed in favour of requests-based approach to consuming the API.
*pokemon_list.html*
1. template updated to add button for refreshing list from API.


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

1. A model method compares the number of items in the database to the API and saves the new entries to the database. This is callable from the template view.
2. A Django project has been created from the Boilerplate provided, it has a Pokemon model and schema for storing the data.  Image, name, height, abilities and number of moves are stored.  Class-based views were implemented using basic html templates: a paginated ListView for all entries and a DetailView for individual entries (access via /pokemon_id primary key in url). The DetailView shows the full abilities list.
3. A test-driven approach to development was taken.  Tests are in ```tests.py```, they  check connection to the API and simulate saving entries to the database. If this project were further developed and had its own API endpoints for CRUD, tests for these could be added.

## Design notes
Used the Boilerplate provided and built the Docker image.
Added 'crawler' app to the Django project.
Created a basic web page to show the results, so that the sprite could be rendered.
Enable Django Admin so the database can be managed that way too.

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
- it is perhaps be preferable to check for new pokemon and only add new ones to the database - implemented
In practice, it may be preferable to consume the API from the source, or saving selected information, rather than saving a copy of everything.

## Testing
Took a test-driven approach to implementation, with unit tests to check the API works and test saving to the database.
Tests are in the tests.py file.  All tests passed.

## Further developments
- Review choice of data collected - there may be more useful or interesting information that users might want to have in the database.

## To use
1. Clone the repo.
2. Build the Docker container with ```docker build .``` inside the project directory.
3. Run the Django migrate function with ```docker-compose run --rm web sh -c "python manage.py migrate"```
4. Run the Django server with ```docker-compose up -d``` (runs in detached background mode).
5. Navigate to http://127.0.0.1:8000/ or http://127.0.0.1:8000/admin in the web browser to see the Pokemon. Click a name to see the detailview.
6. Populate the database by clicking the Update Database button on the page.
7. Run ```docker-compose down``` to stop the server.