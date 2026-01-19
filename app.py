"""
Portfolio Data Scientist - Marwane Houngnon
Application Streamlit avec design professionnel et image de fond personnalisée
"""

# ============================================
# IMPORTS OPTIMISÉS
# ============================================
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from pathlib import Path
import base64
import json
import sys
import os
from typing import Dict, List, Optional, Tuple

# Configuration du path
sys.path.append(str(Path(__file__).parent))

# ============================================
# CONFIGURATION & CONSTANTES
# ============================================
class Config:
    """Configuration globale de l'application"""
    
    # App config
    PAGE_TITLE = "Marwane Houngnon | Data Scientist Portfolio"
    PAGE_ICON = "📊"
    LAYOUT = "wide"
    
    # Paths
    BASE_DIR = Path(__file__).parent
    ASSETS_DIR = BASE_DIR / "assets"
    IMAGES_DIR = ASSETS_DIR / "images"
    DATA_DIR = ASSETS_DIR / "data"
    
    # Background image (l'image que vous avez fournie)
    BACKGROUND_IMAGE = BASE_DIR / "image de fond.png"
    
    # Design
    COLORS = {
        "primary": "#ffffff",  # Blanc pour contraster
        "secondary": "#cccccc",
        "accent": "#00d4ff",   # Bleu data science
        "dark": "#0a0a0a",
        "light": "#e0e0e0",
        "overlay": "rgba(10, 10, 10, 0.85)"  # Overlay plus foncé
    }
    
    # Performance
    CACHE_TTL = 3600  # 1 heure

# ============================================
# GESTION DU CACHE (Performance)
# ============================================
@st.cache_data(ttl=Config.CACHE_TTL)
def load_profile_data() -> Dict:
    """Charge les données du profil avec cache"""
    return {
        "personal": {
            "name": "Marwane Houngnon",
            "title": "Statistician | Data Science & AI Researcher | Consultant",
            "photo": "assets/images/moi.jpeg", # Chemin original conservé
            "email": "alberichoun.del@gmail.com",
            "phone": "(+212) 641-364-029",
            "location": "Casablanca, Morocco",
            "summary": """
            AI/ML Engineer with two years of integrated academic, research, and industry experience, with a strong focus on 
            predictive modeling, deep learning, and computer vision. Demonstrated ability to design, implement, and evaluate 
            end-to-end machine learning pipelines, from data preprocessing to model optimization and deployment. Skilled in 
            developing and operationalizing advanced AI systems leveraging Docker-based workflows and core AWS services. 
            Academic contributions include co-authored publications in reputable journals (Web of Science, Taylor & Francis).
            """
        },
        "social": {
            "github": {"url": "https://github.com/Thekidmaroi", "icon": "https://cdn-icons-png.flaticon.com/512/25/25231.png", "name": "GitHub"},
            "linkedin": {"url": "https://linkedin.com/in/marwane-houngnon", "icon": "https://cdn-icons-png.flaticon.com/512/174/174857.png", "name": "LinkedIn"},
            "kaggle": {"url": "https://kaggle.com/marwanehoungnon", "icon": "https://cdn-icons-png.flaticon.com/512/5968/5968850.png", "name": "Kaggle"},
            "email": {"url": "mailto:alberichoun.del@gmail.com", "icon": "https://cdn-icons-png.flaticon.com/512/732/732200.png", "name": "Email"}
        },
        "stats": {
            "projects": 15,
            "years_exp": 2,
            "technologies": 30,
            "publications": 4,
            "models": 10
        }
    }

@st.cache_data(ttl=Config.CACHE_TTL)
def load_projects_data() -> List[Dict]:
    """Charge la liste des projets avec cache"""
    return [
        {
            "id": 1,
            "title": "🤖 LLM Containerized Pipeline",
            "category": "Generative AI • MLOps",
            "description": "Déploiement de modèles Mistral et DeepSeek via Docker pour l'automatisation de réponses clients.",
            "technologies": ["Python", "Mistral", "DeepSeek", "Docker", "Transformers", "FastAPI"],
            "features": ["Fine-tuning", "Conteneurisation", "API REST", "Optimisation de latence"],
            "client": "SRM-CS",
            "year": 2025,
            "github": "https://github.com/Thekidmaroi",
            "metrics": {"Latence": "-25%", "Précision": "92%", "Status": "Production"}
        },
        {
            "id": 2,
            "title": "🎯 Adaptive Recommendation Engine",
            "category": "Machine Learning • Career Guidance",
            "description": "Système SOIPA pour l'orientation de carrière basé sur des tests psychométriques personnalisés.",
            "technologies": ["Python", "Scikit-learn", "Pandas", "Streamlit", "Statistical Modeling"],
            "features": ["Recommandation adaptative", "Tests psychométriques", "Dashboard interactif"],
            "client": "Web4Jobs",
            "year": 2025,
            "github": "https://github.com/Thekidmaroi",
            "metrics": {"Engagement": "+15%", "Précision": "88%", "Users": "Active"}
        }
    ]

