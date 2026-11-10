
import streamlit as st
from pathlib import Path
import base64
import html

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Aliyaan | Developer Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
PROJECT_IMAGES = ASSETS_DIR / "projects"

# ============================================================
# PERSONAL INFORMATION
# Edit these values whenever needed.
# ============================================================

NAME = "M. Aliyaan Shabbir Ahmed"
ROLE = "Python Developer | AI & Machine Learning Enthusiast"

INTRO = """
I am a developer interested in Python programming, artificial
intelligence, machine learning, and building practical software
applications. I enjoy learning new technologies and turning
ideas into working projects.
"""

EMAIL = ""  # Add your real email address here.

GITHUB = "https://github.com/maliyaanshabbirahmed-cpu"

# ============================================================
# IMAGE FUNCTIONS
# ============================================================

def get_image_base64(image_path):
    path = Path(image_path)

    if not path.exists():
        return None

    try:
        return base64.b64encode(path.read_bytes()).decode("utf-8")
    except Exception:
        return None


def display_profile_image():
    image_path = BASE_DIR / "profile_photo.jpg"
    encoded = get_image_base64(image_path)

    if encoded:
        st.markdown(
            f"""
            <div class="profile-image-container">
                <img src="data:image/jpeg;base64,{encoded}"
                     class="profile-image">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(
            "Profile image not found. Add profile_photo.jpg "
            "to the root directory of your repository."
        )


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --gold: #D6AE55;
    --gold-light: #F3D58B;
    --background: #080808;
    --card: #121212;
    --text: #F5F5F5;
    --muted: #A0A0A0;
}

html {
    scroll-behavior: smooth;
}

.stApp {
    background: var(--background);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
}

.gold {
    color: var(--gold);
}

.hero {
    padding: 65px 15px 45px;
    text-align: center;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(38px, 6vw, 68px);
    font-weight: 800;
    letter-spacing: -2px;
    margin-bottom: 10px;
    color: white;
}

.hero-role {
    color: var(--gold);
    font-size: 20px;
    font-weight: 600;
}

.hero-description {
    max-width: 720px;
    margin: 20px auto;
    color: #B7B7B7;
    font-size: 16px;
    line-height: 1.9;
}

.profile-image-container {
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
}

.profile-image {
    width: 205px;
    height: 205px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid var(--gold);
    padding: 5px;
    background: #121212;
    box-shadow: 0 0 35px rgba(214,174,85,0.20);
}

.section-title {
    font-size: 34px;
    font-weight: 800;
    margin-top: 65px;
    margin-bottom: 8px;
    color: white;
}

.section-subtitle {
    color: #999;
    margin-bottom: 28px;
    font-size: 15px;
}

.gold-line {
    width: 65px;
    height: 4px;
    background: var(--gold);
    border-radius: 5px;
    margin: 12px 0 25px;
}

.project-card {
    background: linear-gradient(145deg, #171717, #0E0E0E);
    border: 1px solid #292929;
    border-radius: 15px;
    padding: 20px;
    min-height: 230px;
    margin-bottom: 20px;
    transition: 0.3s ease;
}

.project-card:hover {
    border-color: var(--gold);
    transform: translateY(-5px);
}

.project-card h3 {
    color: var(--gold-light);
    font-size: 21px;
    margin-bottom: 12px;
}

.project-card p {
    color: #B5B5B5;
    line-height: 1.7;
    font-size: 14px;
}

.skill-card {
    background: #141414;
    border: 1px solid #292929;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 12px;
    text-align: center;
    color: #E8E8E8;
    font-weight: 600;
    transition: 0.2s;
}

.skill-card:hover {
    border-color: var(--gold);
    color: var(--gold);
}

.info-card {
    background: #141414;
    border: 1px solid #292929;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 15px;
}

.info-card h3 {
    color: var(--gold);
}

.tag {
    display: inline-block;
    color: var(--gold-light);
    background: #282216;
    border: 1px solid #544324;
    border-radius: 20px;
    padding: 5px 12px;
    font-size: 12px;
    margin: 4px 3px;
}

.footer {
    border-top: 1px solid #292929;
    text-align: center;
    padding: 30px 10px;
    margin-top: 65px;
    color: #888;
    font-size: 13px;
}

div.stButton > button {
    background: var(--gold);
    color: #080808;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    padding: 10px 22px;
}

div.stButton > button:hover {
    background: var(--gold-light);
    color: black;
    border: none;
}

a {
    color: var(--gold-light) !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

nav1, nav2, nav3, nav4, nav5 = st.columns(5)

with nav1:
    st.markdown("[Home](#home)")

with nav2:
    st.markdown("[About](#about-me)")

with nav3:
    st.markdown("[Skills](#technical-skills)")

with nav4:
    st.markdown("[Projects](#my-projects)")

with nav5:
    st.markdown("[Contact](#contact-me)")


# ============================================================
# HERO SECTION
# ============================================================

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

st.markdown('<div class="hero">', unsafe_allow_html=True)

display_profile_image()

st.markdown(
    f'<div class="hero-title">{html.escape(NAME)}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="hero-role">{html.escape(ROLE)}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="hero-description">{html.escape(INTRO.strip())}</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# ABOUT SECTION
# ============================================================

st.markdown('<div id="about-me"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">About <span class="gold">Me</span></div>',
    unsafe_allow_html=True
)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

about1, about2 = st.columns([1.5, 1])

with about1:
    st.markdown("""
    I am a technology enthusiast focused on software development
    and artificial intelligence.

    My interests include:

    - Python application development
    - Machine Learning and Deep Learning
    - Computer Vision and YOLO
    - AI-powered applications
    - Natural Language Processing
    - Building interactive web applications

    My objective is to continuously improve my programming
    abilities and develop useful real-world applications.
    """)

with about2:
    st.markdown("""
    <div class="info-card">
        <h3>Developer Profile</h3>
        <p><b>Primary Language:</b> Python</p>
        <p><b>Framework:</b> Streamlit</p>
        <p><b>Interests:</b> AI / ML</p>
        <p><b>Focus:</b> Application Development</p>
        <p><b>Location:</b> Karachi, Pakistan</p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SKILLS SECTION
# ============================================================

st.markdown('<div id="technical-skills"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Technical <span class="gold">Skills</span></div>',
    unsafe_allow_html=True
)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

skills = {
    "Programming": [
        "Python",
        "SQL",
        "JavaScript"
    ],
    "AI & Machine Learning": [
        "Machine Learning",
        "Deep Learning",
        "YOLO",
        "Computer Vision",
        "RAG",
        "LangChain"
    ],
    "Development Tools": [
        "Streamlit",
        "Git",
        "GitHub",
        "VS Code",
        "Google Colab"
    ]
}

for category, skill_list in skills.items():

    st.subheader(category)

    columns = st.columns(4)

    for index, skill in enumerate(skill_list):
        with columns[index % 4]:
            st.markdown(
                f'<div class="skill-card">{html.escape(skill)}</div>',
                unsafe_allow_html=True
            )


# ============================================================
# PROJECTS SECTION
# ============================================================

st.markdown('<div id="my-projects"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">My <span class="gold">Projects</span></div>',
    unsafe_allow_html=True
)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-subtitle">Selected software and AI projects.</div>',
    unsafe_allow_html=True
)

