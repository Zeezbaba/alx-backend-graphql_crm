# 📊 CRM Celery Task Setup

This guide helps you set up **Celery** with **Django** and **Redis** for scheduling weekly CRM reports.

---

## 📦 Installation

### 1. Install Redis

```bash
sudo apt update && sudo apt install redis
2. Add Dependencies
Update your requirements.txt file to include:

nginx
Copy
Edit
celery
django-celery-beat
redis
Then install them:

bash
Copy
Edit
pip install -r requirements.txt
3. Run Django Migrations
bash
Copy
Edit
python manage.py migrate
🚀 Running Celery
Start the Redis Server
bash
Copy
Edit
redis-server
Start the Celery Worker
bash
Copy
Edit
celery -A crm worker -l info
Start the Celery Beat Scheduler
bash
Copy
Edit
celery -A crm beat -l info
📝 Logs
The weekly CRM report will be saved to:

bash
Copy
Edit
/tmp/crm_report_log.txt