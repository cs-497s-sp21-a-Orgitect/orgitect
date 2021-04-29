# Docker Node.js

How to use the exemplar files for Docker with Node.js

## Steps for Windows

0. Install Docker Desktop
1. Copy the three files: `.dockerignore`, `docker-compose.yml`, and `Dockerfile`
2. Paste them in the same folder as your `package.json` file
3. Edit the `docker-compose.yml`. You will need to change:
    * `your-service-name` to the name of your microservice
    * `your-server-script.js` to the name of the script that should be run by node to start your server 
    * `1234` to a different port. It must be different from the other microservices, and different from the other ports in use on your system
    * (might not need to change) `80` to the port that you use with your code in Express. But if you already use port 80 in your code then you're good
4. Open command prompt in the folder. [Here are some steps](https://stackoverflow.com/a/60914) for doing this quickly.
5. Run `docker-compose up --build`. When you change your code, you need to go back to this command prompt window, press Ctrl+C, and then run `docker-compose up --build` again for your changes to be updated.
6. Then you should be able to access your app at `http://localhost:1234` (except 1234 is replaced by the unique port you chose in step 3)
7. Create a Docker Hub account using the linked instructions. **Skip any steps about connecting to GitHub**. Just make a public repository and then follow the steps for pushing your image. The instructions are [here](https://docs.docker.com/docker-hub/). If you make changes to your code, you will need to repeat the steps to build, tag, and upload your image to Docker Hub.
8. Send the link to your public repository in Discord so that we can either run the image locally or on AWS for the demo