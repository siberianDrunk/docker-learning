FROM node:lts-alpine as build-stage

WORKDIR /app

COPY ./package.json .

RUN npm install

COPY . .

EXPOSE 9001

CMD ["npm", "run", "dev"]
