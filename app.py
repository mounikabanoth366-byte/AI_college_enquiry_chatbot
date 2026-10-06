import streamlit as st
import json

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="MRECW AI College Enquiry",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# LOAD COLLEGE DATA
# --------------------------------------------------
with open("college_data.json", "r", encoding="utf-8") as file:
    college_data = json.load(file)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.hero {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    padding: 35px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
}

.card {
    background-color: white;
    padding: 22px;
    border-radius: 15px;
    margin-bottom: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    min-height: 150px;
}

.card h3 {
    color: #2563eb;
}

.chat-title {
    color: #4f46e5;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("🎓 MRECW")

st.sidebar.markdown(
    "**Malla Reddy Engineering College for Women**"
)

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Quick Information")

if st.sidebar.button("🏫 College"):
    st.session_state.quick_question = "What is the college name?"

if st.sidebar.button("📚 Courses"):
    st.session_state.quick_question = "What courses are available?"

if st.sidebar.button("📝 Admissions"):
    st.session_state.quick_question = "What is the admission process?"

if st.sidebar.button("💰 Fees"):
    st.session_state.quick_question = "What are the fees?"

if st.sidebar.button("🏠 Hostel"):
    st.session_state.quick_question = "Is hostel available?"

if st.sidebar.button("🚌 Transport"):
    st.session_state.quick_question = "Is transport available?"

if st.sidebar.button("📖 Library"):
    st.session_state.quick_question = "Is library available?"

if st.sidebar.button("📞 Contact"):
    st.session_state.quick_question = "What is the contact number?"

if st.sidebar.button("⏰ Timings"):
    st.session_state.quick_question = "What are the college timings?"

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🎓 AI College Enquiry Chatbot</h1>
    <p>Malla Reddy Engineering College for Women</p>
    <p>📍 Maisammaguda, Hyderabad, Telangana</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# COLLEGE INFORMATION CARDS
# --------------------------------------------------
st.subheader("🏫 College Information")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📚 Courses</h3>
        <p>B.Tech Programs</p>
        <p>Multiple Engineering Branches</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🏠 Hostel</h3>
        <p>Hostel Facility Available</p>
        <p>For Women Students</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🚌 Transport</h3>
        <p>College Bus Facility</p>
        <p>Available for Students</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h3>📖 Library</h3>
        <p>Library Facility</p>
        <p>Digital Learning Support</p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# CHATBOT
# --------------------------------------------------
st.markdown("---")

st.markdown(
    '<div class="chat-title">🤖 Ask the AI College Assistant</div>',
    unsafe_allow_html=True
)

st.write(
    "Ask questions about courses, admissions, fees, hostel, transport, library and more."
)

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# ANSWER FUNCTION
# --------------------------------------------------
def get_answer(question):

    question = question.lower()

    # College
    if "college" in question or "name" in question:

        college = college_data["College"]

        return (
            f"🏫 **College Name:** {college['name']}\n\n"
            f"📍 **Location:** {college['location']}"
        )

    # Courses
    elif "course" in question or "courses" in question:

        courses = college_data["Courses"]

        answer = "📚 **Available Courses:**\n\n"

        for course in courses:
            answer += f"• {course}\n"

        return answer

    # Eligibility
    elif "eligibility" in question or "eligible" in question:

        return (
            "✅ **Eligibility:**\n\n"
            + college_data["Eligibility"]["B.Tech"]
        )

    # Admissions
    elif "admission" in question or "documents" in question:

        admission = college_data["Admissions"]

        answer = (
            "📝 **Admission Process:**\n\n"
            + admission["process"]
            + "\n\n"
        )

        answer += "📄 **Required Documents:**\n"

        for document in admission["documents"]:
            answer += f"• {document}\n"

        return answer

    # Fees
    elif "fee" in question or "fees" in question:

        return (
            "💰 **B.Tech Fees:**\n\n"
            + college_data["Fees"]["B.Tech"]
        )

    # Hostel
    elif "hostel" in question:

        hostel = college_data["Hostel"]

        if hostel["available"]:

            return (
                "🏠 **Hostel:** Available\n\n"
                + hostel["details"]
            )

        return "❌ Hostel facility is not available."

    # Transport
    elif "transport" in question or "bus" in question:

        transport = college_data["Transport"]

        if transport["available"]:

            return (
                "🚌 **Transport:** Available\n\n"
                + transport["details"]
            )

        return "❌ Transport facility is not available."

    # Library
    elif "library" in question:

        library = college_data["Library"]

        if library["available"]:

            return (
                "📖 **Library:** Available\n\n"
                + library["details"]
            )

        return "❌ Library facility is not available."

    # Contact
    elif (
        "contact" in question
        or "phone" in question
        or "email" in question
        or "number" in question
    ):

        contact = college_data["Contact"]

        return (
            "📞 **Contact Information:**\n\n"
            f"**Phone:** {contact['phone']}\n\n"
            f"**Admissions:** {contact['admissions']}\n\n"
            f"**Email:** {contact['email']}\n\n"
            f"**Website:** {contact['website']}"
        )

    # Timings
    elif (
        "timing" in question
        or "timings" in question
        or "time" in question
    ):

        timings = college_data["Timings"]

        return (
            "⏰ **College Timings:**\n\n"
            f"🏫 College: {timings['college']}\n\n"
            f"🏢 Office: {timings['office']}\n\n"
            f"📖 Library: {timings['library']}"
        )

    # Greeting
    elif (
        "hello" in question
        or "hi" in question
        or "hey" in question
    ):

        return (
            "👋 Hello! Welcome to the MRECW AI College Enquiry Chatbot.\n\n"
            "You can ask me about courses, admissions, fees, hostel, "
            "transport, library, contact details and timings."
        )

    # Default
    else:

        return (
            "🤖 **Sorry, I couldn't understand your question.**\n\n"
            "You can ask me about:\n\n"
            "• 📚 Courses\n"
            "• ✅ Eligibility\n"
            "• 📝 Admissions\n"
            "• 💰 Fees\n"
            "• 🏠 Hostel\n"
            "• 🚌 Transport\n"
            "• 📖 Library\n"
            "• 📞 Contact\n"
            "• ⏰ Timings"
        )


# --------------------------------------------------
# DISPLAY OLD MESSAGES
# --------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# QUICK QUESTION
# --------------------------------------------------
if "quick_question" in st.session_state:

    user_question = st.session_state.quick_question

    del st.session_state.quick_question

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    answer = get_answer(user_question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------
user_question = st.chat_input(
    "Ask your question about MRECW..."
)

if user_question:

    # User message
    with st.chat_message("user"):

        st.markdown(user_question)

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    # AI answer
    answer = get_answer(user_question)

    with st.chat_message("assistant"):

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")

st.markdown(
    """
    <center>
    🎓 <b>MRECW AI College Enquiry Chatbot</b><br>
    Malla Reddy Engineering College for Women<br>
    Maisammaguda, Hyderabad, Telangana
    </center>
    """,
    unsafe_allow_html=True
)