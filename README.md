# CurrencyConverter

CurrencyConverter will be a web platform that allows users to calculate currency
exchange rates.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Clone repository

```
git clone https://github.com/amolinaalvarez/currency-converter.git
```

### Environment

This project uses Pipenv to manage virtual environments and dependencies.

```
sudo apt install pipenv
```

Rename ```.env.dist``` file to ```.env``` with your local vars.


### Pipenv

Activate environment and install libraries:

```
pipenv shell
```

```
pipenv install
```

In your local machine:

```
pipenv install --dev
```

Please, try to keep updates dependencies, not changing * from Pipfile.

### Configuration

Create models and relationships implied by your models into your database (with pipenv activated):

```
python manage.py migrate
```

Initial data for populating the database:

```
python manage.py loaddata currencies.json
python manage.py loaddata providers.json
```

Django runserver:

```
python manage.py runserver
```

## Running the tests

Django comes with a test suite of its own, in the tests directory of the code base.

```
python manage.py test
```

## Endpoints

The platform exposes the following API endpoints:

- List of currency rates for a specific time period

    ```
    /api/currency-exchanges/list
    ```

    - Parameters:
        - source_currency
        - date_from
        - date_to

    - Example:
        ```
        /api/currency-exchanges/list?source_currency=EUR&date_from=2021-02-20&date_to=2021-02-25
        ```

- Calculate amount in a currency exchanged into a different currency

    ```
    /api/currency-exchanges/calculate
    ```

    - Parameters:
        - source_currency
        - amount
        - exchanged_currency

    - Example:
        ```
        /api/currency-exchanges/calculate?source_currency=EUR&amount=200&exchanged_currency=USD
        ```