# djangocelery
This is a repo for practicing Background tasks in Django using Celery

I create a django app to send emails and populate a database after a registration form is filled up.

Then, the two tasks are offloaded to Celery to improve web app loading speed.

# requirements
- Message Broker: Redis or RabitMQ
- wkhtmltopdf

