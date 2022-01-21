FROM node:15-alpine

WORKDIR /usr/src/socket_server
COPY package*.json ./

RUN npm install -g npm@8.3.1
RUN npm install nodemon -g
RUN npm i --silent

EXPOSE 3000

CMD ["nodemon", "index.js"]
