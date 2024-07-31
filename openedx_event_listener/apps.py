from django.apps import AppConfig
class MyAppConfig(AppConfig):
    name = 'openedx_event_listener' # name of the module

    plugin_app = {
        'signals_config': {
        # Here you can add all the events you want to listen to in your lms 
            'lms.djangoapp': {
                'relative_path': 'plugin', # relative path to the plugin directory 
                'receivers': [{
                    'receiver_func_name': 'on_session_login_completed', # name of the receiver function
                    'signal_path': 'openedx_events.learning.signals.SESSION_LOGIN_COMPLETED', # path to the signal
                },
                {
                    'receiver_func_name': 'on_course_enrollment_created',
                    'signal_path': 'openedx_events.learning.signals.COURSE_ENROLLMENT_CREATED',
                },
                {
                    'receiver_func_name': 'on_certificate_created',
                    'signal_path': 'openedx_events.learning.signals.CERTIFICATE_CREATED',
                },
                {
                    'receiver_func_name': 'on_certificate_awarded',
                    'signal_path': 'openedx_events.learning.signals.PROGRAM_CERTIFICATE_AWARDED',
                },
                
                
                ],
            },
        # Here you can add all the events you want to listen to in your cms
            "cms.djangoapp": {
                "relative_path": "plugin",
                "receivers": [
                    {
                        "receiver_func_name": "on_course_created",
                        "signal_path": "openedx_events.content_authoring.signals.COURSE_CREATED",
                    },
                ],
            }
        }
    }