@st.cache_data(ttl=Config.CACHE_TTL)
def load_research_data() -> List[Dict]:
    """Charge les projets de recherche (publications)"""
    return [
        {
            "title": "Missing Data Robust EM for Incentive-Aware Markovian Smart Grid Optimization",
            "journal": "Web of Science Indexed Journal",
            "status": "Accepted and presented",
            "description": "Optimization of smart grid resources using Markov models robust to missing data."
        },
        {
            "title": "Dynamic Fusion of Hidden Markov Models and Neural Networks for Adaptive Pattern Recognition in Multimodal Environments",
            "journal": "Taylor & Francis Journal",
            "status": "Accepted and presented",
            "description": "Hybrid approach combining HMM and NN for pattern recognition."
        },
        {
            "title": "Markov-Optimized Resource Allocation for Sustainable 6G Mediterranean Smart Cities",
            "journal": "International Conference",
            "status": "Accepted and Presented",
            "description": "Resource allocation strategies for 6G networks in smart city contexts."
        },
        {
            "title": "Modeling Smart City Governance Transitions with HMM and Public IoT Data",
            "journal": "Research Paper",
            "status": "Accepted and Presented",
            "description": "Using IoT data and Hidden Markov Models to model governance transitions."
        }
    ]

@st.cache_data(ttl=Config.CACHE_TTL)
def load_skills_data() -> Dict:
    """Charge les compétences avec cache"""
    return {
        "technical": {
            "Python": {"level": 95, "category": "Languages", "years": 4, "logo": "https://cdn-icons-png.flaticon.com/512/5968/5968350.png"},
            "R": {"level": 82, "category": "Languages", "years": 2, "logo": "https://cdn-icons-png.flaticon.com/512/2103/2103601.png"},
            "SQL": {"level": 90, "category": "Databases", "years": 4, "logo": "https://cdn-icons-png.flaticon.com/512/4248/4248443.png"},
            "Machine Learning": {"level": 92, "category": "ML/DL", "years": 3, "logo": "https://cdn-icons-png.flaticon.com/512/2103/2103633.png"},
            "Deep Learning": {"level": 88, "category": "ML/DL", "years": 2, "logo": "https://cdn-icons-png.flaticon.com/512/8618/8618881.png"},
            "Computer Vision": {"level": 90, "category": "ML/DL", "years": 2, "logo": "https://cdn-icons-png.flaticon.com/512/10522/10522283.png"},
            "LLMs (Mistral/DeepSeek)": {"level": 85, "category": "ML/DL", "years": 1, "logo": "https://cdn-icons-png.flaticon.com/512/8618/8618847.png"},
            "Docker": {"level": 88, "category": "MLOps & Cloud", "years": 2, "logo": "https://cdn-icons-png.flaticon.com/512/919/919853.png"},
            "AWS": {"level": 82, "category": "MLOps & Cloud", "years": 1, "logo": "https://cdn-icons-png.flaticon.com/512/5968/5968412.png"},
            "Power BI": {"level": 85, "category": "Tools", "years": 1, "logo": "https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg"},
            "Git": {"level": 92, "category": "Tools", "years": 4, "logo": "https://cdn-icons-png.flaticon.com/512/4494/4494740.png"},
            "Streamlit": {"level": 90, "category": "Tools", "years": 2, "logo": "https://streamlit.io/images/brand/streamlit-mark-color.png"}
        },
        "soft": {
            "Problem Solving": 95,
            "Technical Communication": 90,
            "Teamwork": 88,
            "Project Management": 85,
            "Analytical Thinking": 92
        }
    }

