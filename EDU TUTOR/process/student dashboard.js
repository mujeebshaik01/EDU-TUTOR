import React, { useState, useEffect } from 'react';
import { getStudentProgress, generateQuiz } from '../services/api';

const StudentDashboard = ({ user }) => {
  const [courses, setCourses] = useState([]);
  const [quiz, setQuiz] = useState(null);
  
  useEffect(() => {
    const loadData = async () => {
      const progress = await getStudentProgress(user.id);
      setCourses(progress.courses);
    };
    loadData();
  }, [user.id]);
  
  const handleGenerateQuiz = async (topic) => {
    const newQuiz = await generateQuiz(user.id, topic);
    setQuiz(newQuiz);
  };
  
  return (
    <div className="dashboard">
      <h2>My Learning Dashboard</h2>
      <div className="course-list">
        {courses.map(course => (
          <div key={course.id} className="course-card">
            <h3>{course.name}</h3>
            <button onClick={() => handleGenerateQuiz(course.currentTopic)}>
              Practice {course.currentTopic}
            </button>
          </div>
        ))}
      </div>
      {quiz && <QuizInterface quiz={quiz} />}
    </div>
  );
};