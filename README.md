# Fitness Studio

## Setup Steps

### Clone Repository

```bash
git clone https://github.com/heydhruv/fitness-studio.git
cd fitness-studio
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn booking_api.main:app --reload
```

## Check Swagger for API Documentation.
