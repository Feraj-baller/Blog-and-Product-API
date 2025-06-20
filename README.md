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

2. **Set up a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. **Test with Postman or any REST client**

---

## 🧾 Sample JSON (POST /blogs/)

```json
{
  "title": "My First Blog",
  "author": "Feranmi",
  "published_date": "2025-06-20",
  "description": "This is an article about Django and REST APIs."
}
```

---

## 🧯 Error Handling

* Returns `400` for missing/incomplete fields
* Returns `404` for non-existent resources
* Uses Django REST Framework’s status codes for clarity

---

## 🧠 Author

**Akinsanya Oluwaferanmi Joshua**
🖥 GitHub: [@feraj-baller](https://github.com/feraj-baller)
📧 Email: [feranmiakinsanya6@gmail.com](mailto:feranmiakinsanya6@gmail.com)

---

## 🪄 Future Improvements

* Add DRF serializers for better validation
* Implement token-based authentication
* Add pagination and filtering
* Docker support and CI/CD integration

---

## 🪪 License

This project is open-source and available for educational and personal use.

```

---

Would you like me to generate the `requirements.txt` file for this project too?
```
