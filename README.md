
# 🏀 Django Sports Stats Application 🏆

Welcome to the **Django Sports Stats Application**! 🎉 This web application allows coaches to register, add players, track their statistics, and manage images and videos for each player. Coaches can also view, edit, and print player information with ease. 🌟

The app utilizes AWS for database storage and S3 buckets for images and videos, ensuring smooth integration and scalability. 🚀 The application is deployed and hosted in a production environment using **OnRender**.

---

## 🌟 Features

- **Trainer Registration** 👨‍🏫: Coaches can register and log in to manage players.
- **Add and Edit Players** 📝: Coaches can add new players, track stats, upload images and videos.
- **Player Dashboard** 🖼️: All player data (stats, images, and videos) is displayed on the main screen.
- **Print Data** 🖨️: The ability to print player information in a printer-friendly format.
- **AWS Database with Supabase** 🌐: Utilizes AWS and Supabase for database management.
- **AWS S3 Bucket for Media** 📦: Stores player images and videos securely in an S3 bucket.
- **Production Hosting via OnRender** 🌍: The app is deployed and live on OnRender.

---

## 🛠️ Technologies

- **Django**: The web framework that powers the backend of this application.
- **Supabase (AWS)**: Manages the database using AWS through Supabase.
- **AWS S3**: Stores player images and video content.
- **OnRender**: Hosts the application in a production environment.

---

## 📥 Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Stevanovic-Milos/Players
   cd Players
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsactivate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Local Database** (if not using Supabase):

   Modify `settings.py` to match your local database configuration:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server**:

   ```bash
   python manage.py runserver
   ```

---

## 🔧 AWS S3 Configuration

1. **Create an AWS Account** 🌐: Sign up if you don't already have one.
2. **Create an S3 Bucket** 🗃️: Set up an S3 bucket to store player images and videos.
3. **Configure Settings in `settings.py`**:
4. **Install Required Packages**:

   ```bash
   pip install django-storages boto3
   ```

---

## 🚀 Deployment on OnRender

To deploy your application on OnRender, follow these steps:

1. **Create an OnRender Account** 🌍: Sign up and log in.
2. **Create a New Project** 💻: Link it to your GitHub repository.
3. **Configure Environment Variables** 🔑: Set up the necessary environment variables like AWS credentials and database URL in the OnRender dashboard.
4. **Automatic Deployment** 🔄: OnRender will automatically detect your Django application and deploy it to production.
5. **Setup Envirnoment variables** 📥


   ```python
   AWS_ACCESS_KEY_ID = 'your-access-key-id'
   AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
   AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
   ```


---

## 🖨️ Print-Friendly View

The app includes functionality to print player data in a clean, organized table format. 📑

To print, just click the **Print** button located at the bottom of the player table. 🖱️

---

## 📱 Mobile Responsiveness

The application is fully responsive on mobile devices. 📱 Tables, images, and media scale accordingly for a smooth user experience.

---

## 📅 Future Features

- **Player Search** 🔍: Add search functionality for faster player lookup.
- **Advanced Stats** 📊: Track more detailed player performance metrics.
- **Email Notifications** 📧: Notify coaches about important updates or actions.

---

## 📧 Contact

- Email: [stevanovicmilos0003@gmail.com.com] 📬
- Portfolio: [Stevanovic_Portfolio](https://stevanovicm.com) 🌐
