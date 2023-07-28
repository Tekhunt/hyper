# Hyper9 - Interns Management System

Hyper9 is an Interns Management System, designed to facilitate the management and tracking of interns and their activities within an organization. The system allows Operational Managers to assign interns to themselves and track their Key Performance Indicators (KPIs) such as Pull Requests, StackOverflow Engagements, Blogs, GitHub Issues, and Twitter Posts.

## Table of Contents
- Getting Started
- Prerequisites
- Installation
- Usage


## Getting Started

### Prerequisites
Before running the Hyper9 application, ensure you have the following installed on your system:

- Python 3.9
- Docker (if you want to run the application in containers)

### Installation
Follow the steps below to set up the Hyper9 application on your local system:

1. Clone the repository:
- `git clone https://github.com/yourusername/hyper9.git`
- `cd hyper9`
2. Create a virtual environment and activate it:
- `python3 -m venv henv`
- `source henv/bin/activate`

Install the required Python packages:
- `pip install -r requirements.txt`
- `python manage.py runserver`

3. Build the Docker image:
- `docker-compose up --build`

>> The application will be accessible at http://localhost:9000/

## Usage

Access the Hyper9 application in your web browser by navigating to http://localhost:9000/api/v1/welcome/ to see endpoints accessible.

Use the provided API endpoints to manage interns, operational managers, and their activities
