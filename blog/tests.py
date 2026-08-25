try:
    from django.test import TestCase  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover
    from unittest import TestCase

# Creating my tests here
