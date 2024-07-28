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


  # Summary
The project successfully integrates multiple technologies to provide a seamless experience for passengers needing real-time flight status updates. The frontend communicates with the backend API to display current flight information, while notifications keep passengers informed about any changes. Data management is handled efficiently with MySQL, and RabbitMQ ensures reliable processing of background tasks.

Feel free to reach out if you need more details or have any further questions!
