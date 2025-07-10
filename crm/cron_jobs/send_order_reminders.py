#!/usr/bin/env python3

import datetime
import logging
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# ===> setup <===
log_file = "/tmp/order_reminders_log"
logging.basicConfig(filename=log_file, level=logging.INFO)

# ===> 7 days ago <===
today = datetime.datetime.now()
seven_days_ago = (today - datetime.timedelta(days=7)).isoformat()

# ===> setup GraphQl Transport <===
transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=False,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

# ===> Define graphql Query <===
query = gql(
    """
    query {
        allOrders(orderBy: "-orderDate") {
            edges {
                node {
                    id
                    orderDate
                    customer {
                        email
                    }
                }
            }
        }
    }
    """
)

# ===> Run Query and filter <===
try:
    result = client.execute(query)
    orders = result['allOrder']['edges']

    for order in orders:
        order_node = order['node']
        order_date = order_node['orderDate']
        customer_email = order_node['customer']['email']

        # Check if order is within last 7 days
        if order_date > seven_days_ago:
            log_message = f"[{today}] order ID: {order_node[id]} - Email: {customer_email}"
            logging.info(log_message)

    print("Orders reminder processed")

except Exception as e:
    logging.error(f"[{today}] ERROR: (str(e))")
    print("An error occured ehile processing order reminder")