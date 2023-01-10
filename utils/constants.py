import os, sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')