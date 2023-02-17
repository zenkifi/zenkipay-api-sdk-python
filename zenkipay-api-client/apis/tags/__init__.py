# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from zenkipay-api-client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUTHENTICATION_AND_AUTHORIZATION = "Authentication and authorization"
    MERCHANTS = "Merchants"
    ORDERS = "Orders"
    ESCROW = "Escrow"
    TRACKING = "Tracking"
    REFUNDS = "Refunds"
    WEBHOOKS = "Webhooks"
