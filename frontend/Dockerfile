FROM node:lts-alpine
LABEL authors="Гриша"

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build
