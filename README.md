[![License: MIT](https://img.shields.io/github/license/vintasoftware/django-react-boilerplate.svg)](LICENSE.txt)

# Djangá

## About
A [Django](https://www.djangoproject.com/) project boilerplate/template with lots of state of the art libraries and tools like:
- [React](https://facebook.github.io/react/), for building interactive UIs
- [django-js-reverse](https://github.com/ierror/django-js-reverse), for generating URLs on JS
- [Bootstrap 4](https://v4-alpha.getbootstrap.com/), for responsive styling
- [Webpack](https://webpack.js.org/), for bundling static assets
- [Celery](http://www.celeryproject.org/), for background worker tasks
- [WhiteNoise](http://whitenoise.evans.io/en/stable/) with [brotlipy](https://github.com/python-hyper/brotlipy), for efficient static files serving
- [prospector](https://prospector.landscape.io/en/master/) and [ESLint](https://eslint.org/) with [pre-commit](http://pre-commit.com/) for automated quality assurance (does not replace proper testing!)

For continuous integration, a [CircleCI](https://circleci.com/) configuration `.circleci/config.yml` is included.

Also, includes a Heroku `app.json` and a working Django `production.py` settings, enabling easy deployments with ['Deploy to Heroku' button](https://devcenter.heroku.com/articles/heroku-button). Those Heroku plugins are included in `app.json`:
- PostgreSQL, for DB
- Redis, for Celery
- Sendgrid, for e-mail sending
- Papertrail, for logs and platform errors alerts (must set them manually)

This is a good starting point for modern Python/JavaScript web projects.

## Running
### Setup
- Inside the `backend` folder, do the following:
- Create a copy of ``djanga/settings/local.py.example``:  
  `cp djanga/settings/local.py.example djanga/settings/local.py` (remembering you should replace `djanga` with your project's name!).
- Create a copy of ``.env.example``:  
  `cp .env.example .env`
- Create the migrations for `users` app (do this, then remove this line from the README):  
  `python manage.py makemigrations`
- Run the migrations:  
  `python manage.py migrate`

### Tools
- Setup [editorconfig](http://editorconfig.org/), [prospector](https://prospector.landscape.io/en/master/) and [ESLint](http://eslint.org/) in the text editor you will use to develop.

### Running the project
- Open a command line window and go to the project's directory.
- `pipenv install --dev`
- `npm install`
- `npm run start`
- Open another command line window and go to the `backend` directory.
- `pipenv shell`
- `python manage.py runserver`

#### Celery
- Open a command line window and go to the project's directory
- `pipenv shell`
- `python manage.py celery`

### Testing
`make test`

Will run django tests using `--keepdb` and `--parallel`. You may pass a path to the desired test module in the make command. E.g.:

`make test someapp.tests.test_views`

### Adding new pypi libs
Just run `pipenv install LIB_NAME_ON_PYPI` and then `pipenv lock` to lock the version in Pipfile.lock file

## Linting
- Manually with `prospector` and `npm run lint` on project root.
- During development with an editor compatible with prospector and ESLint.

## Pre-commit hooks
- Run `pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.

## Commercial Support
This project, as other Vinta open-source projects, is used in products of Vinta clients. We are always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br

Copyright (c) 2018 Vinta Serviços e Soluções Tecnológicas Ltda.
[MIT License](LICENSE.txt)
