import streamlit as st
import pandas as pd
import requests
import pydeck as pdk

# 1) Page layout
st.set_page_config(page_title="Vessel Tracks by MMSI", layout="wide")
st.title("📡 Vessel Positions by MMSI")

# 2) User input
mmsi = st.number_input(
    "Enter MMSI", 
    min_value=0, 
    step=1, 
    format="%d",
    help="Maritime Mobile Service Identity number"
)
if st.button("Fetch Track"):

    # 3) Call your FastAPI endpoint
    url = f"http://localhost:8000/mmsi/{mmsi}"
    with st.spinner("Loading AIS data..."):
        resp = requests.get(url)
    if not resp.ok:
        st.error(f"API returned {resp.status_code}")
        st.stop()

    data = resp.json()
    if not data:
        st.warning("No data found for that MMSI.")
        st.stop()

    # 4) Build a DataFrame and clean
    df = pd.DataFrame(data)
    # ensure numeric lat/lon
    df['latitude']  = pd.to_numeric(df['latitude'],  errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df = df.dropna(subset=['latitude','longitude'])
    df = df[df['latitude'].between(-90,90) & df['longitude'].between(-180,180)]

    # 5) Display a simple point map
    st.subheader("Raw Positions")
    st.map(df[['latitude','longitude']])

    # 6) Bonus: draw a path in PyDeck
    st.subheader("Track Path")
    # sort by timestamp if available
    if 'ts' in df.columns:
        df['ts'] = pd.to_datetime(df['ts'])
        df = df.sort_values('ts')

    # single-line path layer
    path_data = [{
        "path": df[['longitude','latitude']].values.tolist()
    }]

    layer = pdk.Layer(
        "PathLayer",
        data=path_data,
        get_color=[255, 0, 0],
        width_scale=20,
        width_min_pixels=2,
    )

    # center view
    mid_lon = df['longitude'].mean()
    mid_lat = df['latitude'].mean()
    view_state = pdk.ViewState(
        longitude=mid_lon,
        latitude=mid_lat,
        zoom=6,
        pitch=0,
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/light-v10"
    )

    st.pydeck_chart(deck)
