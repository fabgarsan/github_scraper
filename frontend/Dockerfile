FROM node:15-alpine

WORKDIR /usr/src/frontend
COPY package*.json ./

RUN npm install -g npm@8.3.1
RUN npm i --silent

EXPOSE 8080

CMD ["npm", "run", "serve"]
