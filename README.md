# Django Recipe Sharing Application

This application allows users to authenticate, share, and create their own recipes. Follow the instructions below to get started with your local development environment.

## Prerequisites

Before you start, ensure you have the following installed:

- Docker and Docker Compose
- Python 3
- pip (Python package manager)
- Virtualenv (optional, but recommended for creating isolated Python environments)

## Initial Setup

We've simplified the setup process with a Makefile. Each step of the setup process can be executed with simple make commands.

### Step 1: Start PostgreSQL Database

First, start the PostgreSQL database using Docker:

```bash
make postgres
```

### Step 2: Create Database

After starting the PostgreSQL container, create the recipes database:

```bash
make createdb
```

### Step 3: Create python virtual environment

Create a virtual environment for the project:

```bash
make env
```

install the dependencies:

```bash
make pip install -r requirements.txt

```

#### Step 4: Apply Migrations

Before running the application, apply migrations to set up your database schema:

```bash
make migrations
```

Then, apply the migrations:

```bash
make migrate
```

### Step 5: Run

Finally, run the application:

```bash
make server
```

The application will be accessible at http://127.0.0.1:8000/.
