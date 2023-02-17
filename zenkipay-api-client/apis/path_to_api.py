import typing_extensions

from zenkipay-api-client.paths import PathValues
from zenkipay-api-client.apis.paths.v1_oauth_tokens import V1OauthTokens
from zenkipay-api-client.apis.paths.v1_pay_me import V1PayMe
from zenkipay-api-client.apis.paths.v1_pay_orders import V1PayOrders
from zenkipay-api-client.apis.paths.v1_pay_orders_zenki_order_id import V1PayOrdersZenkiOrderId
from zenkipay-api-client.apis.paths.v1_pay_escrow_zenki_order_id_fulfillments import V1PayEscrowZenkiOrderIdFulfillments
from zenkipay-api-client.apis.paths.v1_pay_orders_zenki_order_id_tracking import V1PayOrdersZenkiOrderIdTracking
from zenkipay-api-client.apis.paths.v1_pay_orders_zenki_order_id_tracking_zenki_track_id import V1PayOrdersZenkiOrderIdTrackingZenkiTrackId
from zenkipay-api-client.apis.paths.v1_pay_orders_zenki_order_id_refunds import V1PayOrdersZenkiOrderIdRefunds
from zenkipay-api-client.apis.paths.v1_pay_orders_zenki_order_id_refunds_zenki_refund_id import V1PayOrdersZenkiOrderIdRefundsZenkiRefundId
from zenkipay-api-client.apis.paths.url_merchant import URLMERCHANT

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_OAUTH_TOKENS: V1OauthTokens,
        PathValues.V1_PAY_ME: V1PayMe,
        PathValues.V1_PAY_ORDERS: V1PayOrders,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID: V1PayOrdersZenkiOrderId,
        PathValues.V1_PAY_ESCROW_ZENKI_ORDER_ID_FULFILLMENTS: V1PayEscrowZenkiOrderIdFulfillments,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID_TRACKING: V1PayOrdersZenkiOrderIdTracking,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID_TRACKING_ZENKI_TRACK_ID: V1PayOrdersZenkiOrderIdTrackingZenkiTrackId,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID_REFUNDS: V1PayOrdersZenkiOrderIdRefunds,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID_REFUNDS_ZENKI_REFUND_ID: V1PayOrdersZenkiOrderIdRefundsZenkiRefundId,
        PathValues.URL_MERCHANT: URLMERCHANT,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_OAUTH_TOKENS: V1OauthTokens,
        PathValues.V1_PAY_ME: V1PayMe,
        PathValues.V1_PAY_ORDERS: V1PayOrders,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID: V1PayOrdersZenkiOrderId,
        PathValues.V1_PAY_ESCROW_ZENKI_ORDER_ID_FULFILLMENTS: V1PayEscrowZenkiOrderIdFulfillments,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID_TRACKING: V1PayOrdersZenkiOrderIdTracking,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID_TRACKING_ZENKI_TRACK_ID: V1PayOrdersZenkiOrderIdTrackingZenkiTrackId,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID_REFUNDS: V1PayOrdersZenkiOrderIdRefunds,
        PathValues.V1_PAY_ORDERS_ZENKI_ORDER_ID_REFUNDS_ZENKI_REFUND_ID: V1PayOrdersZenkiOrderIdRefundsZenkiRefundId,
        PathValues.URL_MERCHANT: URLMERCHANT,
    }
)
