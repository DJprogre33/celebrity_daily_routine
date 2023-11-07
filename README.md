# celebrity_daily_routine
Microservice for task manager mobile app

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/DJprogre33/ticket_system.git
   cd your-repo
   ```
2. Create an .env file with the required environment variables:
   ```sh
   cp .env.example .env
   ```
3. Build and start the containers using Docker Compose:
   ```sh
   docker-compose up -d --build
   ```
   This command will build all the containers and run them in the background. If all configurations are correct, you should see your application running and ready to use.

4. Open your web browser and navigate to http://localhost:9000 (depending on the docker compose file settings). You should see your application up and running in the browser.
5. Visit http://localhost:9000/docs to access Swagger documentation
6. If you want to stop and remove the containers, run the following command:
   ```sh
   docker-compose down
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>