import json
from datetime import datetime, timedelta
from app.db.database import db

def reset_database():
    """Drop and re-create tables, then seed fresh sample operational data."""
    db.init_db()
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM order_items")
    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM support_tickets")
    cursor.execute("DELETE FROM workflow_events")
    cursor.execute("DELETE FROM audit_traces")
    cursor.execute("DELETE FROM conversations")
    conn.commit()
    conn.close()
    seed_database(force=True)

def seed_database(force: bool = False):
    """Seed sample operational data into the SQLite database."""
    db.init_db()
    conn = db.get_connection()
    cursor = conn.cursor()

    # Check if orders are already populated
    if not force:
        cursor.execute("SELECT COUNT(*) FROM orders")
        if cursor.fetchone()[0] > 0:
            conn.close()
            return

    now = datetime.now()

    sample_orders = [
        {
            "order_id": "ORD-1001",
            "customer_name": "Rahul Sharma",
            "customer_phone": "+91-98765-43101",
            "total_amount": 34.50,
            "status": "Delivered",
            "created_at": (now - timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": "Delivered at 12:45 PM",
            "delivery_address": "Flat 402, Lotus Residency, Andheri West, Mumbai",
            "driver_name": "Suresh Kumar",
            "driver_phone": "+91-98765-43188",
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-01", "name": "Classic Cheeseburger", "quantity": 2, "price": 12.00, "special_instructions": "No onions"},
                {"item_id": "ITM-02", "name": "Crispy French Fries", "quantity": 1, "price": 4.50, "special_instructions": "Extra crispy"},
                {"item_id": "ITM-03", "name": "Craft Root Beer", "quantity": 2, "price": 3.00, "special_instructions": None}
            ]
        },
        {
            "order_id": "ORD-1002",
            "customer_name": "Priya Patel",
            "customer_phone": "+91-98765-43102",
            "total_amount": 42.00,
            "status": "Out for Delivery",
            "created_at": (now - timedelta(minutes=40)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": (now + timedelta(minutes=15)).strftime("%I:%M %p"),
            "delivery_address": "12, Satellite Road, Ahmedabad",
            "driver_name": "Vikram Singh",
            "driver_phone": "+91-98765-43192",
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-04", "name": "Chicken Alfredo Pasta", "quantity": 2, "price": 18.00, "special_instructions": "Extra parmesan"},
                {"item_id": "ITM-05", "name": "Garlic Breadsticks", "quantity": 1, "price": 6.00, "special_instructions": None}
            ]
        },
        {
            "order_id": "ORD-1003",
            "customer_name": "Amit Verma",
            "customer_phone": "+91-98765-43103",
            "total_amount": 28.00,
            "status": "Preparing",
            "created_at": (now - timedelta(minutes=20)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": (now + timedelta(minutes=30)).strftime("%I:%M %p"),
            "delivery_address": "B-27, Sector 62, Noida",
            "driver_name": "Unassigned (Kitchen in Progress)",
            "driver_phone": None,
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-06", "name": "Margherita Pizza (12 inch)", "quantity": 1, "price": 18.00, "special_instructions": "Thin crust"},
                {"item_id": "ITM-07", "name": "Caesar Salad", "quantity": 1, "price": 10.00, "special_instructions": "Dressing on the side"}
            ]
        },
        {
            "order_id": "ORD-1004",
            "customer_name": "Rohan Mehta",
            "customer_phone": "+91-98765-43104",
            "total_amount": 19.50,
            "status": "Confirmed",
            "created_at": (now - timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": (now + timedelta(minutes=45)).strftime("%I:%M %p"),
            "delivery_address": "Apt 3B, Green Park Towers, Pune",
            "driver_name": None,
            "driver_phone": None,
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-08", "name": "Spicy Buffalo Wings (10 pcs)", "quantity": 1, "price": 14.50, "special_instructions": "Ranch dip"},
                {"item_id": "ITM-09", "name": "Diet Coke Can", "quantity": 2, "price": 2.50, "special_instructions": None}
            ]
        },
        {
            # Highlighted in assessment scenario 1: "Where is my order ORD-1005?"
            "order_id": "ORD-1005",
            "customer_name": "Ananya Iyer",
            "customer_phone": "+91-98765-43105",
            "total_amount": 56.25,
            "status": "Preparing",
            "created_at": (now - timedelta(minutes=18)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": (now + timedelta(minutes=22)).strftime("%I:%M %p"),
            "delivery_address": "Suite 12, Brigade Gateway, Rajajinagar, Bengaluru",
            "driver_name": "Arjun Nair (Pending pickup)",
            "driver_phone": "+91-98765-43144",
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-10", "name": "Truffle Mushroom Risotto", "quantity": 1, "price": 24.00, "special_instructions": "Gluten-free"},
                {"item_id": "ITM-11", "name": "Grilled Salmon Fillet", "quantity": 1, "price": 26.00, "special_instructions": "Medium well"},
                {"item_id": "ITM-12", "name": "Sparkling Mineral Water", "quantity": 1, "price": 6.25, "special_instructions": "With lemon slice"}
            ]
        },
        {
            "order_id": "ORD-1006",
            "customer_name": "Karthik Reddy",
            "customer_phone": "+91-98765-43106",
            "total_amount": 22.00,
            "status": "Cancelled",
            "created_at": (now - timedelta(hours=1, minutes=15)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": None,
            "delivery_address": "88, Banjara Hills Road No. 3, Hyderabad",
            "driver_name": None,
            "driver_phone": None,
            "cancellation_reason": "Customer cancelled within 60 seconds of placing order before kitchen confirmation. Refund of $22.00 processed.",
            "items": [
                {"item_id": "ITM-13", "name": "Pepperoni Pizza (12 inch)", "quantity": 1, "price": 19.00, "special_instructions": None},
                {"item_id": "ITM-03", "name": "Craft Root Beer", "quantity": 1, "price": 3.00, "special_instructions": None}
            ]
        },
        {
            "order_id": "ORD-1007",
            "customer_name": "Sneha Kulkarni",
            "customer_phone": "+91-98765-43107",
            "total_amount": 16.50,
            "status": "Placed",
            "created_at": (now - timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": (now + timedelta(minutes=40)).strftime("%I:%M %p"),
            "delivery_address": "15, Shivaji Nagar, Nagpur",
            "driver_name": None,
            "driver_phone": None,
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-14", "name": "Vegetarian Pad Thai", "quantity": 1, "price": 14.00, "special_instructions": "Mild spicy"},
                {"item_id": "ITM-09", "name": "Diet Coke Can", "quantity": 1, "price": 2.50, "special_instructions": None}
            ]
        },

        # ------------------------- Additional guests -------------------------
        {
            "order_id": "ORD-1008",
            "customer_name": "Aditya Joshi",
            "customer_phone": "+91-98765-43108",
            "total_amount": 31.50,
            "status": "Out for Delivery",
            "created_at": (now - timedelta(minutes=35)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": (now + timedelta(minutes=10)).strftime("%I:%M %p"),
            "delivery_address": "Room 1204, Dragonstone Tower, Connaught Place, New Delhi",
            "driver_name": "Manoj Yadav",
            "driver_phone": "+91-98765-43208",
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-15", "name": "Butter Chicken", "quantity": 1, "price": 16.00, "special_instructions": "Medium spicy"},
                {"item_id": "ITM-16", "name": "Garlic Naan", "quantity": 3, "price": 2.50, "special_instructions": None},
                {"item_id": "ITM-17", "name": "Mango Lassi", "quantity": 2, "price": 4.00, "special_instructions": "Less sugar"}
            ]
        },
        {
            "order_id": "ORD-1009",
            "customer_name": "Meera Nair",
            "customer_phone": "+91-98765-43109",
            "total_amount": 25.00,
            "status": "Delivered",
            "created_at": (now - timedelta(hours=2, minutes=30)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": "Delivered at 01:10 PM",
            "delivery_address": "Villa 7, Marine Drive, Kochi",
            "driver_name": "Sajeev Pillai",
            "driver_phone": "+91-98765-43209",
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-18", "name": "Masala Dosa", "quantity": 2, "price": 9.00, "special_instructions": "Extra chutney"},
                {"item_id": "ITM-19", "name": "Filter Coffee", "quantity": 2, "price": 3.50, "special_instructions": None}
            ]
        },
        {
            "order_id": "ORD-1010",
            "customer_name": "Imran Khan",
            "customer_phone": "+91-98765-43110",
            "total_amount": 48.50,
            "status": "Preparing",
            "created_at": (now - timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": (now + timedelta(minutes=28)).strftime("%I:%M %p"),
            "delivery_address": "21, Tolichowki Main Road, Hyderabad",
            "driver_name": "Farhan Ali (Pending pickup)",
            "driver_phone": "+91-98765-43210",
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-20", "name": "Hyderabadi Chicken Biryani", "quantity": 2, "price": 17.00, "special_instructions": "Extra raita"},
                {"item_id": "ITM-21", "name": "Mirchi Ka Salan", "quantity": 1, "price": 5.50, "special_instructions": None},
                {"item_id": "ITM-22", "name": "Gulab Jamun", "quantity": 2, "price": 4.50, "special_instructions": "Served warm"}
            ]
        },
        {
            "order_id": "ORD-1011",
            "customer_name": "Kavya Menon",
            "customer_phone": "+91-98765-43111",
            "total_amount": 23.00,
            "status": "Placed",
            "created_at": (now - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": (now + timedelta(minutes=42)).strftime("%I:%M %p"),
            "delivery_address": "Flat 5C, Lake View Apartments, Thiruvananthapuram",
            "driver_name": None,
            "driver_phone": None,
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-23", "name": "Paneer Butter Masala", "quantity": 1, "price": 15.00, "special_instructions": "Jain preparation"},
                {"item_id": "ITM-24", "name": "Jeera Rice", "quantity": 1, "price": 5.00, "special_instructions": None},
                {"item_id": "ITM-25", "name": "Masala Chai", "quantity": 1, "price": 3.00, "special_instructions": "Less sugar"}
            ]
        },
        {
            "order_id": "ORD-1012",
            "customer_name": "Harpreet Singh",
            "customer_phone": "+91-98765-43112",
            "total_amount": 30.00,
            "status": "Confirmed",
            "created_at": (now - timedelta(minutes=8)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": (now + timedelta(minutes=38)).strftime("%I:%M %p"),
            "delivery_address": "SCO 45, Sector 17, Chandigarh",
            "driver_name": None,
            "driver_phone": None,
            "cancellation_reason": None,
            "items": [
                {"item_id": "ITM-26", "name": "Chole Bhature", "quantity": 2, "price": 11.00, "special_instructions": "Extra pickle"},
                {"item_id": "ITM-27", "name": "Sweet Lassi", "quantity": 2, "price": 4.00, "special_instructions": None}
            ]
        },
        {
            "order_id": "ORD-1013",
            "customer_name": "Debashree Das",
            "customer_phone": "+91-98765-43113",
            "total_amount": 23.00,
            "status": "Cancelled",
            "created_at": (now - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
            "estimated_delivery_time": None,
            "delivery_address": "Plot 18, Saheed Nagar, Bhubaneswar",
            "driver_name": None,
            "driver_phone": None,
            "cancellation_reason": "Customer cancelled before kitchen confirmation. Refund of $23.00 processed.",
            "items": [
                {"item_id": "ITM-28", "name": "Veg Thali", "quantity": 1, "price": 18.00, "special_instructions": None},
                {"item_id": "ITM-29", "name": "Rasgulla", "quantity": 1, "price": 5.00, "special_instructions": None}
            ]
        }
    ]

    for order in sample_orders:
        cursor.execute("""
            INSERT OR REPLACE INTO orders
            (order_id, customer_name, customer_phone, total_amount, status, created_at, estimated_delivery_time, delivery_address, driver_name, driver_phone, cancellation_reason)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            order["order_id"],
            order["customer_name"],
            order["customer_phone"],
            order["total_amount"],
            order["status"],
            order["created_at"],
            order["estimated_delivery_time"],
            order["delivery_address"],
            order["driver_name"],
            order["driver_phone"],
            order["cancellation_reason"]
        ))

        for item in order["items"]:
            cursor.execute("""
                INSERT INTO order_items (order_id, item_id, name, quantity, price, special_instructions)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                order["order_id"],
                item["item_id"],
                item["name"],
                item["quantity"],
                item["price"],
                item["special_instructions"]
            ))

    # Sample Initial Support Ticket
    cursor.execute("""
        INSERT OR REPLACE INTO support_tickets
        (ticket_id, order_id, customer_name, customer_contact, issue_category, priority, description, sentiment, status, created_at, resolution_notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "TCK-9001",
        "ORD-1001",
        "Rahul Sharma",
        "+91-98765-43101",
        "Order",
        "Low",
        "Customer asked for nutritional information regarding the burger buns.",
        "Neutral",
        "Resolved",
        (now - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
        "Nutritional sheet sent via email."
    ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_database()
    print("Database initialized and seeded successfully.")