<div align="center">

# Movie Reviews

A Django web application for browsing movies, searching by title, viewing statistics, and reading the latest movie-related news.

<br/>

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)

</div>

## Overview

Movie Reviews is a full-stack web application that allows users to browse a collection of movies, search by title, view detailed statistics about the movie database, and keep up with the latest movie news. The application features a clean interface with search functionality, dynamic charts showing movie distribution by year and genre, and a news section for updates.

Built with Django and Python, the project demonstrates key web development concepts including database management, data visualization with Matplotlib, and responsive template design.

## Features

- **Movie Database**: Browse a comprehensive collection of movies with titles, descriptions, genres, and release years
- **Search Functionality**: Quick search to filter movies by title
- **Statistics Dashboard**: Visual charts displaying movie distribution by year and genre
- **News Section**: Stay updated with the latest movie-related news articles
- **User Authentication**: Signup functionality for user registration
- **Media Management**: Support for movie poster images with Django's media handling

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/moviereviewsproject.git
cd moviereviewsproject
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp config/.env.example .env
# Edit .env with your configuration
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Load initial movie data:
```bash
python manage.py add_movies_db
```

7. Start the development server:
```bash
python manage.py runserver
```

8. Open your browser and navigate to `http://localhost:8000`

## Project Structure

```
moviereviewsproject/
├── movie/                    # Movie app
│   ├── models.py            # Movie model
│   ├── views.py             # Views for home, search, statistics, etc.
│   ├── templates/           # Movie-related templates
│   └── management/          
│       └── commands/        # Custom management commands
│           └── add_movies_db.py  # Load movies from JSON
├── news/                    # News app
│   ├── models.py            # News model
│   ├── views.py             # News display views
│   └── templates/           # News templates
├── moviereviews/            # Project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # URL routing
│   └── templates/           # Base templates
├── media/                   # Uploaded media files
├── config/                  # Configuration files
│   └── .env.example        # Environment variables template
├── requirements.txt         # Python dependencies
└── manage.py               # Django management script
```

## Configuration

### Environment Variables

Copy `config/.env.example` to `.env` and configure:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database

The project uses SQLite by default. For production, configure PostgreSQL or MySQL in `settings.py`.

### Media Files

Movie posters are stored in `media/movie/images/`. Ensure the media directory has proper write permissions.

## Usage

### Adding Movies

Use the custom management command to load movies from JSON:

```bash
python manage.py add_movies_db
```

The command reads from `movie/management/commands/movies.json` and populates the database.

### Viewing Statistics

Navigate to `/statistics/` to view:
- Bar chart of movies by release year
- Bar chart of movies by genre

## Dependencies

- **Django 5.0+**: Web framework
- **Pillow**: Image processing for movie posters
- **pandas**: Data manipulation
- **matplotlib**: Chart generation for statistics

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- Project developed as part of EAFIT University coursework (Semestre 7, Proyecto 1)
