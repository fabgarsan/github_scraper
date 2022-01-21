#!/bin/zsh
cd backend && pipenv lock -r > requirements.txt && cd .. && docker-compose up --build