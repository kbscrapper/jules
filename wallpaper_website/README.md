# Modern Wallpaper Website

This project is a simple wallpaper download website built with Python and Django. It features a public-facing site for browsing and downloading wallpapers, and an admin panel for uploading and managing content.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- pip (Python package installer)
- Django (will be installed via requirements.txt)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url> 
    # Replace <repository_url> with the actual URL where this project will be hosted.
    # For now, you can just mention "Clone this repository".
    cd wallpaper_website
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    (First, ensure `requirements.txt` exists. This will be created in the next step of the overall plan, but the README should mention it).
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser account (for accessing the admin panel):**
    ```bash
    python manage.py createsuperuser
    ```
    (Follow the prompts to choose a username, email, and password).

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## How to Access

-   **Main Website:** Open your browser and go to `http://127.0.0.1:8000/`
-   **Admin Panel:** Open your browser and go to `http://127.0.0.1:8000/admin/`
    - Log in with the superuser credentials you created.

## Using the Admin Panel

1.  Navigate to the Admin Panel.
2.  Log in with your superuser account.
3.  You can manage `Tags` and `Wallpapers`.
    -   **To add a new wallpaper:**
        -   Go to the "Wallpapers" section.
        -   Click "Add wallpaper".
        -   Fill in the title, upload an image, and optionally add a description and tags.
        -   Save the wallpaper. It will then appear on the main website.
```