projects = [
    {
        "name": "LinguaFlow",
        "description": "A voice and text translation application designed to support multilingual communication.",
        "tech": ["Python", "Streamlit", "Speech Recognition", "Translation"],
        "image": "linguaflow.png",
        "icon": "🌍",
        "url": ""
    },
    {
        "name": "ImageData Extractor",
        "description": "An image-to-data application focused on extracting text and numerical information from images and converting it into structured CSV data.",
        "tech": ["Python", "OCR", "Computer Vision", "CSV"],
        "image": "image_extractor.png",
        "icon": "📄",
        "url": ""
    },
    {
        "name": "Khurram Tuition AI",
        "description": "An educational AI application concept focused on providing learning assistance.",
        "tech": ["Python", "AI", "Streamlit"],
        "image": "khurram_tuition.png",
        "icon": "🎓",
        "url": ""
    }
]

project_columns = st.columns(2)

for index, project in enumerate(projects):

    with project_columns[index % 2]:

        st.markdown('<div class="project-card">', unsafe_allow_html=True)

        image_path = PROJECT_IMAGES / project["image"]

        if image_path.exists():
            st.image(str(image_path), use_container_width=True)
        else:
            st.markdown(
                f'<div style="font-size:55px;text-align:center;padding:20px;">'
                f'{project["icon"]}</div>',
                unsafe_allow_html=True
            )

        st.markdown(
            f'<h3>{html.escape(project["name"])}</h3>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<p>{html.escape(project["description"])}</p>',
            unsafe_allow_html=True
        )

        tags = "".join(
            f'<span class="tag">{html.escape(tag)}</span>'
            for tag in project["tech"]
        )

        st.markdown(tags, unsafe_allow_html=True)

        if project["url"]:
            st.link_button("View Project", project["url"])

        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# ADDITIONAL PROJECT IMAGE GALLERY
# ============================================================

st.markdown(
    '<div class="section-title">Project <span class="gold">Gallery</span></div>',
    unsafe_allow_html=True
)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

gallery_images = [
    PROJECT_IMAGES / "linguaflow.png",
    PROJECT_IMAGES / "image_extractor.png",
    PROJECT_IMAGES / "khurram_tuition.png"
]

existing_gallery = [p for p in gallery_images if p.exists()]

if existing_gallery:

    gallery_columns = st.columns(3)

    for index, image_path in enumerate(existing_gallery):
        with gallery_columns[index % 3]:
            st.image(
                str(image_path),
                caption=image_path.stem.replace("_", " ").title(),
                use_container_width=True
            )
else:
    st.info(
        "Add your project screenshots to assets/projects "
        "to display them in this gallery."
    )


# ============================================================
# CONTACT SECTION
# ============================================================

st.markdown('<div id="contact-me"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Contact <span class="gold">Me</span></div>',
    unsafe_allow_html=True
)

st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

st.markdown("""
Interested in discussing a project, technology, or collaboration?
You can reach me through the contact details below.
""")

contact1, contact2 = st.columns(2)

with contact1:

    if EMAIL.strip():
        st.markdown(f"**Email:** {EMAIL}")
        st.link_button(
            "Send Me an Email",
            f"mailto:{EMAIL}"
        )
    else:
        st.info("Add your email address in the EMAIL variable.")

with contact2:

    st.markdown("**GitHub:** Developer repository")

    st.link_button(
        "View My GitHub Repositories",
        GITHUB
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    <p>Designed and developed by M. Aliyaan Shabbir Ahmed</p>
    <p>Python • Artificial Intelligence • Software Development</p>
    <p>© 2026 All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