@st.cache_data(ttl=Config.CACHE_TTL)
def load_experience_data() -> List[Dict]:
    """Charge les expériences professionnelles avec cache"""
    return [
        {
            "company": "Web4Jobs",
            "position": "AI Developer Intern",
            "period": "May – July 2025",
            "location": "Casablanca, Morocco",
            "description": "Optimisation de l'engagement utilisateur via des systèmes de recommandation.",
            "achievements": [
                "Engineered an adaptive recommendation engine (within the SOIPA system) for career guidance, increasing user engagement by 15% through personalized psychometric test paths.",
                "Integrated the recommendation engine into a user-facing web interface."
            ]
        },
        {
            "company": "SRM-CS",
            "position": "AI Engineer Intern",
            "period": "April – July 2025",
            "location": "Casablanca, Morocco",
            "description": "Développement et déploiement de solutions LLM et classification sémantique.",
            "achievements": [
                "Developed and containerized a Large Language Model (LLM) using Docker and fine-tuned transformer models (Mistral, DeepSeek) for automated text generation from client requests.",
                "Reduced average query processing time by 25% through LLM-based response automation.",
                "Designed a multi-label classification pipeline for semantic annotation of customer complaints, improving routing accuracy by 92%.",
                "Built a real-time monitoring dashboard (Power BI) to track model performance and drift."
            ]
        },
        {
            "company": "Galenica (Laboratoire Pharmaceutique)",
            "position": "Commercial Data Analyst Intern",
            "period": "Stage",
            "location": "Casablanca, Morocco",
            "description": "Leveraging data to optimize strategic decision-making.",
            "achievements": [
                "Design interactive dashboards and conduct performance analyses using Power BI and SQL Server.",
                "Automate processes to enhance operational efficiency.",
                "Contribute to the integration of artificial intelligence solutions."
            ]
        }
    ]

