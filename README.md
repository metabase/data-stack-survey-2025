# Metabase Community Data Stack Survey 2025 - raw data

About: In the northern hemisphere summer of 2025, we surveyed 338 companies on how they choose and use their modern data stack-and how AI is shaping their workflows. This repo spins up Metabase and loads the raw survey responses so you can explore them yourself. Curious about our take? [Here is the full report](https://metabase.com/data-stack-report-2025?utm_source=github&utm_medium=repo&utm_campaign=data-stack-report-2025).

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

    This command starts Metabase and setup services defined in the [docker-compose.yaml](docker-compose.yaml) file. Metabase will be accessible at `http://localhost:3000`.

## Usage

1.  **Access Metabase:**

    Open your web browser and go to `http://localhost:3000`.

2.  **Initial Setup:**

    The `setup` service should automatically configure Metabase. If it fails, you may need to check the logs and retry.

3.  **Login:**

    Log in with the credentials defined in [setup.py](setup.py):

    *   Email: `test@test.com`
    *   Password: `metabot1`

4.  **Explore the Data:**

    The "Data Stack Survey 2025" SQLite database should be automatically connected. You can start exploring the data and creating dashboards.

## Troubleshooting

*   **Metabase not accessible:**

    Ensure that the Docker containers are running correctly. Check the logs using `docker-compose logs metabase` and `docker-compose logs setup`.

*   **Setup script fails:**

    Check the logs of the `setup` container for any errors. You might need to adjust the `host` and `port` environment variables in the [docker-compose.yaml](docker-compose.yaml) file if Metabase is not running on `http://localhost:3000`. You can also try setting the `retry` environment variable to `yes` to rerun the setup after Metabase is running.
