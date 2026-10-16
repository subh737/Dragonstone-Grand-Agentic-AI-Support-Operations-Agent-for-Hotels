"""Knowledge base documents for the Dragonstone Grand Support & Operations Agent.

HOW TO EXTEND:
  - Add a new dict to KB_DOCUMENTS (unique doc_id, title, category, keywords, content).
  - Restart the server; the vector index is built from this list at startup.
NOTE: All addresses, prices, phone numbers and times below are SAMPLE values. Replace with real ones.
"""

KB_DOCUMENTS = [
    # ------------------------------------------------------------------
    # Existing documents (doc_ids unchanged so tests keep passing)
    # ------------------------------------------------------------------
    {
        "doc_id": "POL-CANCEL-01",
        "title": "Order Cancellation Policy",
        "category": "Cancellation & Refunds",
        "keywords": ["cancel", "cancellation", "order cancel", "stop order", "abort"],
        "content": (
            "Order Cancellation Policy:\n"
            "1. Before Kitchen Acceptance: Guests may cancel their order free of charge with an immediate "
            "100% refund to the original payment method if the order is still in 'Placed' status and has not yet "
            "been accepted by the kitchen.\n"
            "2. After the Kitchen Accepts or Starts Preparing: Once the kitchen accepts the order and "
            "preparation begins ('Confirmed' or 'Preparing' status), orders CANNOT be cancelled for a full refund "
            "because perishable ingredients and kitchen labor are already committed. In exceptional cases, a partial credit "
            "(up to 50%) may be reviewed by guest support.\n"
            "3. Out for Delivery or Delivered: Orders that are 'Out for Delivery' or 'Delivered' cannot be cancelled "
            "under any circumstances."
        )
    },
    {
        "doc_id": "POL-REFUND-02",
        "title": "Refund Policy & Payment Deduction Issues",
        "category": "Cancellation & Refunds",
        "keywords": ["refund", "deducted", "payment failed", "charged", "double charge", "money taken"],
        "content": (
            "Refund and Payment Failure Policy:\n"
            "1. Payment Deducted but Order Failed: If funds were deducted from your bank or card but the order failed "
            "to generate an order confirmation ID, the banking gateway automatically voids the pre-authorization within "
            "24 hours. If it does not reverse automatically, guest support immediately escalates a high-priority "
            "ticket to the Finance team. Refunds typically reflect in 3 to 5 business days.\n"
            "2. Missing or Damaged Items: If an order arrives with missing items or damaged packaging, guests must "
            "report it within 2 hours. A full refund for the affected item or an instant replacement credit code will be issued.\n"
            "3. Incorrect Food Delivered: If the wrong dish is delivered, the guest receives an immediate 100% refund "
            "or an express re-delivery at zero cost."
        )
    },
    {
        "doc_id": "POL-DELIVERY-03",
        "title": "Delivery Areas, Fees & ETA Guarantees",
        "category": "Delivery Operations",
        "keywords": ["delivery time", "eta", "delivery fee", "delivery area", "late delivery", "radius", "how long"],
        "content": (
            "Delivery Operations & Guidelines:\n"
            "1. Standard Delivery ETA: Delivery usually takes between 30 to 45 minutes from order confirmation, "
            "depending on dish preparation time, kitchen queue, and local traffic.\n"
            "2. Delivery Zone: We deliver within an 8-mile radius of Dragonstone Grand.\n"
            "3. Delivery Charges: Flat delivery fee is $3.99. Delivery is FREE on orders totaling $35.00 or higher "
            "before taxes.\n"
            "4. Late Delivery Guarantee: If an order arrives more than 25 minutes past the quoted estimated delivery time "
            "(due to non-weather reasons), the guest is eligible for a $10 courtesy credit towards their next order."
        )
    },
    {
        "doc_id": "POL-HOURS-04",
        "title": "Operating Hours & Location",
        "category": "General Policy",
        "keywords": ["operating hours", "open time", "closing time", "location", "address", "dine-in hours"],
        "content": (
            "Operating Hours & Hotel Information:\n"
            "- Monday to Thursday: 10:30 AM to 10:00 PM\n"
            "- Friday & Saturday: 10:30 AM to 11:30 PM\n"
            "- Sunday: 11:00 AM to 9:30 PM\n"
            "- Address: 742 Dragonstone Boulevard, Metropolis.\n"
            "- Dine-in reservations must be made at least 2 hours in advance via the mobile app or web portal.\n"
            "- Front Desk & Guest Support: open 24 hours a day, 7 days a week.\n"
            "- Contact Telephone: +1-800-555-DINE (3463)."
        )
    },
    {
        "doc_id": "POL-DIET-05",
        "title": "Dietary Restrictions, Allergens & Customizations",
        "category": "Food & Safety",
        "keywords": ["allergy", "allergen", "gluten", "vegan", "vegetarian", "nuts", "halal", "dairy free"],
        "content": (
            "Allergen & Dietary Information:\n"
            "1. Menu Badges: Menu items clearly indicate Vegan (VG), Vegetarian (V), Gluten-Free (GF), and Halal (H) options.\n"
            "2. Allergen Notice: Our kitchens handle peanuts, tree nuts, dairy, wheat, soy, eggs, and shellfish. "
            "While strict sanitation protocols are maintained, cross-contact may occur. Guests with severe allergies "
            "must specify allergy details in the order notes and contact the Executive Chef's office directly.\n"
            "3. Customizations: Kitchen staff can accommodate basic ingredient omissions (e.g., 'no onions', 'mild spicy') "
            "when specified in item instructions during order placement.\n"
            "4. Special Diets: Kosher and fully dairy-free meals are available with 24 hours notice."
        )
    },
    {
        "doc_id": "POL-TIPS-06",
        "title": "Tipping & Payment Methods",
        "category": "Payment Operations",
        "keywords": ["payment methods", "credit card", "apple pay", "tip", "driver tip", "cash"],
        "content": (
            "Payment & Courier Tipping:\n"
            "1. Accepted Payment Methods: Visa, MasterCard, American Express, Apple Pay, Google Pay, and PayPal.\n"
            "2. Courier Tipping: 100% of all driver tips added during checkout or upon delivery go directly to the driver.\n"
            "3. Cash Payments: Cash on delivery is available for orders under $50 in select delivery areas.\n"
            "4. Room Charges: In-house guests may charge dining and spa services to their room folio."
        )
    },

    # ------------------------------------------------------------------
    # New documents
    # ------------------------------------------------------------------
    {
        "doc_id": "POL-CHECKIN-07",
        "title": "Check-in, Check-out & Early/Late Arrival",
        "category": "Stay & Rooms",
        "keywords": ["check-in", "check in", "checkout", "check out", "early arrival", "late checkout", "arrival time"],
        "content": (
            "Check-in & Check-out Policy:\n"
            "1. Check-in: Standard check-in time is 3:00 PM. A valid government photo ID and the card used for booking "
            "are required at the front desk.\n"
            "2. Check-out: Standard check-out time is 11:00 AM.\n"
            "3. Early Check-in: Subject to availability from 11:00 AM at no charge; before 11:00 AM a half-night charge applies.\n"
            "4. Late Check-out: Until 2:00 PM is complimentary for Dragonstone Rewards Gold members and above; "
            "for other guests it is $30, and after 2:00 PM a full-night charge applies.\n"
            "5. Luggage Storage: Complimentary luggage storage is available before check-in and after check-out."
        )
    },
    {
        "doc_id": "POL-ROOMS-08",
        "title": "Room Types & In-Room Amenities",
        "category": "Stay & Rooms",
        "keywords": ["room types", "suite", "bed", "amenities", "view", "upgrade", "housekeeping", "towels"],
        "content": (
            "Room Types & Amenities:\n"
            "1. Room Categories: Stone Deluxe (King or Twin), Dragon Suite (separate living area), and the "
            "Dragonstone Penthouse (two bedrooms, private terrace).\n"
            "2. Standard Amenities: Smart TV, mini-bar, in-room safe, coffee machine, iron, hairdryer, and premium toiletries.\n"
            "3. Housekeeping: Daily service between 9:00 AM and 4:00 PM. Use the Do Not Disturb sign or call the front desk "
            "to skip service. Extra towels, pillows and toiletries are delivered within 15 minutes of request.\n"
            "4. Upgrades: Room upgrades are subject to availability and can be requested at check-in or via the front desk."
        )
    },
    {
        "doc_id": "POL-ROOMSERVICE-09",
        "title": "In-Room Dining & Breakfast",
        "category": "Food & Dining",
        "keywords": ["room service", "in-room dining", "breakfast", "buffet", "late night menu", "dining hours"],
        "content": (
            "In-Room Dining & Breakfast:\n"
            "1. In-Room Dining: Available 24 hours a day. Typical delivery time to your room is 30 to 40 minutes. "
            "A $5 service charge applies per in-room order.\n"
            "2. Breakfast Buffet: Served daily from 6:30 AM to 10:30 AM at Ember Hall restaurant. Complimentary for guests "
            "on bed-and-breakfast rates and for Dragonstone Rewards Platinum members; otherwise $24 per adult.\n"
            "3. Late-Night Menu: A reduced menu is available from 11:30 PM to 6:00 AM.\n"
            "4. Special Occasions: Cakes and celebration set-ups can be arranged with 24 hours notice."
        )
    },
    {
        "doc_id": "POL-WIFI-10",
        "title": "Wi-Fi, Business Centre & Meeting Rooms",
        "category": "Facilities",
        "keywords": ["wifi", "wi-fi", "internet", "password", "business centre", "printing", "meeting room"],
        "content": (
            "Wi-Fi & Business Services:\n"
            "1. Wi-Fi: Complimentary high-speed Wi-Fi throughout the hotel. Connect to 'DragonstoneGuest' and log in "
            "with your surname and room number.\n"
            "2. Premium Wi-Fi: Upgraded 500 Mbps plan available for $9.99 per day.\n"
            "3. Business Centre: Open 24 hours on the mezzanine level with complimentary printing up to 20 pages per day.\n"
            "4. Meeting Rooms: Bookable through the events desk. Capacity ranges from 8 to 120 guests."
        )
    },
    {
        "doc_id": "POL-PARKING-11",
        "title": "Parking, Valet & Airport Transfers",
        "category": "Facilities",
        "keywords": ["parking", "valet", "car", "airport", "transfer", "shuttle", "ev charging"],
        "content": (
            "Parking & Transport:\n"
            "1. Self-Parking: $18 per night, in-and-out privileges included.\n"
            "2. Valet Parking: $32 per night. Please allow 10 minutes to retrieve your vehicle.\n"
            "3. EV Charging: Four charging stations are available in the basement garage at no additional fee.\n"
            "4. Airport Shuttle: Scheduled shuttle every 30 minutes between 5:00 AM and 11:00 PM; $25 per person each way. "
            "Private car transfers can be booked 24 hours in advance."
        )
    },
    {
        "doc_id": "POL-SPA-12",
        "title": "Spa, Pool & Fitness Centre",
        "category": "Facilities",
        "keywords": ["spa", "pool", "gym", "fitness", "massage", "sauna", "wellness"],
        "content": (
            "Spa, Pool & Fitness:\n"
            "1. Fitness Centre: Open 24 hours for in-house guests with room key access.\n"
            "2. Pool & Sauna: Rooftop pool open 7:00 AM to 10:00 PM. Sauna and steam room open 8:00 AM to 9:00 PM.\n"
            "3. Obsidian Spa: Open 10:00 AM to 8:00 PM. Treatments should be booked at least 24 hours in advance; "
            "cancellations within 4 hours of the appointment are charged in full.\n"
            "4. Age Policy: Guests under 16 must be accompanied by an adult in the pool and fitness areas."
        )
    },
    {
        "doc_id": "POL-PETS-13",
        "title": "Pet Policy",
        "category": "Stay & Rooms",
        "keywords": ["pet", "pets", "dog", "cat", "service animal", "animal"],
        "content": (
            "Pet Policy:\n"
            "1. Pets Welcome: Dogs and cats up to 25 kg are welcome in designated Pet-Friendly rooms. "
            "A $50 per stay cleaning fee applies and a maximum of two pets per room.\n"
            "2. Service Animals: Registered service animals stay free of charge and are welcome in all areas of the hotel.\n"
            "3. Rules: Pets must not be left unattended in the room and must be leashed in public areas.\n"
            "4. Pet Amenities: Beds, bowls and treats are provided on request."
        )
    },
    {
        "doc_id": "POL-LOYALTY-14",
        "title": "Dragonstone Rewards Loyalty Programme",
        "category": "Loyalty & Offers",
        "keywords": ["loyalty", "rewards", "points", "member", "membership", "tier", "gold", "platinum"],
        "content": (
            "Dragonstone Rewards:\n"
            "1. Earning: Members earn 10 points per $1 spent on rooms, dining and spa. Points post within 72 hours of check-out.\n"
            "2. Tiers: Silver (0+ nights), Gold (20+ nights per year), Platinum (50+ nights per year).\n"
            "3. Benefits: Gold adds late check-out and room upgrades subject to availability; "
            "Platinum adds complimentary breakfast and lounge access.\n"
            "4. Redemption: 10,000 points equal one free night. Points expire after 24 months of inactivity."
        )
    },
    {
        "doc_id": "POL-BOOKING-15",
        "title": "Room Reservation Changes & No-Shows",
        "category": "Stay & Rooms",
        "keywords": ["reservation", "room booking", "modify booking", "no-show", "deposit", "change dates"],
        "content": (
            "Room Reservation Changes:\n"
            "1. Modifications: Guests can change dates free of charge up to 48 hours before arrival, subject to availability.\n"
            "2. Room Reservation Cancellation: Free up to 48 hours before arrival. Within 48 hours, the first night is charged.\n"
            "3. No-Shows: A no-show is charged the full first night and the rest of the reservation is released.\n"
            "4. Deposits: A deposit of one night may be taken at booking for non-flexible rates and is non-refundable."
        )
    },
    {
        "doc_id": "POL-SAFETY-16",
        "title": "Accessibility, Safety & Lost Property",
        "category": "General Policy",
        "keywords": ["accessible", "wheelchair", "lost and found", "lost property", "safe", "security", "lift", "elevator"],
        "content": (
            "Accessibility, Safety & Lost Property:\n"
            "1. Accessibility: Step-free entrances, lifts to all floors and accessible rooms with roll-in showers are available. "
            "Request accessible rooms when booking.\n"
            "2. Security: 24-hour CCTV and on-site security. Valuables can be stored in the in-room safe or the front desk safe.\n"
            "3. Lost Property: Report items to the front desk. Found items are held for 90 days and can be shipped "
            "to the guest at their expense.\n"
            "4. Emergencies: Dial 0 from any room phone to reach the front desk immediately."
        )
    },
]