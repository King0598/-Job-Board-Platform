def upload_resume_path(instance, filename):
    return f'resumes/user_{instance.user.id}/{filename}'