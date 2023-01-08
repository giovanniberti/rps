# Rock Paper Scissors API

Hello :)

This is a simple Django project implementing a Rock-Paper-Scissors API to play the game.

## How to run

### With `poetry` (recommended)

If you have [`poetry`](https://python-poetry.org/) installed, you can just

```bash
$ poetry install
```

To get a fresh virtual environment with all dependencies.

Then run DB migrations with

```bash
$ poetry run python manage.py migrate
```

And run the server with

```bash
$ poetry run python manage.py runserver 8080
```

to start the server locally at port 8080.

### Without `poetry`

All dependencies are listed inside `pyproject.toml`.

Assuming you have all of them installed, you can run DB migrations and start the server with:

```bash
$ python manage.py migrate
$ python manage.py runserver 8080
```

## Calling the API

Once you have the server up and running you can test the API with a POST call at `/rps/`.

The body should be a JSON payload with the following format:
```json
{
  "choice": "$CHOICE"
}
```

Where `$CHOICE` is either `ROCK`, `PAPER` or `SCISSORS`.

You can try this cURL command for a quick check:

```bash
$ curl http://127.0.0.1:8080/rps/ -X POST -d '{ "choice": "ROCK" }'
```

The expected output is a JSON with the format:
```json
{
  "outcome": "$OUTCOME"
}
```

Where `$OUTCOME` is either `draw`, `win` or `lose`.

You can check the hand that the computer played by inspecting the logs.

Note that currently the computer chooses which hand to play randomly with a uniform distribution.
