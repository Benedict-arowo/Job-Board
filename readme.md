# Job Board Web Application

A job board web application built using Django and Tailwind CSS. This project allows employers to post job listings, and job seekers to search for and apply to these listings.

## Table of Contents

-   [Features](#features)

-   [Technologies Used](#technologies-used)

-   [Installation](#installation)

-   [Usage](#usage)

-   [Contributing](#contributing)

## Features

- [ ] User authentication for job seekers and employers.
- [ ] Job posting with details such as job title, description, company name, location, and more.
- [ ] Job searching with filtering options.
- [ ] Application submission for job seekers with resume and cover letter attachments.
- [ ] User profiles and company profiles for employers.
- [ ] Email notifications for important events (e.g., new job postings, job applications).
- [ ] Job categories for better organization and searching.
- [ ] User dashboard to manage applications and job listings.
- [ ] Admin panel for site administrators.

## Technologies Used

-   **Django**: A high-level Python web framework.
-   **Tailwind CSS**: A utility-first CSS framework for creating sleek and responsive designs.
-   **Sqlite**: A serverless database

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/job-board.git
cd job-board
```

3. Create a virtual environment and install the required dependencies:

```python
(Linux/macOS)
> python -m venv venv
> source venv/bin/activate

(Windows)
> venv\Scripts\activate
> pip install -r requirements.txt
```

3. Setup the database:

```bash
python manage.py migrate
```

4. Create a super user:

```bash
python manage.py createsuperuser
```

5. Run the development server:
6.

```bash
python manage.py runserver
```

## Usage

1. Access the application by visiting http://localhost:8000 in your web browser.
2. Register as a job seeker or employer, or use the admin superuser account created earlier.
3. Explore the features, create job listings, and start searching for or applying to jobs.

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.
