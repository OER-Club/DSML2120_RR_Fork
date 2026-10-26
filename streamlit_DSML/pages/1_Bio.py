import streamlit as st
from pathlib import Path

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Ranjidha Rajan"
PROGRAM = "Your Program / Major / Professor"
INTRO = (
    "Write 2–3 sentences about yourself: what you’re studying/working on, "
    "what excites you about data visualization or computing, etc."
)
FUN_FACTS = [
    "I love …",
    "I’m learning …",
    "I want to build …",
]
#PHOTO_PATH = "RanjidhaR.jpg"  # Put a file in repo root or set a URL
def find_photo(filename="RanjidhaR.jpg"):
    # Try common locations for multipage apps
    try:
        script_dir = Path(__file__).resolve().parent
    except NameError:
        script_dir = Path.cwd()

    candidates = [
        script_dir / "assets" / filename,          # pages/assets/...
        script_dir.parent / "assets" / filename,   # root/assets/... (common)
        Path("assets") / filename,                 # cwd/assets/...
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    return None

photo_src = find_photo("RanjidhaR.jpg")

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` inside the `assets/` folder, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
