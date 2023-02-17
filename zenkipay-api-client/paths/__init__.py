# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from zenkipay-api-client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_OAUTH_TOKENS = "/v1/oauth/tokens"
    V1_PAY_ME = "/v1/pay/me"
    V1_PAY_ORDERS = "/v1/pay/orders"
    V1_PAY_ORDERS_ZENKI_ORDER_ID = "/v1/pay/orders/{zenkiOrderId}"
    V1_PAY_ESCROW_ZENKI_ORDER_ID_FULFILLMENTS = "/v1/pay/escrow/{zenkiOrderId}/fulfillments"
    V1_PAY_ORDERS_ZENKI_ORDER_ID_TRACKING = "/v1/pay/orders/{zenkiOrderId}/tracking"
    V1_PAY_ORDERS_ZENKI_ORDER_ID_TRACKING_ZENKI_TRACK_ID = "/v1/pay/orders/{zenkiOrderId}/tracking/{zenkiTrackId}"
    V1_PAY_ORDERS_ZENKI_ORDER_ID_REFUNDS = "/v1/pay/orders/{zenkiOrderId}/refunds"
    V1_PAY_ORDERS_ZENKI_ORDER_ID_REFUNDS_ZENKI_REFUND_ID = "/v1/pay/orders/{zenkiOrderId}/refunds/{zenkiRefundId}"
    URL_MERCHANT = "/URL_MERCHANT"
