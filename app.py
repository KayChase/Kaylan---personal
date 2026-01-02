import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Kaylan Chase | Portfolio",
    page_icon="👋",
    layout="wide",
)

# ---------- QUICK EDIT SECTION ----------
NAME = "Kaylan Chase"
TAGLINE = "Informatics student • Business minor • Building projects in software, data, and tech"
LOCATION = "New York, NY"
EMAIL = "chasekaylan@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/kaylan-chase-3007022a5"
GITHUB = "https://github.com/your-username"  # change this

PROJECTS = [
    {
        "title": "Countries Visited Manager",
        "desc": "Object-oriented tracker to log countries, notes, and trip details.",
        "stack": ["Python", "OOP"],
        "links": {"GitHub": "https://github.com/your-username/countries-visited"},
    },
    {
        "title": "Library Book Checkout System",
        "desc": "Checkout + CSV persistence + overdue tracking with clean menus.",
        "stack": ["Python", "CSV"],
        "links": {"GitHub": "https://github.com/your-username/library-system"},
    },
    {
        "title": "Weather API App",
        "desc": "Pulls live weather data from an API and displays results in a simple UI.",
        "stack": ["Python", "APIs", "JSON"],
        "links": {"GitHub": "https://github.com/your-username/weather-api"},
    },
]

EXPERIENCE = [
    {
        "role": "Intern",
        "company": "IvySwimwear",
        "bullets": [
            "Supported business operations and helped with data/marketing tasks.",
            "Worked cross-functionally and improved organization/communication.",
        ],
    },
    {
        "role": "Fellow / Internship Experience",
        "company": "NYSTEC IgniteU (if applicable)",
        "bullets": [
            "Worked on tech-focused projects and professional development.",
            "Strengthened communication, teamwork, and problem-solving.",
        ],
    },
]

SKILLS = ["Python", "SQL", "Excel", "Data Analysis", "Problem Solving", "Communication"]

# ---------- STYLES ----------
st.markdown(
    """
    <style>
      .hero {padding: 28px 24px; border-radius: 18px; background: #0b1220;}
      .hero h1 {color: white; margin-bottom: 4px;}
      .hero p {color: #cbd5e1; margin-top: 0px;}
      .pill {display:inline-block; padding:6px 10px; border-radius:999px; border:1px solid #334155; margin: 4px 6px 0 0;}
      .card {padding:18px; border:1px solid #243045; border-radius:18px; background:#0b1220;}
      .muted {color:#cbd5e1;}
      a {text-decoration:none;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- HEADER / HERO ----------
left, right = st.columns([2, 1], vertical_alignment="center")
with left:
    st.markdown(f"""
    <div class="hero">
      <h1>{NAME}</h1>
      <p>{TAGLINE}</p>
      <p class="muted">📍 {LOCATION} • ✉️ {EMAIL}</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("### Links")
    st.link_button("LinkedIn", LINKEDIN, use_container_width=True)
    if GITHUB != "https://github.com/your-username":
        st.link_button("GitHub", GITHUB, use_container_width=True)
    st.link_button("Email me", f"mailto:{EMAIL}", use_container_width=True)

st.write("")
tab1, tab2, tab3 = st.tabs(["Projects", "Experience", "Skills"])

# ---------- PROJECTS ----------
with tab1:
    st.subheader("Projects")
    cols = st.columns(3)
    for i, p in enumerate(PROJECTS):
        with cols[i % 3]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"**{p['title']}**")
            st.markdown(f"<p class='muted'>{p['desc']}</p>", unsafe_allow_html=True)

            st.markdown("**Tech:**")
            st.markdown("".join([f"<span class='pill'>{s}</span>" for s in p["stack"]]), unsafe_allow_html=True)

            st.write("")
            for label, url in p["links"].items():
                st.link_button(label, url, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

# ---------- EXPERIENCE ----------
with tab2:
    st.subheader("Experience")
    for e in EXPERIENCE:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"**{e['role']} — {e['company']}**")
        for b in e["bullets"]:
            st.markdown(f"- {b}")
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")

# ---------- SKILLS ----------
with tab3:
    st.subheader("Skills")
    st.markdown("".join([f"<span class='pill'>{s}</span>" for s in SKILLS]), unsafe_allow_html=True)

st.write("")
st.caption("Built with Python + Streamlit. Customize the text at the top of app.py.")
