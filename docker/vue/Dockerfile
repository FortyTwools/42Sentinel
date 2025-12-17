FROM node:lts-alpine

WORKDIR /app

COPY frontend/package.json ./

RUN npm install

COPY frontend/ .

EXPOSE 5173

CMD [ "npm", "run", "dev" ]


## use this later for prod

# build stage
# FROM node:lts-alpine as build-stage
# WORKDIR /app
# COPY frontend/package.json ./
# RUN npm install
# COPY frontend/ .
# RUN npm run build

# # production stage
# FROM nginx:stable-alpine as production-stage
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]