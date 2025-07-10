#!/bin/bash

# Add a timestamp
echo "[$(date)] Starting Customer cleanup..." >> /tmp/customer_cleanup_log.txt

# Using django shell to delete inactive customer
deleted_count=$(python manage.py shell << EOF
from datetime import datetime, timedelta
from crm.models import Customer
from django.utils.timezone import now

one_year_ago = now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__isnull=True, created_at__lt=one_year_ago).distinct()
count = inactive_customers.count()
inactive_customers.delete()
print(count)
EOF
)

# Log number of customer deleted
echo "[$(date)] Deleted $deleted_count inactive customers." >> /tmp/customer_cleanup_log.txt