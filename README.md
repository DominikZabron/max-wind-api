# max-wind-api
Return the most windy places on Earth

## Installation

    $ pipenv install
    
## Configuration

To set number of locations returned by API to 10, edit settings.py file:

    QUERYSET_COUNT = 10
    
## Running

    $ pipenv run python api.py

## Example

    $ curl http://127.0.0.1:5000/NE
    ["Almeria", 15.4, "NE"], ["Ma-kung", 14.46, "NE"], ["Vicar", 14.4, "NE"]]