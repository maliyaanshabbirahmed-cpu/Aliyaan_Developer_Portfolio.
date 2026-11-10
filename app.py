import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Muhammad Aliyaan | Developer Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
PROFILE_IMAGE = ROOT / "assets" / "profile_photo.jpg"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
:root { --gold:#d9b66f; --muted:#a6a6b2; --panel:#151720; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp {
  background:
    radial-gradient(circle at 82% 5%, rgba(201,160,83,.13), transparent 28%),
    radial-gradient(circle at 8% 35%, rgba(61,79,125,.12), transparent 30%),
    #090a0f;
  color:#f5f5f7;
}
.block-container { max-width:1180px; padding-top:2rem; padding-bottom:4rem; }
h1,h2,h3 { font-family:'Space Grotesk',sans-serif !important; }
a { color:var(--gold) !important; }
.hero {
  background:linear-gradient(135deg,rgba(28,30,40,.98),rgba(15,16,22,.96));
  border:1px solid rgba(217,182,111,.28); border-radius:26px;
  padding:34px; box-shadow:0 18px 60px rgba(0,0,0,.25);
}
.eyebrow { color:var(--gold); letter-spacing:.18em; text-transform:uppercase; font-size:.76rem; font-weight:700; }
.hero-title { font-family:'Space Grotesk',sans-serif; font-size:clamp(2.1rem,5vw,4rem); line-height:1.05; font-weight:700; margin:.45rem 0; }
.hero-sub { color:#d7d7df; font-size:1.1rem; line-height:1.65; max-width:720px; }
.pill {
 display:inline-block; border:1px solid rgba(217,182,111,.3); background:rgba(217,182,111,.08);
 color:#ead5a7; border-radius:999px; padding:6px 11px; margin:4px 5px 4px 0; font-size:.82rem;
}
.section-kicker { color:var(--gold); font-size:.76rem; letter-spacing:.16em; font-weight:700; text-transform:uppercase; }
.project {
 background:linear-gradient(145deg,#181a24,#11131a); border:1px solid #2a2d39;
 border-radius:18px; padding:22px; min-height:270px; height:100%;
}
.project h3 { margin:.4rem 0 .65rem 0; font-size:1.25rem; }
.project p { color:#c1c2cb; line-height:1.6; font-size:.94rem; }
.project-meta { color:#9fa1ad; font-size:.8rem; margin-top:14px; }
.project-link {
 display:inline-block; margin-top:14px; padding:9px 14px; border-radius:10px;
 background:rgba(217,182,111,.12); border:1px solid rgba(217,182,111,.35);
 text-decoration:none !important; font-weight:600;
}
.skill-card {
 background:#141620; border:1px solid #282b36; border-radius:15px;
 padding:17px; margin-bottom:10px; min-height:140px;
}
.skill-card h4 { color:#f1d69e; margin:0 0 10px 0; font-family:'Space Grotesk',sans-serif; }
.small-muted { color:#a6a8b3; font-size:.88rem; line-height:1.6; }
.footer { border-top:1px solid #292b35; padding-top:22px; color:#999ba6; text-align:center; }
div[data-testid="stImage"] img { border-radius:20px; }
.stButton button { border-radius:10px; }
</style>
""", unsafe_allow_html=True)

# Header navigation
nav1, nav2 = st.columns([3, 2])
with nav1:
    st.markdown("**MA.** <span style='color:#d9b66f'>PORTFOLIO</span>", unsafe_allow_html=True)
with nav2:
    st.markdown("<div style='text-align:right;color:#a6a6b2;font-size:.88rem'>ABOUT &nbsp; · &nbsp; PROJECTS &nbsp; · &nbsp; SKILLS &nbsp; · &nbsp; EDUCATION</div>", unsafe_allow_html=True)

st.write("")
with st.container():
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    left, right = st.columns([1, 2.5], vertical_alignment="center")
    with left:
        if PROFILE_IMAGE.exists():
            st.image(str(PROFILE_IMAGE), use_container_width=True)
    with right:
        st.markdown('<div class="eyebrow">Aspiring AI & Software Developer</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Muhammad Aliyaan<br>Shabbir Ahmed</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-sub">A student developer exploring Python, Data Science, Machine Learning, Computer Vision and Generative AI. I enjoy learning by building practical applications and turning ideas into working software.</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<span class="pill">Python</span><span class="pill">Data Science</span>'
            '<span class="pill">Machine Learning</span><span class="pill">Generative AI</span>'
            '<span class="pill">Streamlit</span>',
            unsafe_allow_html=True
        )
        st.caption("Grade 9 student · Agentic AI & Data Science learner at Saylani Mass IT Training (SMIT)")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.markdown('<div class="section-kicker">01 / About</div>', unsafe_allow_html=True)
st.header("Curious by nature. Building through code.")
st.markdown("""
I am a Grade 9 student currently studying **Agentic AI and Data Science at Saylani Mass IT Training (SMIT)**.
I am a fast learner who enjoys understanding how technology works, experimenting with new tools and developing
applications. My current learning spans Python programming, data analysis, machine learning, deep learning,
computer vision and Generative AI.

My long-term ambition is to contribute to meaningful technology and, one day, work with an innovative
organization such as **Microsoft or OpenAI**. I see that ambition as a direction to work toward through
consistent learning, strong fundamentals and real project experience.
""")

st.write("")
st.markdown('<div class="section-kicker">02 / Selected work</div>', unsafe_allow_html=True)
st.header("Projects")
st.markdown('<p class="small-muted">A selection of applications I have built and deployed. Open each project to explore it.</p>', unsafe_allow_html=True)

projects = [
    {
        "number":"PROJECT 01",
        "name":"LinguaFlow — Voice & Text Translator",
        "description":"A translation application focused on helping users convert language content. The project has been developed around speech recognition and translation workflows. Supported languages and current voice features should be confirmed against the live app.",
        "stack":"Python · Streamlit · Speech / Translation APIs",
        "url":"https://transalatorapppy-fejjzljvfuhtmsbkge9ftx.streamlit.app/",
        "status":"Deployed app",
    },
    {
        "number":"PROJECT 02",
        "name":"ImageData Extractor — Image to CSV",
        "description":"An image-data extraction application designed to read text, numbers and other visible information from uploaded images, then organize extracted content for CSV-style data output. Review the live app for the exact recognition and export options.",
        "stack":"Python · Streamlit · OCR / Image Processing",
        "url":"https://imagedataextractor-lappjdyaltzgrndw8cu5cvb.streamlit.app/",
        "status":"Deployed app",
    },
    {
        "number":"PROJECT 03",
        "name":"Khurram Tuition AI — Learning Assistant",
        "description":"An AI-focused tuition and learning project. The precise features and intended student workflow have not yet been provided, so this portfolio keeps the description general rather than claiming unverified capabilities.",
        "stack":"Python · Streamlit · AI (confirm exact stack)",
        "url":"https://khurramtuitionaibyaliyaan-g5nnntims5x7yp4elbndhr.streamlit.app/",
        "status":"Link supplied from app name",
    },
]

cols = st.columns(3, gap="medium")
for col, p in zip(cols, projects):
    with col:
        st.markdown(f"""
        <div class="project">
          <div class="section-kicker">{p['number']}</div>
          <h3>{p['name']}</h3>
          <p>{p['description']}</p>
          <div class="project-meta"><b>Technology:</b> {p['stack']}<br><b>Status:</b> {p['status']}</div>
          <a class="project-link" href="{p['url']}" target="_blank" rel="noopener noreferrer">Open application ↗</a>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.markdown('<div class="section-kicker">03 / Technical toolkit</div>', unsafe_allow_html=True)
st.header("Skills & learning")
st.markdown('<p class="small-muted">Topics studied through coursework and practice. This section describes learning exposure, not a claim of expert-level proficiency in every tool.</p>', unsafe_allow_html=True)

skill_groups = [
    ("Python Programming", "Python fundamentals, variables and data types, conditionals, loops, functions, modules, data structures, OOP, file handling, exception handling, libraries and packages."),
    ("Data Science & Analytics", "NumPy, Pandas, data cleaning, preprocessing, data analysis, exploratory data analysis (EDA), statistics, probability, Matplotlib, Seaborn and data visualization."),
    ("Machine Learning", "Supervised and unsupervised learning, Linear Regression, Logistic Regression, Decision Trees, Random Forest, Support Vector Machines (SVM), model training, testing and evaluation."),
    ("Deep Learning & Computer Vision", "Artificial Neural Networks (ANN), Convolutional Neural Networks (CNN), TensorFlow, Keras, YOLO object detection, image classification and image preprocessing."),
    ("Generative AI", "Large Language Models (LLMs), Generative AI, OpenAI and Gemini APIs, prompt engineering, LangChain and Agentic AI workflows."),
    ("App Development & Deployment", "Streamlit, frontend/backend concepts, Git and GitHub, virtual environments, pip, requirements.txt, Streamlit Cloud deployment and Python application development."),
]
skill_cols = st.columns(2, gap="medium")
for i, (title, desc) in enumerate(skill_groups):
    with skill_cols[i % 2]:
        st.markdown(f'<div class="skill-card"><h4>{title}</h4><div class="small-muted">{desc}</div></div>', unsafe_allow_html=True)

st.write("")
st.markdown('<div class="section-kicker">04 / Education</div>', unsafe_allow_html=True)
st.header("Education & ongoing learning")
e1, e2 = st.columns(2)
with e1:
    st.markdown("**School Education**")
    st.markdown("Grade 9 student")
with e2:
    st.markdown("**Saylani Mass IT Training (SMIT)**")
    st.markdown("Agentic AI and Data Science courses")

st.write("")
st.markdown('<div class="section-kicker">05 / Direction</div>', unsafe_allow_html=True)
st.header("Building toward the future")
st.markdown("""
I want to keep strengthening my programming foundations, build useful AI-powered applications and gain
experience solving real problems. My long-term goal is to become a skilled software and AI professional
and work toward opportunities at companies such as Microsoft or OpenAI.
""")

st.markdown("")
st.markdown('<div class="footer">© 2026 Muhammad Aliyaan Shabbir Ahmed · Built with Python & Streamlit</div>', unsafe_allow_html=True)
