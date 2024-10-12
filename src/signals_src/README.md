# Signal Demo Project

This project demonstrates the behavior of Django signals in response to three key questions:

1. Are Django signals executed synchronously or asynchronously?
2. Do Django signals run in the same thread as the caller?
3. Do Django signals run in the same transaction as the caller?


Project Setup


1. Clone the Project:

git clone https://github.com/febinaadhi/django_signals.git
cd signal_demo

2. Create and Activate a Virtual Environment:

      For Windows:
      python -m venv venv
      venv\Scripts\activate

      For macOS/Linux:
      python3 -m venv venv
      source venv/bin/activate

3. Install the Dependencies:

      pip install -r requirements.txt

4. Set Up the Database:

      python manage.py makemigrations
      python manage.py migrate

5. Create a Superuser (Optional):

      python manage.py createsuperuser

6. Run the Development Server:

      python manage.py runserver

7. Accessing the Admin Interface:

      http://127.0.0.1:8000/admin/

8. Test the Signals:

   Two methods

Method 1: Using the Django Admin Interface

          Create a new User via the Django admin interface.
          going to http://127.0.0.1:8000/admin/

Method 2: Using the Django Shell
          
          Use the Django shell to create a user:
          python manage.py shell

          from django.contrib.auth.models import User
          user = User.objects.create(username='test_user', password='testpassword')




NOTE:

Synchronous vs Asynchronous: Signals are executed synchronously.
Thread Execution: Signals run in the same thread as the caller.
Database Transactions: Signals run in the same transaction as the caller.

When you create or update a User in the Django admin, 
the signals will be triggered, and you will see the output in your terminal, 
including whether the signals run synchronously, in the same thread, and in the same transaction.
