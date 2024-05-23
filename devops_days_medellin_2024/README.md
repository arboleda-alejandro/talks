# Instructions to Run the "get_attendee" Project

## Requirements
1. Tested with python==3.11.5
2. Docker and Docker Compose

## Installing Dependencies

1. Clone this project and enter to `devops_days_medellin_2024/get_attendee` folder

    ```bash
    cd devops_days_medellin_2024/get_attendee
    ```

2. Create and activate a virtual environment, or use your local python setup (not recommended)

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Docker Compose Configuration

1. Enter to `otlp/opentelemetry-collector-contrib`

    ```bash
    cd ../otlp/opentelemetry-collector-contrib
    ```

3. Start the services with Docker Compose:

    ```bash
    docker-compose up -d
    ```

4. Verify containers are up and running:

    ```bash
    docker ps
    ```

## Running the Scripts

1. To run the automatic instrumented script (`get_attendees_autoinstrumented.py`) move to `get_attendee` folder an execute like this:

    ```bash
    cd ../../get_attendee
    ```

    ```bash
    python get_attendees_autoinstrumented.py
    ```

2. To run the manual instrumented script (`get_attendees_manualinstrumented.py`):

    ```bash
    python get_attendees_manualinstrumented.py
    ```

3. Open `zipkin` on this url: http://0.0.0.0:9411/

4. Open `jaeger` on this url: http://0.0.0.0:16686/