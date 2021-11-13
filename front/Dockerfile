FROM node:16-alpine as dev

WORKDIR /work/app

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile
COPY . .

FROM node:16-alpine as build

ENV NODE_ENV=production
WORKDIR /work/build

COPY --from=base /work/app ./

RUN yarn build


FROM node:16-slim AS node_modules

WORKDIR /modules

COPY package.json yarn.lock ./
RUN yarn install --non-interactive --frozen-lockfile --production

FROM node:16-slim

ENV NODE_ENV=production
WORKDIR /work/app

COPY package.json yarn.lock next.config.js ./
COPY --from=build /work/build/public ./public
COPY --from=build /work/build/.next ./.next
COPY --from=build /work/build/dist ./dist
COPY --from=node_modules /modules/node_modules ./node_modules

CMD ["yarn", "start"]
