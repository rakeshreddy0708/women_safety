

# Use the official Node.js image as a build stage
FROM node:18 AS build-stage
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Use an Nginx image to serve the built files
FROM nginx:1.21.6-alpine
COPY --from=build-stage /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
