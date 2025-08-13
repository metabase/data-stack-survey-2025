# Metabase Data Stack Setup

This project sets up Metabase with a SQLite database for data analysis.

## Prerequisites

- Docker
- Docker Compose

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Run docker compose:**

    ```bash
    docker-compose up -d
    ```

    This command builds and starts the Metabase and setup services defined in the [docker-compose.yaml](docker-compose.yaml) file. Metabase will be accessible at `http://localhost:3000`.

## Usage

1.  **Access Metabase:**

    Open your web browser and go to `http://localhost:3000`.

2.  **Initial Setup:**

    The `setup` service should automatically configure Metabase. If it fails, you may need to check the logs and retry.

3.  **Login:**

    Log in with the credentials defined in [setup.py](setup.py):

    *   Email: `a@b.com`
    *   Password: `metabot1`

4.  **Explore the Data:**

    The "Data Stack Survey 2025" SQLite database should be automatically connected. You can start exploring the data and creating dashboards.

## Troubleshooting

*   **Metabase not accessible:**

    Ensure that the Docker containers are running correctly. Check the logs using `docker-compose logs metabase` and `docker-compose logs setup`.

*   **Setup script fails:**

    Check the logs of the `setup` container for any errors. You might need to adjust the `host` and `port` environment variables in the [docker-compose.yaml](docker-compose.yaml) file if Metabase is not running on `http://localhost:3000`. You can also try setting the `retry` environment variable to `yes` to rerun the setup after Metabase is running.
