# Best_Location 🏪

## Overview
Best_Location is an intelligent platform leveraging AI algorithms to predict store location profitability. Users can input location details and receive data-driven predictions about the potential success of opening a store in that area, enabling strategic business decisions.

## Key Features 🎯

### 💡 AI-Powered Analysis
- Advanced linear regression model
- Analysis based on 1,000 data samples
- Predicts profitability based on multiple factors:
  - Area metrics
  - Store size
  - Product grade
  - Parking availability

### 🔐 User Authentication
- Secure registration and login system
- Protected access to platform features
- User-specific data management

### 📊 Data Management
- Comprehensive archive system
- Historical data tracking
- Easy data deletion capability
- Access to previous predictions

### 🔄 Containerized Infrastructure
- Two independent Docker containers:
  - Web server container
  - PostgreSQL database container
- Platform-independent deployment
- Simplified installation process

## Technical Architecture 🏗️

### Project Structure
```
Best_Location/
├── dataset/
│   └── data.xlsx
├── migrations/
├── static/
│   └── script.js
├── templates/
│   ├── index.html
│   ├── archive.html
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   ├── result.html
│   └── try_AI.html
├── location_predictor/
├── admin.py
├── apps.py
├── models.py
├── urls.py
├── views.py
├── Docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
└── wait-for-it.sh
```

### Core Components
- **Frontend**: JavaScript-enhanced UI for seamless user interaction
- **Backend**: Django-powered server with AI integration
- **Database**: PostgreSQL for robust data storage
- **AI Model**: Linear regression model trained on 1,000+ samples
- **Docker**: Containerized deployment for consistent performance

## Installation Guide 🚀

### Prerequisites
- [Python](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/engine/install/)

### Setup Steps
1. Clone the repository
```bash
git clone https://github.com/mehrad-RT/Best_Location.git
```

2. Navigate to project directory
```bash
cd Best_Location
```

3. Start the application
```bash
docker-compose up
```

## Usage Guide 📖
1. Register for a new account
2. Log in to access the platform
3. Navigate to the AI analysis section
4. Input location and store details
5. Receive profitability predictions
6. Access your prediction history in the archive section

## Contributing 🤝
We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch
```bash
git checkout -b feature/YourFeature
```
3. Commit your changes
```bash
git commit -m 'Add YourFeature'
```
4. Push to the branch
```bash
git push origin feature/YourFeature
```
5. Open a Pull Request

## Technical Details ⚙️
- **AI Model**: Linear regression trained on 1,000+ samples
- **Backend Framework**: Django
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django built-in auth system

## License 📝
Distributed under the MIT License. See [License](LICENSE) for more information.

---
Built with ❤️ by Mehrad-RT
