from rest_framework.throttling import UserRateThrottle


class user_throttle(UserRateThrottle):
    scope = "myuser"
