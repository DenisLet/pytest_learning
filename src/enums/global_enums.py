from enum import Enum

class GlobalErrorMessages(Enum):
    WRGONG_STATUS_CODE = 'Received status code is not equal to exp'
    WRGONG_ELEMENT_COUNT = 'Number of item is not equal to expected'
