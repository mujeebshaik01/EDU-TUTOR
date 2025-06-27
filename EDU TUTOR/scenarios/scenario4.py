def sync_classroom_courses():
    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/classroom.courses.readonly"])
    service = build("classroom", "v1", credentials=creds)
    courses = service.courses().list().execute().get("courses", [])
    return [{"id": c["id"], "name": c["name"], "section": c.get("section", "")} for c in courses]

synced_courses = sync_classroom_courses()
for course in synced_courses:
    print(f"Synced: {course['name']} - {course['section']}")