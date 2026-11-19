
import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="ResearchIQ | AI Research Workspace",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION STATE ----------------

if "uploaded_papers" not in st.session_state:
    st.session_state.uploaded_papers = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #F7F8FC;
}

[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263247;
}

[data-testid="stSidebar"] * {
    color: #E5E7EB;
}

.brand {
    font-family: 'Manrope', sans-serif;
    font-size: 27px;
    font-weight: 800;
    color: white;
    letter-spacing: -1px;
    padding: 12px 0 2px 0;
}

.brand span {
    color: #A78BFA;
}

.sidebar-caption {
    color: #9CA3AF;
    font-size: 12px;
    margin-bottom: 28px;
}

.main-title {
    font-family: 'Manrope', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #172033;
    letter-spacing: -1px;
    margin-bottom: 3px;
}

.subtitle {
    color: #778196;
    font-size: 14px;
    margin-bottom: 24px;
}

.hero {
    background: linear-gradient(115deg, #202B50 0%, #43358B 58%, #7054C8 100%);
    border-radius: 18px;
    padding: 30px;
    color: white;
    margin: 12px 0 24px 0;
}

.hero h2 {
    color: white;
    font-family: 'Manrope', sans-serif;
    font-size: 27px;
    margin-bottom: 8px;
}

.hero p {
    color: #E1DDFB;
    font-size: 14px;
    max-width: 600px;
}

.section-title {
    color: #202A3D;
    font-family: 'Manrope', sans-serif;
    font-weight: 750;
    font-size: 19px;
    margin: 22px 0 12px 0;
}

.metric-card {
    background: white;
    border: 1px solid #E8EAF2;
    border-radius: 15px;
    padding: 19px;
    min-height: 112px;
}

.metric-label {
    color: #7B8497;
    font-size: 12px;
    font-weight: 600;
}

.metric-value {
    color: #202A3D;
    font-family: 'Manrope', sans-serif;
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}

.feature-card {
    background: white;
    border: 1px solid #E8EAF2;
    border-radius: 15px;
    padding: 20px;
    min-height: 155px;
}

.feature-icon {
    font-size: 23px;
    margin-bottom: 9px;
}

.feature-card h4 {
    color: #202A3D;
    font-size: 15px;
    margin: 0 0 7px 0;
}

.feature-card p {
    color: #7B8497;
    font-size: 12px;
    line-height: 1.6;
}

.info-box {
    background: #F0EDFF;
    border: 1px solid #E2DCFF;
    border-radius: 12px;
    padding: 15px;
    color: #51418C;
    font-size: 13px;
}

div.stButton > button {
    border-radius: 10px;
    border: 1px solid #DDD6FE;
    background: #6D5BD0;
    color: white;
    font-weight: 600;
    min-height: 42px;
}

div.stButton > button:hover {
    background: #5846B6;
    border-color: #5846B6;
    color: white;
}

.stTextInput input, .stTextArea textarea {
    border-radius: 10px;
}

div[data-testid="stFileUploader"] {
    background: white;
    border: 1px dashed #B9B1E8;
    border-radius: 14px;
    padding: 12px;
}

hr {
    border-color: #E8EAF2;
}

.footer {
    color: #929BAD;
    font-size: 11px;
    text-align: center;
    padding: 25px 0 8px 0;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown(
        '<div class="brand">Research<span>IQ</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-caption">AI-POWERED RESEARCH WORKSPACE</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "WORKSPACE",
        [
            "Overview",
            "Paper Library",
            "Summarization",
            "Research Copilot",
            "Semantic Search",
            "Paper Comparison",
            "Research Insights"
        ],
        label_visibility="visible"
    )

    st.markdown("---")

    st.markdown("**YOUR WORKSPACE**")

    st.caption(
        f"📚 {len(st.session_state.uploaded_papers)} uploaded file(s)"
    )

    st.markdown("---")
    st.caption("ResearchIQ · Project Prototype")
    st.caption("Built with Python & Transformers")

# ---------------- REUSABLE HEADER ----------------

def page_header(title, description):
    st.markdown(
        f'<div class="main-title">{title}</div>'
        f'<div class="subtitle">{description}</div>',
        unsafe_allow_html=True
    )

# ---------------- OVERVIEW ----------------

if page == "Overview":

    page_header(
        "Research workspace",
        "Your central space to explore, understand and compare research."
    )

    st.markdown("""
    <div class="hero">
        <h2>Turn research papers into insights.</h2>
        <p>
        Upload academic papers, discover important findings,
        ask questions and explore research with AI-powered tools.
        Everything you need for a smarter research workflow.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    metrics = [
        ("PAPERS UPLOADED", len(st.session_state.uploaded_papers)),
        ("AI FEATURES", "6"),
        ("WORKSPACE", "Active")
    ]

    for col, (label, value) in zip([col1, col2, col3], metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Explore your research tools</div>',
        unsafe_allow_html=True
    )

    features = [
        ("📄", "Paper Summarization",
         "Understand lengthy academic papers through concise summaries."),
        ("💬", "Research Copilot",
         "Ask questions and explore answers grounded in your papers."),
        ("🔎", "Semantic Search",
         "Find relevant research passages using natural language."),
        ("⚖️", "Paper Comparison",
         "Compare objectives, methodologies and findings."),
        ("🧠", "Topic Classification",
         "Discover the research topics covered by your papers."),
        ("📊", "Research Insights",
         "Explore extracted information and research patterns.")
    ]

    for start in range(0, len(features), 3):
        cols = st.columns(3)

        for col, item in zip(cols, features[start:start+3]):
            icon, title, description = item

            with col:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <h4>{title}</h4>
                    <p>{description}</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Get started</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        <b>New to ResearchIQ?</b><br>
        Start by uploading your research papers in the Paper Library.
        Then explore summarization, search and research chat.
    </div>
    """, unsafe_allow_html=True)

# ---------------- PAPER LIBRARY ----------------

elif page == "Paper Library":

    page_header(
        "Paper Library",
        "Upload and organize the research papers you want to explore."
    )

    uploaded_files = st.file_uploader(
        "Upload research papers",
        type=["pdf"],
        accept_multiple_files=True,
        help="Choose one or more PDF research papers."
    )

    if uploaded_files:
        existing_names = {
            file.name for file in st.session_state.uploaded_papers
        }

        for file in uploaded_files:
            if file.name not in existing_names:
                st.session_state.uploaded_papers.append(file)

        st.success("Uploaded files added to your session.")

    st.markdown(
        '<div class="section-title">Your documents</div>',
        unsafe_allow_html=True
    )

    if st.session_state.uploaded_papers:

        for i, file in enumerate(st.session_state.uploaded_papers):
            with st.container(border=True):
                col1, col2 = st.columns([5, 1])

                with col1:
                    st.markdown(f"**📄 {file.name}**")
                    st.caption(
                        f"PDF document · {file.size / 1024:.1f} KB"
                    )

                with col2:
                    if st.button("Remove", key=f"remove_{i}"):
                        st.session_state.uploaded_papers.pop(i)
                        st.rerun()

    else:
        st.info("No papers uploaded yet. Upload your first PDF above.")

# ---------------- SUMMARIZATION ----------------

elif page == "Summarization":

    page_header(
        "Paper Summarization",
        "Turn lengthy academic papers into easier-to-understand summaries."
    )

    st.markdown(
        '<div class="info-box">Select a paper and generate a concise summary. '
        'The summarization model will be connected in the backend integration stage.</div>',
        unsafe_allow_html=True
    )

    if st.session_state.uploaded_papers:

        names = [
            file.name for file in st.session_state.uploaded_papers
        ]

        selected = st.selectbox("Select a research paper", names)

        if st.button("Generate Summary"):
            st.info(
                "Frontend ready. Model connection is the next integration task."
            )

    else:
        st.warning("Upload a PDF in Paper Library to get started.")

# ---------------- RESEARCH COPILOT ----------------

elif page == "Research Copilot":

    page_header(
        "Research Copilot",
        "Ask questions and explore information from your research papers."
    )

    st.markdown("""
    <div class="info-box">
        Ask about a paper's methodology, findings, architecture,
        datasets or conclusions. Answers will include source references
        once the RAG backend is connected.
    </div>
    """, unsafe_allow_html=True)

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    question = st.chat_input("Ask something about your research...")

    if question:
        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            st.info(
                "The research-answering backend will be connected next."
            )

    if st.button("Clear conversation"):
        st.session_state.chat_history = []
        st.rerun()

# ---------------- SEMANTIC SEARCH ----------------

elif page == "Semantic Search":

    page_header(
        "Semantic Search",
        "Search research by meaning instead of relying only on exact keywords."
    )

    query = st.text_input(
        "What would you like to find?",
        placeholder="Example: How does self-attention work?"
    )

    top_k = st.slider(
        "Number of results",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("Search Research"):
        if query.strip():
            st.info(
                "Search interface ready. FAISS backend connection is pending."
            )
        else:
            st.warning("Please enter a search query.")

# ---------------- PAPER COMPARISON ----------------

elif page == "Paper Comparison":

    page_header(
        "Paper Comparison",
        "Understand how two research papers differ and where they overlap."
    )

    if len(st.session_state.uploaded_papers) >= 2:

        names = [
            file.name for file in st.session_state.uploaded_papers
        ]

        col1, col2 = st.columns(2)

        with col1:
            paper1 = st.selectbox(
                "First paper",
                names,
                key="comparison_paper1"
            )

        with col2:
            paper2 = st.selectbox(
                "Second paper",
                names,
                index=1,
                key="comparison_paper2"
            )

        if st.button("Compare Papers"):
            if paper1 == paper2:
                st.warning("Please select two different papers.")
            else:
                st.info(
                    "Comparison interface ready. Backend connection is pending."
                )

    else:
        st.info(
            "Upload at least two research papers in Paper Library "
            "to prepare a comparison."
        )

# ---------------- RESEARCH INSIGHTS ----------------

elif page == "Research Insights":

    page_header(
        "Research Insights",
        "Explore topics, extracted findings and patterns across your papers."
    )

    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <h4>Topic Classification</h4>
        <p>Identify the main research areas covered by your documents.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔑</div>
        <h4>Keyword Extraction</h4>
        <p>Discover important terms and keyphrases from research papers.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📑</div>
        <h4>Research Information</h4>
        <p>Explore objectives, methodologies, datasets, results and limitations.</p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "These sections will display real model results after backend integration."
    )

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    ResearchIQ · AI Research Paper Intelligence System<br>
    Designed for smarter academic research.
</div>
""", unsafe_allow_html=True)
