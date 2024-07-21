from django.conf import settings

VALID_METHOD_NAMES = getattr(
    settings,
    "REQUEST_VALID_METHOD_NAMES",
    ("get", "post", "put", "delete", "head", "options", "trace"),
)

ONLY_ERRORS = getattr(settings, "REQUEST_ONLY_ERRORS", False)
IGNORE_AJAX = getattr(settings, "REQUEST_IGNORE_AJAX", False)
IGNORE_IP = getattr(settings, "REQUEST_IGNORE_IP", tuple())
LOG_IP = getattr(settings, "REQUEST_LOG_IP", True)
IP_DUMMY = getattr(settings, "REQUEST_IP_DUMMY", "1.1.1.1")
ANONYMOUS_IP = getattr(settings, "REQUEST_ANONYMOUS_IP", False)
LOG_USER = getattr(settings, "REQUEST_LOG_USER", True)
IGNORE_USERNAME = getattr(settings, "REQUEST_IGNORE_USERNAME", tuple())
IGNORE_PATHS = getattr(settings, "REQUEST_IGNORE_PATHS", tuple())
IGNORE_USER_AGENTS = getattr(settings, "REQUEST_IGNORE_USER_AGENTS", tuple())

TRAFFIC_MODULES = getattr(
    settings,
    "REQUEST_TRAFFIC_MODULES",
    (
        "django_request_ahmb.request.traffic.UniqueVisitor",
        "django_request_ahmb.request.traffic.UniqueVisit",
        "django_request_ahmb.request.traffic.Hit",
    ),
)

PLUGINS = getattr(
    settings,
    "REQUEST_PLUGINS",
    (
        "django_request_ahmb.request.plugins.TrafficInformation",
        "django_request_ahmb.request.plugins.LatestRequests",
        "django_request_ahmb.request.plugins.TopPaths",
        "django_request_ahmb.request.plugins.TopErrorPaths",
        "django_request_ahmb.request.plugins.TopReferrers",
        "django_request_ahmb.request.plugins.TopSearchPhrases",
        "django_request_ahmb.request.plugins.TopBrowsers",
    ),
)
