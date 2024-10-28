# Project Name: Best_Location

## Overview
The Best_Location project is an intelligent platform that utilizes advanced AI algorithms to enable users to input the location they wish to purchase and receive an accurate prediction of the profitability of opening a store at that location. This analytical tool provides data-driven insights to aid in strategic and informed decision-making.

## Distinction and Complexity
The Best_Location project leverages advanced AI algorithms to offer a powerful tool for analyzing the profitability of store openings. The system is based on a linear regression model developed using a dataset consisting of 1,000 samples, allowing for precise and practical predictions.

### Distinctive Features
- **Advanced AI**: Utilizing an optimized linear regression model, the system analyzes data such as area number, store size, product grade, and parking availability, enabling users to input this information and estimate profitability percentages.

- **Flexible Containerized Infrastructure**: This project is implemented in a containerized environment, consisting of two independent images. One image is dedicated to the web server, while the other manages a PostgreSQL database. This structure allows the project to run seamlessly in any infrastructure or environment without the need to reinstall libraries and dependencies.

### Technical Complexity
- **Independent Platform**: By employing Docker technology for containerization, all necessary execution requirements are automatically managed. This capability reduces the complexities associated with installation and setup across various environments, ensuring flawless system performance on all platforms.

- **Advanced Front-End Development**: The use of JavaScript in the front end enhances both aesthetics and the efficiency of the website, leading to improved user experience and enabling users to interact with the platform effortlessly.

## Key Features
- **Authentication System**: The website features an authentication system that ensures users must register and log in to access all the platform's functionalities and features.

- **Data Entry for AI Analysis**: Users can easily input the required data, allowing the AI system to conduct analyses and provide more accurate estimates of store profitability.

- **Comprehensive Archive Section**: This section allows users to fully access all previously entered data and the predicted profit percentages provided by the website. Users can browse stored data and delete it if necessary.

## File Contents
1. **Folder: dataset**
   - **Path**: dataset/
   - **data.xlsx**: This Excel file contains our main dataset, comprising 1,001 records with information such as store size, product grade, etc.

2. **Folder: migrations**
   - **Path**: migrations/
   - This folder indicates changes and updates made to the database structure.

3. **Folder: static**
   - **Path**: static/
   - **script.js**: This JavaScript file manages the main page and dynamically displays data regarding profits earned by other users.

4. **Folder: templates**
   - **Path**: templates/
   - This folder contains various HTML files for the website pages, including:
     - **index.html**: Main page
     - **archive.html**: Displays archived information
     - **layout.html**: Overall page template
     - **login.html**: User login page
     - **register.html**: User registration page
     - **result.html**: Displays results
     - **try_AI.html**: User data entry page for analysis

5. **File: admin.py**
   - **Path**: admin.py
   - For managing the Django admin section, displaying and organizing models.

6. **File: apps.py**
   - **Path**: apps.py
   - For configuring the Django application.

7. **File: models.py**
   - **Path**: models.py
   - Contains models used in the database, such as User and Information.

8. **File: urls.py**
   - **Path**: urls.py
   - URL routing to corresponding functions in views.py.

9. **File: views.py**
   - **Path**: views.py
   - Contains main backend functions such as:
     - **index**: Manages the main page
     - **log_in**: Manages user login
     - **logout**: User logout
     - **register**: User registration
     - **predict_profit**: Data analysis and profit prediction
     - **try_AI**: Receives data from users and sends it for analysis
     - **result_view**: Displays results to users
     - **archive**: Displays archived information
     - **delete_information**: Deletes archived data

10. **Folder: location_predictor**
    - **Path**: location_predictor/
    - Contains project settings and URL routing files.

11. **File: Docker-compose.yml**
    - **Path**: Docker-compose.yml
    - Infrastructure settings for running the website and PostgreSQL database.

12. **File: Dockerfile**
    - **Path**: Dockerfile
    - Codes related to containerizing the project.

13. **File: manage.py**
    - **Path**: manage.py
    - Entry point for executing Django management commands.

14. **File: requirements.txt**
    - **Path**: requirements.txt
    - Contains a list of required libraries for the project.

15. **File: wait-for-it.sh**
    - **Path**: wait-for-it.sh
    - A script ensuring that the PostgreSQL database is up and ready.

## How to Run

1. Install [Python](https://www.python.org/downloads/).
2. Clone the repository: `git clone https://github.com/mehrad-RT/Best_Location.git`.
3. Navigate to the project directory: `cd Best_Location`.
4. Install [Docker](https://docs.docker.com/engine/install/).
5. Run the project: `Docker-compose up`.

## Contributing

If you have any suggestions to improve this project, please feel free to fork the repository and submit a pull request. Alternatively, you can simply open an issue and tag it as “enhancement.” We would also appreciate it if you could give the project a star⭐. Thank you once again!

1. Fork the Project
2. Create your Feature Branch (e.g., `git checkout -b feature/AmazingFeature`)
3. Commit your Changes (e.g., `git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (e.g., `git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is distributed under the MIT License.
