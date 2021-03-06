django-init 
============

(formerly known as django-cookiecutter)

[![Build Status](https://travis-ci.org/Fueled/django-init.svg?branch=user-app)](https://travis-ci.org/Fueled/django-init)

Project template for django based projects, optimized for making REST API with deployment on Heroku and EC2 instances.

## Features

- Django 1.9.x
- PostresSQL everywhere(support of postgis is available).
- [Procfile] for deploying to Heroku.
- [Ansible] script for quick deployment to Ubuntu based servers.
- [12-Factor][12factor] based settings management via [django-environ], reads settings from `.env` if present.
- Designed to work with Django Rest Framework 3.0+.
- Uses `django_sites` instead of `django.contrib.sites`
- Use [mkdocs] for project documentation.
- Uses [py.test] as test runner.
- `travis.yml` for running isolated tests and deployments to dev/qa/prod environment on Heroku from git branches.
- Custom User app, for easier extensibility.
- Optional media storage using Amazon S3
- Livereloading of browser in development via [devrecargar]
- robots.txt and humans.txt configured

## Getting Started

Install cookiecutter with `brew install cookiecutter` or `pip install cookiecutter`.

```
cookiecutter gh:Fueled/django-init
```

It will ask you couple of questions required to generate the project. It will generate a folder containing all the files in your current working directory. 

If you opt to setup the project automatically, it will also:
- initialize a git repo and bump initial tag and version.
- create a virtualenv in the folder `venv` inside the project.
- install all the python dependencies inside it.
- try to create a postgres database and run the initial migration against it.

then only thing you'll need to do is:

1. `cd` into the new `github_repository` folder just created.
2. Activate virtualenv `source venv/bin/activate`.
3. Run `fab serve` or `./manage.py runserver`

Don't forget to carefully look at the generated README. Awesome, right?

You can also explore the [wiki] section for details on advance setups and usuages.

## Changelogs

Refer to [CHANGELOG.md](CHANGELOG.md).

--------

Built with ♥ at [Fueled](http://fueled.com)

[wiki]: https://github.com/Fueled/django-init/wiki
[mkdocs]: http://www.mkdocs.org/
[12factor]: http://12factor.net
[py.test]: http://pytest.org/
[Procfile]: https://devcenter.heroku.com/articles/procfile
[django-environ]: https://github.com/joke2k/django-environ
[Ansible]: http://docs.ansible.com/index.html
[devrecargar]: https://github.com/scottwoodall/django-devrecargar
