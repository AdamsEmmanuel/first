Designing a friend request system is a classic exercise in handling **relational data** and **state management**. To make it feel like Facebook, you need to handle three distinct phases: the request, the pending state, and the final friendship.

---

### 1. The Data Model
In a relational database (like PostgreSQL), you shouldn't just have a list of friends in a text column. Instead, use a **Join Table** (often called `Friendships` or `Relationships`).

**Core Table Structure:**
*   **requester_id:** (Foreign Key to Users) The person who sent the invite.
*   **addressee_id:** (Foreign Key to Users) The person receiving the invite.
*   **status:** An ENUM or Integer representing the state (e.g., `0: Pending`, `1: Accepted`, `2: Declined`, `3: Blocked`).
*   **created_at / updated_at:** For sorting the "Recently Added" or "New Requests" lists.



---

### 2. The Logic Flow

#### Phase A: Sending the Request
When User A clicks "Add Friend" on User B's profile:
1.  **Check for existing relationship:** Ensure there isn't already a record where A -> B or B -> A.
2.  **Validation:** Ensure A is not B (you can't friend yourself) and that A hasn't been blocked by B.
3.  **Insert Record:** Create a row with `status: 'Pending'`.

#### Phase B: The Receiver's View
User B checks their notifications:
*   **Query:** `SELECT * FROM Friendships WHERE addressee_id = B_ID AND status = 'Pending'`.
*   **Action:** User B can choose to **Accept** or **Decline**.

#### Phase C: Accepting the Request
If User B clicks "Accept":
1.  **Update Record:** Change the `status` from `Pending` to `Accepted`.
2.  **Symmetry:** Because friendship is mutual, your queries should now account for both directions. To find all of User A's friends:
    $$Friends = \{x \mid (requester = A \land addressee = x \land status = 'Accepted') \lor (requester = x \land addressee = A \land status = 'Accepted')\}$$

---

### 3. Key Features to Mimic Facebook

*   **The "Cancel Request" Button:** If User A changes their mind before B responds, simply delete the row.
*   **The "Follow" vs "Friend" Distinction:** Facebook allows you to follow someone without being friends. You might need a separate `Followers` table if you want to separate the social graph from the newsfeed logic.
*   **Mutual Friends:** To calculate this, you find the intersection of the friend sets for User A and User B.
    *   *SQL Tip:* Join the friendship table on itself where the `addressee_id` matches.

### 4. Scalability Considerations
As your app grows, querying a massive join table for every page load gets slow.
*   **Caching:** Store a list of "Accepted Friend IDs" in a cache (like Redis) for each user.
*   **Denormalization:** Some systems store a redundant `friend_count` on the `Users` table to avoid running a `COUNT(*)` query every time a profile is viewed.

Are you building this using a specific stack (like MERN or Django), or are you more focused on the database architecture right now?








Building a health-tech platform in Nigeria requires a delicate balance between a smooth user experience (UX) and strict regulatory compliance (MDCN and NDPR). Since your API will serve as the backbone, the user flows must ensure that data integrity, professional verification, and patient safety are baked into every "call."

Here is a high-level user flow designed for your Nutrition and Therapy Management platform.

---

## 1. Practitioner/Specialist Flow

The goal for the practitioner is **verification** and **onboarding**. Nigeria's MDCN (Medical and Dental Council of Nigeria) guidelines now require strict verification of licenses for digital health.

1. **Sign Up & Profile Creation:**
* Enter basic details (Email, Phone, Location).
* **Verification Upload:** National ID (NIN) + Professional License (MDCN/Nutritionist certification).
* **Niche Selection:** Define specialty (e.g., Clinical Nutrition, Mental Health Therapy, Pediatric Nutrition).


2. **Verification Queue (Admin Side):**
* API triggers a background check or admin review of credentials.
* Practitioner remains in "Pending" status (can't accept patients yet).


3. **Availability & Service Setup:**
* Set working hours (Calendar Sync).
* Define service tiers (e.g., 30-min Consultation, 4-week Meal Plan, Weekly Therapy).
* Set pricing in NGN (Nigerian Naira) or USD (Global).


4. **Dashboard Access:**
* Receive "Verified" badge.
* View patient requests and upcoming appointments.



---

## 2. Patient/User Flow

The goal for the patient is **discovery** and **accessibility**.

1. **Search & Discovery:**
* Filter by specialty, language (e.g., Yoruba, Igbo, Hausa), or location.
* View practitioner profiles, ratings, and peer-reviewed success stories.


2. **Onboarding (Health Profile):**
* **Pre-Assessment:** Input BMI, current symptoms, allergies, or mental health history.
* *Note:* Under Nigerian law, explicit **Informed Consent** must be captured here before any data is stored.


3. **Booking & Payment:**
* Select an available slot.
* **Payment Gateway:** Integrated payment (e.g., Paystack or Flutterwave) to handle local and international transactions.


4. **Consultation & Management:**
* **Session:** Secure Video/Audio/Chat within the platform.
* **Post-Session:** Receive specialized meal plans, therapy notes, or prescriptions.


5. **Follow-up & Monitoring:**
* Log daily nutrition (Food Diary) or mood for the specialist to review in real-time.



---

## 3. The API Integration Architecture

Since you are building an **API-first** platform, your endpoints should be structured to handle these distinct flows:

| Category | Key API Endpoints | Purpose |
| --- | --- | --- |
| **Identity** | `/auth/register`, `/auth/verify-license` | Handles onboarding and MDCN/NIN validation. |
| **Directory** | `/specialists/search`, `/specialists/{id}/slots` | Fetches available practitioners based on filters. |
| **Health Data** | `/records/upload`, `/records/sharing/consent` | Securely stores EMR (Electronic Medical Records). |
| **Engagement** | `/consultations/start`, `/plans/assign` | Manages the actual therapy/nutrition delivery. |
| **Finance** | `/payments/initialize`, `/payouts/practitioner` | Handles the freelance marketplace splits/escrow. |

---

## 4. Critical Compliance for Nigeria (2026)

* **Data Residency:** The Nigeria Data Protection Act (NDPA) prefers health data to be stored on servers within Nigeria or in jurisdictions with equivalent protection.
* **e-Pharmacy Integration:** If your nutritionists recommend supplements, you must now integrate with the **National Electronic Pharmacy Platform (NEPP)** if you intend to fulfill those orders through the app.
* **Professional Indemnity:** Ensure your practitioners have valid insurance; your platform should have a field to capture and track the expiry of their indemnity cover.

> **Pro-Tip:** For the freelance aspect, implement an **Escrow System**. The patient’s payment should be held by the platform and only released to the practitioner after the consultation or milestone (e.g., 1st week of meal plan) is completed to ensure quality control.

Would you like me to dive deeper into the specific database schema needed for the Patient-Practitioner relationship?






















To design the logic for this "Send Request" button, we need to move beyond a simple message and create a **State Machine**. This ensures that the 5-minute timer is enforced and that both the Patient and the Specialist are kept in sync.

Here is the breakdown of the logic, the backend flow, and the Python implementation strategy.

---

### 1. The Logical Flow (The "Happy Path")

1. **Trigger:** Patient clicks "Send Request."
2. **Validation:** System checks if the Patient has active `Consent` and if the Specialist's `Slot` is still technically available.
3. **State Change:** An `Appointment` record is created with a status of `PENDING`.
4. **Timer Initialization:** A 5-minute countdown starts on the server.
5. **Notification:** The `Notification` object sends a push/email to the Specialist.
6. **Resolution:**
* **If Specialist Accepts:** Status changes to `CONFIRMED`.
* **If Specialist Rejects:** Status changes to `REJECTED`.
* **If 5 Minutes Pass:** Status changes to `EXPIRED` (Slot released).



---

### 2. Backend Logic Design (Python/Pseudo-code)

Since you are using Python, you would likely use a task queue like **Celery** or a simple background thread to handle the 5-minute expiry.

#### **The API Endpoint**

`POST /api/v1/appointments/request`

```python
import datetime

def handle_request_button(patient_id, specialist_id, slot_id):
    # 1. Create the Appointment record
    appointment = Appointment.create(
        patient_id=patient_id,
        specialist_id=specialist_id,
        slot_id=slot_id,
        status="PENDING",
        request_time=datetime.now()
    )

    # 2. Trigger the Notification object
    notification = Notification(
        recipient_id=specialist_id,
        message=f"New request from Patient {patient_id}. You have 5 minutes to confirm.",
        priority="URGENT"
    )
    notification.send()

    # 3. Start the 5-minute "Kill Switch"
    # In Python, we schedule a background task to check this 5 mins later
    schedule_expiry_check.apply_async(args=[appointment.id], countdown=300)

    return {"message": "Request sent. Waiting for specialist confirmation.", "timeout": "300s"}

```

#### **The Expiry Task**

```python
def schedule_expiry_check(appointment_id):
    appt = Appointment.get(appointment_id)
    
    if appt.status == "PENDING":
        appt.status = "EXPIRED"
        appt.save()
        
        # Notify the patient that the specialist didn't respond in time
        Notification.send(
            recipient_id=appt.patient_id,
            message="The request has expired. Please select another slot or specialist."
        )
        # Audit the expiry
        AuditLog.create(action="APPOINTMENT_EXPIRED", resource_id=appointment_id)

```

---

### 3. Database Updates

To support this logic, your `Appointment` or `TherapySession` table needs these specific columns:

* `status`: (Enum: PENDING, CONFIRMED, REJECTED, EXPIRED).
* `expires_at`: A timestamp set to `current_time + 5 minutes`.

---

### 4. Frontend UI Logic (The Patient's View)

When the button is pushed, the UI should change to prevent "double-clicking":

1. **Disable Button:** Gray out the "Send Request" button.
2. **Visual Timer:** Show a 5-minute countdown clock.
3. **Polling/WebSockets:** The frontend should "listen" for a status change.
* If the backend updates the status to `CONFIRMED`, the UI shows a green checkmark.
* If the status hits `EXPIRED`, the UI alerts the user and refreshes the catalog.



---

### 5. Specialist Logic (The Confirmation)

The Specialist’s notification should lead to two buttons: **[Accept]** or **[Decline]**.

* **Accept Logic:**
* Check if `now < expires_at`.
* If yes: Update status to `CONFIRMED`, send notification to Patient, and lock the slot in the `Practitioner` schedule.
* If no: Return error "This request has already expired."



**Does this 5-minute "Kill Switch" logic fit your system requirements, or do you want to adjust the time based on the specific type of therapy service?**