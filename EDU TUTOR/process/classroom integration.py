from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from config import GOOGLE_CLIENT_CONFIG

class GoogleClassroomSync:
    def __init__(self, user_token):
        self.credentials = Credentials(
            token=user_token,
            **GOOGLE_CLIENT_CONFIG
        )
        self.service = build('classroom', 'v1', credentials=self.credentials)
    
    def get_courses(self):
        results = self.service.courses().list().execute()
        return results.get('courses', [])
    
    def get_course_work(self, course_id):
        return self.service.courses().courseWork().list(
            courseId=course_id
        ).execute()