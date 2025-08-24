<img width="939" height="912" alt="image" src="https://github.com/user-attachments/assets/1878e876-9e67-4c8c-aa17-9361a481fb11" /># Sensor Dashboard

This project implements a real-time sensor data dashboard using FastAPI for the backend and Server-Sent Events (SSE) to push data to a simple HTML frontend. The dashboard visualizes simulated sensor readings.

![dashboard](https://github.com/user-attachments/assets/77f59aa8-c954-4e0a-9ef6-c69f30b91a66)


## Features

- Real-time sensor data visualization.
- Backend built with FastAPI, providing a RESTful API and SSE endpoint.
- Frontend uses HTML, CSS (DaisyUI/TailwindCSS), and JavaScript to display dynamic charts.
- Automated testing with `pytest`.

## Project Structure

```
sensor-dashboard/
├── .venv/                  # Python virtual environment
├── app.py                  # FastAPI application entry point
├── utils.py                # Utility functions and data models (SensorData, recent_readings)
├── test_app.py             # Pytest unit tests for the application
├── templates/              # HTML templates
│   ├── base.html           # Base HTML structure
│   ├── index.html          # Main dashboard page
│   └── chart_data.html     # Partial HTML for chart data updates
├── pyproject.toml          # Project dependencies and metadata
├── uv.lock                 # UV lock file for dependencies
└── README.md               # This README file
```

## Setup and Installation

Follow these steps to set up and run the project locally:

1.  **Navigate to the project directory:**

    ```bash
    cd sensor-dashboard
    ```

2.  **Install dependencies using `uv`:**

    If you don't have `uv` installed, you can install it via `pip`:
    ```bash
    pip install uv
    ```

    Then, install the project dependencies:
    ```bash
    uv pip install -r requirements.txt
    # (Note: If requirements.txt is not present, uv will install from pyproject.toml)
    ```
    *Self-correction: The project uses `pyproject.toml` and `uv.lock` for dependency management. `uv pip install` without `-r` will install from `pyproject.toml`.*

3.  **Run the application:**

    ```bash
    uvicorn app:app --reload --port 8000
    ```

    The application will be accessible at `http://127.0.0.1:8000`.

## Running Tests

To run the unit tests for the application, ensure you have `pytest` and `httpx` installed (they should be installed with the main dependencies if using `uv`):

```bash
uv run pytest test_app.py
```

This will execute the tests defined in `test_app.py`.
