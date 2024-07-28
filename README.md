# Flight-Tracker system

  # Objective:
Develop a system to provide real-time flight status updates and notifications to passengers. The system includes a backend API, a frontend interface, and integrates with Firebase for notifications and MySQL for data management.

   # Tech Stack:
1.Frontend: React.js
2.Backend: Python (Flask)
3.Database: MySQL
4.Notifications: Firebase Cloud Messaging
5.Message Queue: RabbitMQ
6.Data Import: CSV files

  # Implementation Details
  
1. Backend Development
Framework: Flask (Python)
Key Components:
API Endpoints: Implemented endpoints to fetch flight status, handle notifications, and integrate with the database.
Database Integration: Connected to MySQL to store and retrieve flight data.
Notifications: Integrated Firebase Admin SDK to send real-time notifications to passengers.
Message Queue: Used RabbitMQ to handle asynchronous tasks and ensure reliable notification delivery.

3. Frontend Development
Framework: React.js
Key Components:
FlightStatus Component: Displays real-time flight status updates.
API Integration: Fetches data from the backend API to update the user interface dynamically.
Error Handling: Managed errors and loading states to enhance user experience.

3. Database Setup
Database: MySQL
Tables:
Flights: Stores flight details such as flight ID, status, gate, and last updated timestamp.
Data Import:
Method: Loaded initial flight data from CSV files into MySQL using LOAD DATA INFILE command.
Schema: Defined table schema to match the data structure in CSV files.

5. Notifications
Service: Firebase Cloud Messaging (FCM)
Setup:
Firebase Admin SDK: Initialized in the backend to send push notifications.
Integration: Configured to send notifications for flight status changes via SMS, email, or app notifications.

7. Message Queue
Tool: RabbitMQ
Usage: Handled background tasks related to sending notifications, ensuring that messages are processed efficiently and reliably.
Deployment and Execution
Frontend: Served using React’s development server (localhost:3001).
Backend: Hosted on a local server or cloud service.
Database: Managed through MySQL Workbench or command line.
Notifications: Configured to trigger notifications based on flight status updates.

 # Libraries and Dependencies Used
 
# 1. Frontend: React.js
React: Core library for building the user interface.

Installation: npm install react react-dom
Axios: Promise-based HTTP client for making API requests.

Installation: npm install axios
React Scripts: Scripts and configuration for Create React App.

Installation: Included by default with Create React App.
React Router DOM: For handling routing in the React application.

Installation: npm install react-router-dom

# 2. Backend: Python (Flask)
Flask: Lightweight WSGI web application framework for building the API.

Installation: pip install Flask
Flask-Cors: Middleware for handling Cross-Origin Resource Sharing (CORS).

Installation: pip install flask-cors
Flask-SQLAlchemy: SQLAlchemy integration for Flask to manage database connections.

Installation: pip install Flask-SQLAlchemy
MySQL Connector/Python: MySQL driver for Python to connect to MySQL database.

Installation: pip install mysql-connector-python
Firebase Admin SDK: For interacting with Firebase to send notifications.

Installation: pip install firebase-admin
RabbitMQ Client: Python client for RabbitMQ.

Installation: pip install pika

# 3. Database: MySQL
MySQL Server: The relational database management system used for storing flight data.

MySQL Workbench: GUI tool for managing MySQL databases.

MySQL Connector: Python library for MySQL database connectivity.

# 4. Notifications: Firebase Cloud Messaging
Firebase Admin SDK: Provides administrative access to Firebase services, including FCM.
Installation: pip install firebase-admin


# 5. Message Queue: RabbitMQ
RabbitMQ: Message broker for managing background tasks and notifications.
Python Client: pip install pika
RabbitMQ Server: The service itself, installed and configured on the server.


# 6. Data Import
CSV Handling:
Python CSV Module: Built-in Python module for handling CSV files.
Command Line Utilities: MySQL’s LOAD DATA INFILE command for importing CSV data into the MySQL database.
 
 
 # Summary of Installation Commands

Frontend:

bash
Copy code
npm install react react-dom axios react-router-dom

Backend:

bash
Copy code
pip install Flask Flask-Cors Flask-SQLAlchemy mysql-connector-python firebase-admin pika

Dependencies Overview
React.js for building the user interface and handling client-side interactions.
Flask and related libraries for developing the backend API.

MySQL for data storage and management.
Firebase Admin SDK for sending notifications.
RabbitMQ for handling background processing and messaging.
This stack ensures a robust, scalable, and maintainable system for providing real-time flight status updates and notifications


  # Summary
The project successfully integrates multiple technologies to provide a seamless experience for passengers needing real-time flight status updates. The frontend communicates with the backend API to display current flight information, while notifications keep passengers informed about any changes. Data management is handled efficiently with MySQL, and RabbitMQ ensures reliable processing of background tasks.

Feel free to reach out if you need more details or have any further questions!
