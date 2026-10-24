# GameRatingsProj
Final Project for CSCI 3340 @ UTRGV
A video game version of Letterboxd

## About the project

GameRatingsProj is a website where people can browse a catalog of video games, search and filter it, and (planned) log in to rate and review games on a 1-5 scale, like Letterboxd does for movies. It's built with Python and Django, with a SQLite database.

**Team and roles**

| Teammate | Responsibility |
|---|---|
| Celine Giang | Database and catalog: models, seed data, admin, search and filters |
| Katia Garcia | Front end: HTML, CSS, page design |
| Stephanie Rizo | Back end: accounts and ratings|

## Preliminary delivery checklist
 
| Requirement | Where it is |
|---|---|
| Project description | [About the project](#about-the-project) |
| Repository | https://github.com/celinegiang/GameRatingsProj |
| Environment created | Python virtual environment, `requirements.txt`, and setup steps in [How to run it](#how-to-run-it) |
| Agile planning | [Agile planning](#agile-planning) |
 
## Agile planning
 
### Overview and stakeholders
 
GameRatingsProj is a website like Letterboxd, but for video games: people browse a catalog, create an account, and rate and review games.
 
| Stakeholder | What they care about |
|---|---|
| Visitors and gamers (end users) | Finding games and seeing what other people think of them |
| Reviewers (logged-in users) | Rating and reviewing games quickly |
| Catalog maintainer (admin) | Keeping the game data accurate and easy to update |
| Development team (Celine, Katia, Stephanie) | A working project that is easy to build on together |
| Instructor, CSCI 3340 @ UTRGV | A complete project with documented agile planning |
 
### Context and goals
 
**Context:** this is the final project for CSCI 3340. A team of three builds it with Django, split into database, front end and back end.
 
**Goals**
1. Let anyone browse, search and filter a catalog of games.
2. Let users sign up, log in, rate games from 1 to 5, and write short reviews.
3. Show ratings and recent reviews so people can see what others think.
4. Deliver one integrated, documented site that runs from a clean clone.
### Roles
 
| Person | Role |
|---|---|
| Celine Giang | Database and catalog developer (also integration and tests) |
| Katia Garcia | Front end developer |
| Stephanie Rizo | Back end developer (accounts and ratings) |
 
### Timeline and sprints
 
The work is split into 6 sprints, done in order. Each sprint ends with a working version of the site merged into `main`.
 
| Sprint | Goal | Stories | Status |
|---|---|---|---|
| 1 | A searchable game catalog, accounts and the first page designs | A1-A6, B1, B2, D1 | Done |
| 2 | One integrated site where a user can sign up, log in, rate and review | C1-C4, E1, E2 | Done |
| 3 | Connect the front end so the designed pages run inside Django | B3, D2 | Planned |
| 4 | Make the site look and feel like one product | A7, C5, D3 | Planned |
| 5 | More content and more user features | A8, B4, C6, D4 | Planned |
| 6 | Deploy and demo | E3, E4 | Planned |
 
**Done means:** the story is merged into `main` through a pull request and works from a clean clone (`pip install -r requirements.txt`, `python manage.py migrate`, `python manage.py seed_games`).
 
### Initiative, epics and user stories
 
We follow the structure from class: an initiative is broken into epics, and each epic into user stories written as **"As a [persona], I want to [...], so that [...]."** We use plain roles as the persona.
 
```
Initiative: GameRatingsProj, a Letterboxd for video games
├── Epic A: Catalog (Celine)
├── Epic B: Accounts (Stephanie)
├── Epic C: Ratings and reviews (Celine + Stephanie)
├── Epic D: Front end (Katia)
└── Epic E: Project and delivery (whole team)
```
 
**Roles in our stories**
 
| Role | Who they are |
|---|---|
| Visitor | Anyone browsing the site, logged in or not |
| User | Someone with an account who rates and reviews games |
| Admin | The person who keeps the game catalog up to date |
| Developer on the team | One of the three of us building the site |
 
**Epic A: Catalog**
 
| ID | User story | Sprint | Owner | Status |
|---|---|---|---|---|
| A1 | As a developer on the team, I want shared Game, Genre and Platform models, so that all our pages use one data structure. | 1 | Celine | Done |
| A2 | As a visitor, I want to browse a list of games, so that I can discover something to play. | 1 | Celine | Done |
| A3 | As a visitor, I want to search games by title, so that I can quickly find a game I already know. | 1 | Celine | Done |
| A4 | As a visitor, I want to filter games by genre, platform and year, so that I only see games I can play and like. | 1 | Celine | Done |
| A5 | As an admin, I want a dashboard to add and edit games, so that the catalog stays up to date. | 1 | Celine | Done |
| A6 | As a developer on the team, I want one command that loads the same games for everyone, so that we all test with the same data. | 1 | Celine | Done |
| A7 | As a visitor, I want to sort games (top rated, newest) and page through results, so that I can find the best games faster. | 4 | Celine | Planned |
| A8 | As a visitor, I want a bigger catalog with cover images, so that there is more to discover and the site looks real. | 5 | Celine | Planned |
 
**Epic B: Accounts**
 
| ID | User story | Sprint | Owner | Status |
|---|---|---|---|---|
| B1 | As a visitor, I want to sign up for an account, so that I can rate and review games. | 1 | Stephanie | Done |
| B2 | As a user, I want to log in and log out, so that my ratings are tied to me. | 1 | Stephanie | Done |
| B3 | As a new user, I want to see a confirmation message after signing up, so that I know my account was created. | 3 | Stephanie | Planned |
| B4 | As a user, I want a profile page that lists my ratings, so that I can see everything I have rated. | 5 | Stephanie | Planned |
 
**Epic C: Ratings and reviews**
 
| ID | User story | Sprint | Owner | Status |
|---|---|---|---|---|
| C1 | As a user, I want to rate a game from 1 to 5, so that I can show how much I liked it. | 2 | Celine + Stephanie | Done |
| C2 | As a user, I want to write a short review with my rating, so that I can explain my opinion. | 2 | Celine + Stephanie | Done |
| C3 | As a visitor, I want to see average ratings on the game list and game page, so that I can tell which games are well liked. | 2 | Celine + Stephanie | Done |
| C4 | As a visitor, I want to see the most recent reviews on the home page, so that I can see what people are talking about. | 2 | Whole team | Done |
| C5 | As a user, I want a clickable star control for rating, so that rating feels quick and easy. | 4 | Katia + Stephanie | Planned |
| C6 | As a user, I want to edit or delete my own review, so that I can fix mistakes or change my mind. | 5 | Stephanie | Planned |
 
**Epic D: Front end**
 
| ID | User story | Sprint | Owner | Status |
|---|---|---|---|---|
| D1 | As a visitor, I want a designed landing page and About page, so that I understand what the site is. | 1 | Katia | Done (static HTML/CSS) |
| D2 | As a developer on the team, I want the HTML pages turned into Django templates with a `static/` folder, so that the designed pages run inside the site. | 3 | Katia | Planned |
| D3 | As a visitor, I want the game list, game page, login and signup pages to match the site design, so that the site feels like one product. | 4 | Katia | Planned |
| D4 | As a visitor, I want the site to work on my phone, so that I can use it anywhere. | 5 | Katia | Planned |
 
**Epic E: Project and delivery**
 
| ID | User story | Sprint | Owner | Status |
|---|---|---|---|---|
| E1 | As a developer on the team, I want one integrated project with shared URL names and rules, so that our three parts work together. | 2 | Celine | Done |
| E2 | As a developer on the team, I want automated tests for the main flows, so that we notice when one part breaks another. | 2 | Celine | Planned |
| E3 | As a team member, I want the site deployed, so that anyone can use it. | 6 | Whole team | Planned |
| E4 | As a team member, I want a final demo and complete documentation, so that we can present our work. | 6 | Whole team | Planned |
 
## How to run it

**Requirements:** Python 3.12 or newer and Git.

1. Clone the repo and open the folder in VS Code:
   ```
   git clone https://github.com/celinegiang/GameRatingsProj
   cd GameRatingsProj
   ```
2. Create and activate a virtual environment.

   Windows (PowerShell):
   ```
   py -m venv virt
   virt\Scripts\Activate.ps1
   ```
   macOS / Linux / Codespaces:
   ```
   python3 -m venv virt
   source virt/bin/activate
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up the database and load the sample games (use `python3` instead of `python` on macOS/Linux):
   ```
   python manage.py migrate
   python manage.py seed_games
   ```
5. (Optional) Create an admin login:
   ```
   python manage.py createsuperuser
   ```
6. Start the server:
   ```
   python manage.py runserver
   ```
7. Open http://127.0.0.1:8000/ for the home page, http://127.0.0.1:8000/games/ for the game catalog, or http://127.0.0.1:8000/admin/ for the admin dashboard.

`db.sqlite3` is not committed to Git. Every teammate builds their own with `migrate` and `seed_games`, which gives everyone the same data. After pulling new code, run `python manage.py migrate` again in case the database changed.

## Pages

| URL | Name | What it shows | Owner |
|---|---|---|---|
| `/` | `home` | Login/logout links and the most recent reviews | Backend + database |
| `/games/` | `game_list` | The game catalog with search, filters and average ratings | Database |
| `/games/<id>/` | `game_detail` | One game, its rating form and its reviews | Database + backend |
| `/accounts/signup/` | `signup` | Create an account | Backend |
| `/accounts/login/` | `login` | Log in | Backend |
| `/accounts/logout/` | `logout` | Log out (POST) | Backend |
| `/admin/` | | Admin dashboard for adding and editing data | Database |

Search and filters use URL parameters on `/games/`, for example `/games/?q=hades&genre=RPG&platform=PC&year=2020`:
`q` (title or text search), `genre`, `platform`, `year`.

## How the three parts connect
 
One Django project (`gamebox`) with two apps (`games` and `accounts`). Everyone should follow these conventions so the parts keep working together:
 
- **URL names:** use `{% url 'name' %}` in templates and `redirect('name')` in views, never hard-coded paths. The shared names are `home`, `game_list`, `game_detail` (needs a game id), `login`, `logout` and `signup`.
- **Users:** Django's built-in `User`. Anything that points at a user uses `settings.AUTH_USER_MODEL`.
- **Ratings and reviews** live in `games/models.py` (`Rating`, `Review`), not in `accounts`, because they belong to a game. This keeps the two apps from needing to import each other.
- **The rating rules** live in `games/services.py`. To save a rating, call `services.set_rating(user, game, score, review_text)`. To show average ratings, wrap a game queryset in `services.with_rating_stats(games)`, which adds `avg_rating` and `num_ratings`. Please don't re-implement these in views.
- **Template variables:**
  - `home.html`: `recent_reviews`
  - `game_list.html`: `games` (each has `avg_rating`, `num_ratings`, `.genres.all`, `.platforms.all`), `genres`, `platforms`, `years`, `q`, `genre`, `platform`, `year`
  - `game_detail.html`: `game`, `form`, `user_rating`, `avg_rating`, `num_ratings`, `reviews`
- **Template locations:** project-wide pages go in `templates/` (`home.html`, `registration/`), and catalog pages go in `games/templates/games/`.


## Project structure

```
manage.py
GameRatingsProj files from the front end (not wired into Django yet):
  index.html, about.html, style.css, aboutstyle.css
gamebox/                  Django settings and root URLs
accounts/                 signup view (backend)
templates/                home.html, registration/login.html, registration/signup.html
games/
  models.py               Genre, Platform, Game, Rating, Review
  services.py             shared rating rules and queries
  forms.py                RatingForm (score 1-5 plus optional review text)
  admin.py                Admin dashboard setup
  views.py                home, game_list, game_detail
  urls.py                 URLs for the games app
  data/
    games.json            The shared game catalog
    demo_reviews.json     Sample users and reviews for the home page
  management/commands/
    seed_games.py         Loads the catalog and demo reviews
  migrations/             Database changes generated by Django
  templates/games/        game_list.html, game_detail.html
```

### Celine: Database

**Early prototype**
- Wrote a first C++ `GameRatings` class that stored 1-5 ratings per user per game and could add, update and look up ratings. It was later removed once the project moved to Django.

**Django catalog (database end)**
- **Project setup:** created the Django project and `games` app, added `.gitignore` and `requirements.txt`, and registered the app in settings.
- **Database models:** wrote the `Genre`, `Platform` and `Game` models, with many-to-many links from games to genres and platforms and unique titles and names.
- **Migrations:** generated and applied the initial migration that creates the tables.
- **Admin dashboard:** registered the models so data can be added and edited at `/admin/`.
- **Seed command:** wrote `python manage.py seed_games`, which loads `games/data/games.json` and is safe to rerun. The catalog currently has 10 games, 13 genres and 5 platforms.
- **Game list page:** built `/games/` with a view, URL and template, including title search.
- **Filters:** added genre, platform and year filters that combine with search, and ignore invalid input instead of crashing.

**Connecting the three parts**
- **Merged two Django projects into one:** brought the back end's `accounts` app and login/signup templates into the main project, set up the shared template folder, and merged the URL routes.
- **Rating and Review models:** one rating per user per game, enforced by the database, plus optional written reviews.
- **Shared rules in `services.py`:** `set_rating`, `with_rating_stats`, `get_user_rating` and `recent_reviews`, so every page uses the same logic.
- **Views and pages:** added the home page (recent reviews), the game detail page with a rating form, and average ratings on the game list.


### Stephanie: Back end
 
- **Signup:** a `register` view in `accounts/views.py` using Django's built-in `UserCreationForm`. After a successful signup it shows a success message and redirects to the login page.
- **Login and logout:** Django's built-in authentication views, mounted at `/accounts/`. Logging in or out sends the user to the home page.
- **Templates:** `templates/registration/login.html` and `signup.html`, plus the home page's logged-in / logged-out block (welcome message, logout button, login and signup links).

### Katia: Front end
 
- **Landing page:** `index.html` with a hero section, a gallery row, a banner and three feature cards, in a dark purple theme (`style.css`).
- **About page:** `about.html` with its own layout and cards for "Indie Darlings", "AAA Blockbusters" and "Core Gameplay Features & Mechanics" (`aboutstyle.css`).
- **Status:** these pages are plain HTML/CSS files in the repo root and are **not connected to Django yet**. The templates in `templates/` and `games/templates/games/` are unstyled placeholders.

## Working together
 
- Each person works on their own branch and merges into `main` through a pull request.
- After pulling, run `python manage.py migrate` and `python manage.py seed_games`.
- If two people create a migration at the same time, run `python manage.py makemigrations --merge`.
- Never commit `db.sqlite3` or `virt/` (both are in `.gitignore`).

## Planned next steps

- **Database:** sorting (top rated, newest) and pagination, grow the catalog to 40+ games with cover image URLs, polish the admin (columns, filters, search), and more tests for search and filters
- **Front end:** wire `index.html`, `about.html` and the CSS into Django, and style every page
- **Back end:** extend rating and review features, user profile pages, and show messages (like "Account created") on the login page
