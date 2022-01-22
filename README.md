<h1 align="center">Welcome to GitHub Scraper 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

> A dockerized app built to track GitHub's accounts information. It's called GitHub Scraper.

## Stack

### Build with

* Python
* Docker
* Postgres
* JavaScript
* Celery
* Django Rest Framework
* Node
* Express
* Socket.io
* [Django](https://www.djangoproject.com/)
* [Vue](https://vuejs.org/)

## Install

### Run with docker

**Be sure you are created the .env file in the root of the project. You could use .env_sample as a template.**

You must have Docker installed, and you must run at the root of the project the following command.

```
docker-compose up
```

This project is dockerized and uses docker-compose as an orchestrator.

## Usage

## Backend

### Backend Apis

The backend provides three different endpoints:

#### Cron Query

http://0.0.0.0:8000/api/github/cron_query/

This endpoint receives two arguments:
> username: The username name for the user to be scraped, for example fabgarsan.

> countdown: The seconds to wait to run the scraping process.

#### Get User List

http://0.0.0.0:8000/api/github/github_user_list/

This endpoint lists all the users that have been previously scraped

#### Get User Repository List

http://0.0.0.0:8000/api/github/github_user_repositories?user_id={user_id}

This endpoint lists all the user's repositories that have been previously scraped

> user_id: The user's id who the repositories' is owner

### Backend Admin

In case you want to get into the Django Admin's console

#### Username

admin

#### Default Password

1234567890

## Frontend

To get into the frontend you will be able to do it with http://0.0.0.0:8080/

The frontend is a "Testing Dashboard" where users can cron queries, in seconds, to scrape GitHub's users.

**Be sure you are created the .env file in the frontend folder. You could use .env_sample as a template.**

![ScreenShot](/DashboardTest.png)

### Cron Queries

There will be two fields:
> Username to scrape: Here you can set the username of the user you want to scrape. For instance, fabgarsan.

> Run in seconds: Here you can set the seconds you want to wait to run the query. Default is 5 seconds.

### Fetch Data

You will be able to fetch the data related to the GitHub's users already scraped.

Pushing the button "Fetch Users" will bring all those users that have scraped.

By clicking on any element in the list provided, you will be able to see all the repositories related with the user
selected.

### Synchronized User

A list filled through sockets shows the synchronized users by the backend, listing them at the moment the data is
fetched.

## Author

👤 **Fabio Garcia Sanchez**

* Github: [@fabgarsan](https://github.com/fabgarsan)
* LinkedIn: [@fabgarsan](https://linkedin.com/in/fabgarsan)

## Conclusions

The GitHub scraper will be a not-blocking app that will allow saving data from GitHub's users including their
repositories.

The GitHub Scraper will queue calls by cron in seconds to save data from user and their repositories.

It will always return a success status code from the api call Cron Query in order of being transparent.
***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
