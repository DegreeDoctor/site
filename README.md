# Degree Doctor
Degree Doctor is a web app built in Vue that helps students create and manage a plan for their college degree however complex or simple it may be. The data for the app is gathered by scraping RPI's SIS and using the RPI catalog API through python.

## Project Layout
- `/frontend` contains all code for the frontend
- `frontend/src` contains the Vue source code
- `/backend` contains all code for the backend

## Installation
I recommend using some form of Linux to handle installation and running the project locally. If you do not want to install Linux on Windows feel free to use WSL. I have never used Mac so I am not sure what the steps would be for setting up npm.
If you are on Linux I heavily recommend using [NVM](https://github.com/nvm-sh/nvm) then installing npm through it.

For Windows, go to (https://nodejs.org/en/download) and download using the windows installer. Check the "Automatically install the necessary tools..." button. Let the installer do its work through windows powershell. Once it is done, npm works. This may be the same way to install for mac.

Now that you have npm installed follow the following steps to install the project on your machine:
Navigate to the frontend folder
```sh
cd frontend
```
Then run the following command
```sh
npm ci
```
You will now be fully setup to use the project, next check out the following commands to aid development:
Run a local development server.
```sh
npm run dev
```
Compiles for production.
```sh
npm run build
```
Lints the project.
```sh
npm run lint
```
Runs prettier on the source files.
```sh
npm run pretty
```
