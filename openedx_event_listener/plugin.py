



print("Hello, world! from openedx_event_listener app.")

def on_session_login_completed(user, **kwargs):
    print("Session login completed")




def on_course_created(course, **kwargs):
    print("Course created")


def on_certificate_created(certificate, **kwargs):
    print("Certificate created")



def on_certificate_awarded(certificate, **kwargs):
    print("Certificate awarded")


def on_course_enrollment_created(enrollment, **kwargs):
    print("Course enrollment created")
