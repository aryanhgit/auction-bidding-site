# Auction House

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0-green.svg)](https://www.djangoproject.com/)
[![Database](https://img.shields.io/badge/Database-SQLite3-blueviolet.svg)](https://www.sqlite.org/)
[![Frontend](https://img.shields.io/badge/Frontend-Bootstrap%204-orange.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A full-stack web application built with **Django** that allows users to create, browse, bid on, and comment on auction listings, as well as manage personal watchlists and view items by category.

---

## Features

- **User Authentication**
  - Register, Login, Logout
  - Secure password management

- **Auction Listings**
  - Create, view, and manage auction listings
  - Close listings to finalize the winner
  - Display winners after auction ends

- **Bidding System**
  - Place bids on items
  - Enforce valid bidding rules (higher than current price)

- **Watchlist**
  - Add and remove listings from Watchlist
  - View Watchlist items separately

- **Comments**
  - Comment on active listings
  - View discussion thread on listings

- **Categories**
  - Browse listings by category

- **Django Admin**
  - Manage listings, bids, and comments through Django Admin Interface

---

## Models

- **User**
  - Inherits from Django’s `AbstractUser`
  
- **Listing**
  - Title
  - Description
  - Starting Bid
  - Image URL (optional)
  - Category (optional)
  - Owner (User)
  - Active Status (Boolean)

- **Bid**
  - Amount
  - Bidder (User)
  - Listing Reference

- **Comment**
  - Text
  - Commenter (User)
  - Listing Reference

---

## Technologies Used

- **Backend:** Django (Python)
- **Database:** SQLite (easy development) / PostgreSQL (optional for production)
- **Frontend:** HTML5, CSS3, Bootstrap 4
- **Authentication:** Django built-in authentication system
- **Deployment (optional):** Render / Vercel / Heroku

---

## Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aryanhgit/auction-bidding-site.git
   cd auction-bidding-site
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
   
3. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create an admin user:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Visit your site:**
   - `http://127.0.0.1:8000/`

---

## Future Improvements

- Real-time bidding with Django Channels (WebSockets)
- Email notifications for auction updates
- Enhanced filtering and search functionality
- User profile pages with their own auction history
