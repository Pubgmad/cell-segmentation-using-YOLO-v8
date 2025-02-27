from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys

try:
    a=2/0
    print(a)

except Exception as e:
    raise AppException(e,sys)


