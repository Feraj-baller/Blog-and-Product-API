# Blog & Product API — Django + Django REST Framework

This is a RESTful API built using Django and Django REST Framework (DRF). It handles basic CRUD operations for blog posts and products.

---

## 📁 Features

### 📝 Blog APIs
- `GET /all-blogs/` – Fetch all blog posts
- `POST /create-blog/` – Create a new blog post
- `GET /get-single-blog/<int:id>/` – Fetch a single blog post
- `PUT/PATCH /update-blog/<int:id>/` – Update a blog post
- `DELETE /delete-blog/<int:id>/` – Delete a blog post

### 📦 Product APIs
- `GET /all-products/` – Fetch all products
- `POST /create-product/` – Create a new product
- `GET /get-single-product/<int:id>/` – Fetch a single product
- `PUT/PATCH /update-product/<int:id>/` – Update a product
- `DELETE /delete-product/<int:id>/` – Delete a product

---

## 🛠 Tech Stack

- **Python** 3.x
- **Django** 4.x
- **Django REST Framework** (DRF)
- **SQLite** (default dev DB)

---

## 🧪 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/feraj-baller/<your-repo-name>.git
   cd <your-repo-name>
Set up virtual environment

bash
Copy
Edit
python -m venv env
source env/bin/activate   # or env\Scripts\activate on Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations

bash
Copy
Edit
python manage.py migrate
Start the server

bash
Copy
Edit
python manage.py runserver
Test using Postman or any REST client

🧾 Example Request (POST /blogs/)
json
Copy
Edit
{
  "title": "My First Blog",
  "author": "Feranmi",
  "published_date": "2025-06-20",
  "description": "This is a blog post about Django and DRF."
}
🧯 Error Handling
Proper error messages for:

Invalid or missing fields (400)

Not found resources (404)

Uses status from DRF for readability

🔐 Optional Improvements
Add serializers for better validation (already suggested)

Implement pagination for blog/product list

Protect routes with authentication using DRF's TokenAuth or JWT

📄 License
This project is open-source and free to use for educational purposes.

👨‍💻 Author
Akinsanya Oluwaferanmi Joshua
GitHub: @feraj-baller

