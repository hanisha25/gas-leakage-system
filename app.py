import streamlit as st
import random
import time
import pandas as pd
import csv
import os
import pickle

# Set the page configuration before any Streamlit elements
st.set_page_config(page_title="Gas Leak Detector", page_icon="🔥", layout="centered")

# Load trained AI model
with open('gas_ai_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize pygame mixer

# Simulate gas reading
def simulate_gas_reading():
    return random.uniform(100, 1200)

# Styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 15px;
        }
        h1, h2, h3 {
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("🔥 Gas Leakage Detector")
st.subheader("📱 Real-Time Monitoring with Chart")

refresh_rate = 2  # seconds
placeholder = st.empty()
chart_placeholder = st.empty()

# Store readings
gas_data = []

# CSV file setup
csv_file = 'gas_log.csv'
if not os.path.isfile(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Gas Level'])

# Main monitoring loop
for _ in range(1000):
    gas_level = simulate_gas_reading()
    current_time = time.strftime('%H:%M:%S')
    gas_data.append({'Time': current_time, 'Gas Level': gas_level})

    # Log to CSV
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, gas_level])

    with placeholder.container():
        st.markdown(f"<h2>🧪 Gas Level: <span style='color:#333'>{gas_level:.2f} ppm</span></h2>", unsafe_allow_html=True)

        if gas_level < 400:
            status = "✅ Safe"
            color = "green"
            alarm_sound.stop()
        elif 400 <= gas_level < 700:
            status = "⚠️ Warning"
            color = "orange"
            alarm_sound.stop()
        else:
            status = "🚨 Leak Detected"
            color = "red"
            if not pygame.mixer.get_busy():
                alarm_sound.play(-1)

            # Optional mobile sound (browser-based)
            st.markdown(
                """
                <audio autoplay>
                    <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav">
                </audio>
                """,
                unsafe_allow_html=True
            )

        st.markdown(f"<h2 style='color:{color}'>{status}</h2>", unsafe_allow_html=True)

    # Show chart
    df = pd.DataFrame(gas_data[-20:])  # show last 20 readings
    chart_placeholder.line_chart(df.set_index("Time"), use_container_width=True)

    time.sleep(refresh_rate)

st.markdown(
    """
    <audio autoplay>
        <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav">
    </audio>
    """,
    unsafe_allow_html=True
)
