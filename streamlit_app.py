# steamlit_app.py
import streamlit as st
import random
import json
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="EduTutor - Interactive Learning Platform",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .subject-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .quiz-question {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .correct-answer {
        color: green;
        font-weight: bold;
    }
    .incorrect-answer {
        color: red;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

class EduTutor:
    def __init__(self):
        self.subjects = {
            "Mathematics": {
                "topics": ["Algebra", "Geometry", "Calculus", "Statistics"],
                "description": "Learn mathematical concepts and problem-solving"
            },
            "Science": {
                "topics": ["Physics", "Chemistry", "Biology", "Earth Science"],
                "description": "Explore the wonders of science"
            },
            "Programming": {
                "topics": ["Python", "Web Development", "Data Structures", "Algorithms"],
                "description": "Master coding skills and computational thinking"
            },
            "Languages": {
                "topics": ["English", "Spanish", "French", "Grammar"],
                "description": "Improve language skills and communication"
            }
        }
        
        self.quiz_data = self._load_quiz_data()
        self.user_progress = {}

    def _load_quiz_data(self):
        return {
            "Mathematics": [
                {
                    "question": "What is the value of π (pi) approximately?",
                    "options": ["3.14", "2.71", "1.61", "4.13"],
                    "correct": 0,
                    "explanation": "π is approximately 3.14 and represents the ratio of a circle's circumference to its diameter."
                },
                {
                    "question": "Solve for x: 2x + 5 = 15",
                    "options": ["x = 5", "x = 10", "x = 7.5", "x = 3"],
                    "correct": 0,
                    "explanation": "Subtract 5 from both sides: 2x = 10, then divide by 2: x = 5"
                }
            ],
            "Science": [
                {
                    "question": "What is the chemical symbol for gold?",
                    "options": ["Go", "Gd", "Au", "Ag"],
                    "correct": 2,
                    "explanation": "Au comes from the Latin word 'aurum' meaning gold."
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                    "correct": 1,
                    "explanation": "Mars appears red due to iron oxide (rust) on its surface."
                }
            ],
            "Programming": [
                {
                    "question": "What does HTML stand for?",
                    "options": [
                        "Hyper Text Markup Language",
                        "High Tech Modern Language",
                        "Hyper Transfer Markup Language",
                        "Home Tool Markup Language"
                    ],
                    "correct": 0,
                    "explanation": "HTML is the standard markup language for creating web pages."
                },
                {
                    "question": "Which of these is a Python data type?",
                    "options": ["String", "Integer", "List", "All of the above"],
                    "correct": 3,
                    "explanation": "Python has several built-in data types including strings, integers, and lists."
                }
            ],
            "Languages": [
                {
                    "question": "What is the past tense of 'go'?",
                    "options": ["goed", "went", "gone", "going"],
                    "correct": 1,
                    "explanation": "The past tense of 'go' is 'went'."
                },
                {
                    "question": "How do you say 'hello' in Spanish?",
                    "options": ["Bonjour", "Hola", "Ciao", "Hallo"],
                    "correct": 1,
                    "explanation": "'Hola' is Spanish for 'hello'."
                }
            ]
        }

    def display_welcome(self):
        st.markdown('<div class="main-header">📚 EduTutor - Interactive Learning Platform</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write("""
            ### Welcome to Your Personal Learning Assistant!
            
            EduTutor helps you learn various subjects through interactive lessons, 
            quizzes, and personalized progress tracking.
            
            **Features:**
            - 📖 Interactive lessons in multiple subjects
            - 🧠 Knowledge quizzes with instant feedback
            - 📊 Progress tracking and analytics
            - 🎯 Personalized learning paths
            """)
        
        with col2:
            st.image("https://cdn.pixabay.com/photo/2016/01/19/17/53/books-1150053_960_720.jpg", 
                    use_column_width=True)

    def display_subject_selection(self):
        st.header("🎯 Choose Your Learning Path")
        
        cols = st.columns(2)
        for i, (subject, info) in enumerate(self.subjects.items()):
            with cols[i % 2]:
                with st.container():
                    st.markdown(f'<div class="subject-card">', unsafe_allow_html=True)
                    st.subheader(f"📘 {subject}")
                    st.write(f"**Topics:** {', '.join(info['topics'])}")
                    st.write(info['description'])
                    
                    if st.button(f"Start Learning {subject}", key=f"btn_{subject}"):
                        st.session_state.current_subject = subject
                        st.session_state.current_topic = info['topics'][0]
                        st.session_state.page = "learning"
                    st.markdown('</div>', unsafe_allow_html=True)

    def display_learning_interface(self):
        subject = st.session_state.current_subject
        topic = st.session_state.current_topic
        
        st.header(f"📖 Learning: {subject} - {topic}")
        
        # Back button
        if st.button("← Back to Subjects"):
            st.session_state.page = "subjects"
            st.rerun()
        
        # Topic selection
        topics = self.subjects[subject]["topics"]
        selected_topic = st.selectbox("Select Topic:", topics, index=topics.index(topic))
        st.session_state.current_topic = selected_topic
        
        # Display learning content based on subject and topic
        self._display_learning_content(subject, selected_topic)
        
        # Quiz section
        st.header("🧠 Test Your Knowledge")
        if subject in self.quiz_data:
            self._display_quiz(subject)

    def _display_learning_content(self, subject, topic):
        content = {
            "Mathematics": {
                "Algebra": """
                ## Algebra Basics
                
                **Variables and Expressions:**
                - Variables represent unknown values (x, y, z)
                - Expressions combine variables and numbers
                - Example: 2x + 3y - 5
                
                **Solving Equations:**
                - Isolate the variable on one side
                - Perform the same operation on both sides
                - Example: 3x + 7 = 19 → 3x = 12 → x = 4
                """,
                "Geometry": """
                ## Geometry Fundamentals
                
                **Basic Shapes:**
                - Points, lines, and angles
                - Triangles, circles, polygons
                
                **Formulas:**
                - Area of circle: πr²
                - Pythagorean theorem: a² + b² = c²
                """
            },
            "Science": {
                "Physics": """
                ## Physics Introduction
                
                **Laws of Motion:**
                - Newton's First Law: Objects at rest stay at rest
                - Newton's Second Law: F = ma
                - Newton's Third Law: Action and reaction
                """,
                "Chemistry": """
                ## Chemistry Basics
                
                **Elements and Compounds:**
                - Elements are pure substances (Oxygen, Gold)
                - Compounds are combinations of elements (H₂O, CO₂)
                """
            }
        }
        
        if subject in content and topic in content[subject]:
            st.markdown(content[subject][topic])
        else:
            st.info(f"Learning content for {topic} is coming soon! In the meantime, try the quiz below.")

    def _display_quiz(self, subject):
        questions = self.quiz_data[subject]
        
        if 'quiz_answers' not in st.session_state:
            st.session_state.quiz_answers = {}
        
        for i, q in enumerate(questions):
            st.markdown(f'<div class="quiz-question">Q{i+1}: {q["question"]}</div>', unsafe_allow_html=True)
            
            # Display options as buttons
            selected = st.radio(f"Select your answer for Q{i+1}:", 
                               q["options"], 
                               key=f"quiz_{subject}_{i}")
            
            # Check answer when user selects
            if selected:
                st.session_state.quiz_answers[f"{subject}_{i}"] = selected
                correct_answer = q["options"][q["correct"]]
                
                if selected == correct_answer:
                    st.markdown(f'<div class="correct-answer">✅ Correct! {q["explanation"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="incorrect-answer">❌ Incorrect. The correct answer is: {correct_answer}</div>', unsafe_allow_html=True)
                    st.write(f"**Explanation:** {q['explanation']}")

    def display_progress_tracking(self):
        st.header("📊 Your Learning Progress")
        
        # Mock progress data
        progress_data = {
            "Mathematics": 75,
            "Science": 60,
            "Programming": 85,
            "Languages": 45
        }
        
        for subject, progress in progress_data.items():
            st.write(f"**{subject}**")
            st.progress(progress / 100)
            st.write(f"Completion: {progress}%")
            st.write("---")

    def display_user_profile(self):
        st.sidebar.header("👤 User Profile")
        
        # Initialize session state for user info
        if 'user_name' not in st.session_state:
            st.session_state.user_name = "Student"
        if 'user_level' not in st.session_state:
            st.session_state.user_level = "Beginner"
        
        st.sidebar.text_input("Your Name", value=st.session_state.user_name, key="name_input")
        st.sidebar.selectbox("Learning Level", 
                           ["Beginner", "Intermediate", "Advanced"], 
                           key="level_select")
        
        st.sidebar.write("---")
        st.sidebar.write(f"**Current Level:** {st.session_state.user_level}")
        st.sidebar.write("**Member since:** Today!")

def main():
    # Initialize EduTutor
    tutor = EduTutor()
    
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = "welcome"
    if 'current_subject' not in st.session_state:
        st.session_state.current_subject = "Mathematics"
    if 'current_topic' not in st.session_state:
        st.session_state.current_topic = "Algebra"
    
    # Display user profile in sidebar
    tutor.display_user_profile()
    
    # Navigation
    st.sidebar.header("🎯 Navigation")
    page_options = ["Welcome", "Subjects", "Progress Tracking"]
    selected_page = st.sidebar.selectbox("Go to:", page_options)
    
    # Map selection to session state
    page_mapping = {
        "Welcome": "welcome",
        "Subjects": "subjects", 
        "Progress Tracking": "progress"
    }
    
    if st.sidebar.button("Apply Navigation"):
        st.session_state.page = page_mapping[selected_page]
        st.rerun()
    
    # Display current page
    if st.session_state.page == "welcome":
        tutor.display_welcome()
        
        col1, col2, col3 = st.columns(3)
        with col2:
            if st.button("Start Learning Now!", use_container_width=True):
                st.session_state.page = "subjects"
                st.rerun()
    
    elif st.session_state.page == "subjects":
        tutor.display_subject_selection()
    
    elif st.session_state.page == "learning":
        tutor.display_learning_interface()
    
    elif st.session_state.page == "progress":
        tutor.display_progress_tracking()

    # Footer
    st.sidebar.write("---")
    st.sidebar.info("EduTutor v1.0 • Making learning fun and interactive!")

if __name__ == "__main__":
    main()
