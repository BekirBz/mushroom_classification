import streamlit as st
import joblib
import pandas as pd

# 1. Modeli yükle
model = joblib.load("best_rf_model.pkl")

# 2. Kullanıcıdan veri alacak tüm alanları tanımla
st.title("🍄 Mushroom Edibility Predictor")
st.write("Enter the mushroom features below to predict if it's edible or poisonous.")

# Her bir sütunun UNIQUE değerleri (verinin kendisinden bakabilirsin)
cap_shape = st.selectbox("Cap Shape", ["b", "c", "x", "f", "k", "s"])
cap_surface = st.selectbox("Cap Surface", ["f", "g", "y", "s"])
cap_color = st.selectbox("Cap Color", ["n", "b", "c", "g", "r", "p", "u", "e", "w", "y"])
bruises = st.selectbox("Bruises", ["t", "f"])
odor = st.selectbox("Odor", ["a", "l", "c", "y", "f", "m", "n", "p", "s"])
gill_attachment = st.selectbox("Gill Attachment", ["a", "d", "f", "n"])
gill_spacing = st.selectbox("Gill Spacing", ["c", "w", "d"])
gill_size = st.selectbox("Gill Size", ["b", "n"])
gill_color = st.selectbox("Gill Color", ["k", "n", "b", "h", "g", "r", "o", "p", "u", "e", "w", "y"])
stalk_shape = st.selectbox("Stalk Shape", ["e", "t"])
stalk_root = st.selectbox("Stalk Root", ["b", "c", "u", "e", "z", "r", "?"])
stalk_surface_above_ring = st.selectbox("Stalk Surface Above Ring", ["f", "y", "k", "s"])
stalk_surface_below_ring = st.selectbox("Stalk Surface Below Ring", ["f", "y", "k", "s"])
stalk_color_above_ring = st.selectbox("Stalk Color Above Ring", ["n", "b", "c", "g", "o", "p", "e", "w", "y"])
stalk_color_below_ring = st.selectbox("Stalk Color Below Ring", ["n", "b", "c", "g", "o", "p", "e", "w", "y"])
veil_type = st.selectbox("Veil Type", ["p", "u"])
veil_color = st.selectbox("Veil Color", ["n", "o", "w", "y"])
ring_number = st.selectbox("Ring Number", ["n", "o", "t"])
ring_type = st.selectbox("Ring Type", ["c", "e", "f", "l", "n", "p", "s", "z"])
spore_print_color = st.selectbox("Spore Print Color", ["k", "n", "b", "h", "r", "o", "u", "w", "y"])
population = st.selectbox("Population", ["a", "c", "n", "s", "v", "y"])
habitat = st.selectbox("Habitat", ["g", "l", "m", "p", "u", "w", "d"])

# 3. Kullanıcıdan gelen verileri DataFrame’e çevir
input_df = pd.DataFrame([[
    cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment,
    gill_spacing, gill_size, gill_color, stalk_shape, stalk_root,
    stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring,
    stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type,
    spore_print_color, population, habitat
]], columns=[
    "cap-shape", "cap-surface", "cap-color", "bruises", "odor", "gill-attachment",
    "gill-spacing", "gill-size", "gill-color", "stalk-shape", "stalk-root",
    "stalk-surface-above-ring", "stalk-surface-below-ring", "stalk-color-above-ring",
    "stalk-color-below-ring", "veil-type", "veil-color", "ring-number", "ring-type",
    "spore-print-color", "population", "habitat"
])

# 4. Tahmin butonu
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("☠️ This mushroom is predicted to be **Poisonous!**")
    else:
        st.success("🍀 This mushroom is predicted to be **Edible!**")