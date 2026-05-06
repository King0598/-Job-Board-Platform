from rest_framework.exceptions import APIException

class ApplicationClosed(APIException):
    status_code = 400
    default_detail = 'Job application is closed.'
    default_code = 'application_closed'

class AlreadyApplied(APIException):
    status_code = 400
    default_detail = 'You have already applied for this job.'
    default_code = 'already_applied'