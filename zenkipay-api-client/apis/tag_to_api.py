import typing_extensions

from zenkipay-api-client.apis.tags import TagValues
from zenkipay-api-client.apis.tags.authentication_and_authorization_api import AuthenticationAndAuthorizationApi
from zenkipay-api-client.apis.tags.merchants_api import MerchantsApi
from zenkipay-api-client.apis.tags.orders_api import OrdersApi
from zenkipay-api-client.apis.tags.escrow_api import EscrowApi
from zenkipay-api-client.apis.tags.tracking_api import TrackingApi
from zenkipay-api-client.apis.tags.refunds_api import RefundsApi
from zenkipay-api-client.apis.tags.webhooks_api import WebhooksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION_AND_AUTHORIZATION: AuthenticationAndAuthorizationApi,
        TagValues.MERCHANTS: MerchantsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.ESCROW: EscrowApi,
        TagValues.TRACKING: TrackingApi,
        TagValues.REFUNDS: RefundsApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION_AND_AUTHORIZATION: AuthenticationAndAuthorizationApi,
        TagValues.MERCHANTS: MerchantsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.ESCROW: EscrowApi,
        TagValues.TRACKING: TrackingApi,
        TagValues.REFUNDS: RefundsApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)