# ============================================
# COMPOSANTS UI (Design)
# ============================================
class UIComponents:
    """Composants d'interface réutilisables"""
    
    @staticmethod
    def tech_badge(name: str, logo_url: str = "") -> str:
        """Génère un badge technologique stylisé"""
        logo_html = f'<img src="{logo_url}" style="width: 16px; height: 16px; margin-right: 8px;">' if logo_url else ""
        return f"""
        <div style="
            display: inline-flex;
            align-items: center;
            background: rgba(0, 212, 255, 0.1);
            color: {Config.COLORS['accent']};
            padding: 5px 12px;
            border-radius: 20px;
            margin: 4px;
            border: 1px solid rgba(0, 212, 255, 0.3);
            font-size: 0.85em;
            font-weight: 500;
        ">
            {logo_html}{name}
        </div>
        """

    @staticmethod
    def skill_bar(name: str, level: int):
        """Affiche une barre de compétence avec animation CSS"""
        st.markdown(f"""
        <div style="margin-bottom: 15px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                <span style="color: {Config.COLORS['light']}; font-weight: 500;">{name}</span>
                <span style="color: {Config.COLORS['accent']};">{level}%</span>
            </div>
            <div style="background: rgba(255, 255, 255, 0.1); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="background: linear-gradient(90deg, {Config.COLORS['accent']}, #0099cc); width: {level}%; height: 100%; border-radius: 4px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# SECTIONS DE L'APPLICATION
# ============================================
def render_about_section():
    """Affiche la section ABOUT ME"""
    profile_data = load_profile_data()
    personal = profile_data["personal"]
    stats = profile_data["stats"]
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Photo de profil
        if os.path.exists(personal['photo']):
                       st.image(personal['photo'], width=200) # Changez 200 selon vos préférences

        else:
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="display: inline-block; padding: 5px; background: linear-gradient(45deg, {Config.COLORS['accent']}, #ffffff); border-radius: 15px;">
                    <img src="https://via.placeholder.com/300" style="width: 100%; border-radius: 10px; display: block;">
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Informations de contact
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.8); border-radius: 15px; padding: 20px; border: 1px solid rgba(0, 212, 255, 0.2); backdrop-filter: blur(10px);">
            <h4 style="color: {Config.COLORS['accent']}; margin-top: 0;">📍 Contact</h4>
            <p style="color: {Config.COLORS['light']}; margin-bottom: 5px;"><strong>Email:</strong> {personal['email']}</p>
            <p style="color: {Config.COLORS['light']}; margin-bottom: 5px;"><strong>Tel:</strong> {personal['phone']}</p>
            <p style="color: {Config.COLORS['light']}; margin-bottom: 5px;"><strong>Lieu:</strong> {personal['location']}</p>
            <hr style="border-color: rgba(0, 212, 255, 0.1);">
            <p style="color: {Config.COLORS['light']};">
                <strong style="color: {Config.COLORS['primary']};">🌐 Portfolio:</strong><br>
                <a href="https://github.com/Thekidmaroi" style="color: {Config.COLORS['accent']}; text-decoration: none;" target="_blank">github.com/Thekidmaroi</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"<h2 style='color: {Config.COLORS['primary']}; margin-top: 0;'>{personal['name']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color: {Config.COLORS['accent']};'>{personal['title']}</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.6); border-radius: 15px; padding: 25px; margin-top: 20px; border-left: 5px solid {Config.COLORS['accent']}; color: {Config.COLORS['light']}; line-height: 1.6;">
            {personal['summary']}
        </div>
        """, unsafe_allow_html=True)
        
        # Statistiques
        st.markdown(f"<h3 style='color: {Config.COLORS['primary']}; margin-top: 30px;'>📈 Mes Statistiques Data Science</h3>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown(f'<div style="background: rgba(0, 212, 255, 0.1); border-radius: 10px; padding: 20px; text-align: center; border: 1px solid rgba(0, 212, 255, 0.3);"><h1 style="color: {Config.COLORS["accent"]}; margin: 0;">{stats["projects"]}+</h1><p style="color: {Config.COLORS["light"]};">Projets</p></div>', unsafe_allow_html=True)
        with c2: st.markdown(f'<div style="background: rgba(0, 212, 255, 0.1); border-radius: 10px; padding: 20px; text-align: center; border: 1px solid rgba(0, 212, 255, 0.3);"><h1 style="color: {Config.COLORS["accent"]}; margin: 0;">{stats["years_exp"]}+</h1><p style="color: {Config.COLORS["light"]};">Années</p></div>', unsafe_allow_html=True)
        with c3: st.markdown(f'<div style="background: rgba(0, 212, 255, 0.1); border-radius: 10px; padding: 20px; text-align: center; border: 1px solid rgba(0, 212, 255, 0.3);"><h1 style="color: {Config.COLORS["accent"]}; margin: 0;">{stats["technologies"]}</h1><p style="color: {Config.COLORS["light"]};">Techs</p></div>', unsafe_allow_html=True)
        with c4: st.markdown(f'<div style="background: rgba(0, 212, 255, 0.1); border-radius: 10px; padding: 20px; text-align: center; border: 1px solid rgba(0, 212, 255, 0.3);"><h1 style="color: {Config.COLORS["accent"]}; margin: 0;">{stats["models"]}+</h1><p style="color: {Config.COLORS["light"]};">Modèles</p></div>', unsafe_allow_html=True)

def render_what_i_do_section():
    """Affiche la section WHAT I DO"""
    skills_data = load_skills_data()
    st.markdown(f"<h2 style='color: {Config.COLORS['primary']};'>🛠️ Expertise Technique & Stack</h2>", unsafe_allow_html=True)
    
    categories = {}
    for skill, data in skills_data["technical"].items():
        cat = data["category"]
        if cat not in categories: categories[cat] = []
        categories[cat].append((skill, data))
    
    cat_cols = st.columns(2)
    for idx, (category, skills) in enumerate(categories.items()):
        with cat_cols[idx % 2]:
            st.markdown(f"""
            <div style="background: rgba(15, 23, 42, 0.8); border-radius: 15px; padding: 25px; margin-bottom: 20px; border: 1px solid rgba(0, 212, 255, 0.2); backdrop-filter: blur(10px);">
                <h3 style="color: {Config.COLORS['accent']}; margin-top: 0;">{category}</h3>
                <div style="margin-top: 15px; display: flex; flex-wrap: wrap;">
                    {" ".join([UIComponents.tech_badge(s[0], s[1]["logo"]) for s in skills])}
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_experience_section():
    """Affiche la section MY EXPERIENCE"""
    experience_data = load_experience_data()
    st.markdown(f"<h2 style='color: {Config.COLORS['primary']};'>💼 Mon Parcours Professionnel</h2>", unsafe_allow_html=True)
    
    for exp in experience_data:
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.9); border-radius: 10px; padding: 20px; margin-bottom: 20px; border-left: 4px solid {Config.COLORS['accent']}; backdrop-filter: blur(10px);">
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <h3 style="color: {Config.COLORS['primary']}; margin: 0;">{exp['position']}</h3>
                    <h4 style="color: {Config.COLORS['accent']}; margin: 0;">{exp['company']}</h4>
                </div>
                <div style="color: {Config.COLORS['light']}; font-weight: bold;">{exp['period']}</div>
            </div>
            <p style="color: {Config.COLORS['light']}; margin: 10px 0;">{exp['description']}</p>
            <div style="color: {Config.COLORS['light']};">
                {"".join([f"<div style='margin: 5px 0;'>• {a}</div>" for a in exp['achievements']])}
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_projects_section():
    """Affiche la section MY PROJECTS"""
    projects = load_projects_data()
    st.markdown(f"<h2 style='color: {Config.COLORS['primary']};'>🚀 Mes Projets</h2>", unsafe_allow_html=True)
    for project in projects:
        with st.expander(f"{project['title']} - {project['category']}"):
            st.write(project['description'])
            st.markdown("**Technologies:** " + ", ".join(project['technologies']))
            st.link_button("GitHub", project['github'])

def render_research_section():
    """Affiche la section RESEARCH PROJECTS"""
    research = load_research_data()
    st.markdown(f"<h2 style='color: {Config.COLORS['primary']};'> Projets de Recherche & Publications</h2>", unsafe_allow_html=True)
    for item in research:
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.8); border-radius: 10px; padding: 20px; margin-bottom: 15px; border: 1px solid rgba(0, 212, 255, 0.1);">
            <h4 style="color: {Config.COLORS['accent']}; margin: 0;">{item['title']}</h4>
            <p style="color: {Config.COLORS['primary']}; font-style: italic; margin: 5px 0;">{item['journal']} - <strong>{item['status']}</strong></p>
            <p style="color: {Config.COLORS['light']};">{item['description']}</p>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Fonction principale"""
    st.set_page_config(page_title=Config.PAGE_TITLE, page_icon=Config.PAGE_ICON, layout=Config.LAYOUT)
    
    # Background Image CSS
    bg_img_path = "image de fond.png"
    if os.path.exists(bg_img_path):
        with open(bg_img_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{data}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: {Config.COLORS['overlay']};
            backdrop-filter: blur(80px);
            z-index: -1;
        }}
        </style>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <style>
    .main-title {{ font-size: 3.5em; font-weight: 800; color: {Config.COLORS['primary']}; text-align: center; margin-bottom: 10px; }}
    .main-subtitle {{ font-size: 1.2em; color: {Config.COLORS['accent']}; text-align: center; margin-bottom: 40px; letter-spacing: 4px; }}
    .stTabs [data-baseweb="tab"] {{ color: {Config.COLORS['light']}; font-weight: 600; }}
    .stTabs [aria-selected="true"] {{ color: {Config.COLORS['accent']} !important; border-bottom: 2px solid {Config.COLORS['accent']} !important; }}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="main-title">MY PORTFOLIO</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Data Science • Machine Learning • Artificial Intelligence</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["ABOUT ME", "WHAT I DO", "MY EXPERIENCE", "MY PROJECTS", "RESEARCH PROJECTS"])
    
    with tab1: render_about_section()
    with tab2: render_what_i_do_section()
    with tab3: render_experience_section()
    with tab4: render_projects_section()
    with tab5: render_research_section()
    
    # Footer
    profile_data = load_profile_data()
    social = profile_data["social"]
    st.markdown(f"""
    <div style="background: rgba(15, 23, 42, 0.95); border-radius: 15px; padding: 40px; margin-top: 50px; text-align: center; border: 1px solid rgba(0, 212, 255, 0.2);">
        <h3 style='color: {Config.COLORS['primary']};'>🔗 Connectons-nous</h3>
        <div style="display: flex; justify-content: center; gap: 20px; margin: 20px 0;">
            {" ".join([f'<a href="{d["url"]}" target="_blank"><img src="{d["icon"]}" width="40" style="filter: brightness(0) invert(1);"></a>' for p, d in social.items()])}
        </div>
        <p style="color: {Config.COLORS['light']};">© {datetime.now().year} Marwane Houngnon. Tous droits réservés.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()