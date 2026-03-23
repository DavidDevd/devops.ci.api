FROM node:24 AS build

WORKDIR /user/src/app

COPY package*.json ./

RUN yarn 

COPY . .

RUN yarn run build
RUN npm ci --omit=dev

FROM node:24-alpine3.22

COPY --from=build /user/src/app/package.json ./package.json
COPY --from=build /user/src/app/dist ./dist
COPY --from=build /user/src/app/node_modules ./node_modules

EXPOSE 3000

CMD ["yarn" , "run" , "start:prod"]