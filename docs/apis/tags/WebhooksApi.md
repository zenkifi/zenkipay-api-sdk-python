<a name="__pageTop"></a>
# zenkipay-api-client.fi.zenki.zenkipay.api.services.tags.webhooks_api.WebhooksApi

All URIs are relative to *https://api.zenki.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_event**](#send_event) | **post** /URL_MERCHANT | Event notifications for merchant

# **send_event**
<a name="send_event"></a>
> send_event(svix_idsvix_timestampsvix_signaturecontent_type)

Event notifications for merchant

Service that allows different events to be sent to the merchant.

### Example

```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import webhooks_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.webhook import Webhook
from pprint import pprint
# Defining the host is optional and defaults to https://api.zenki.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = zenkipay-api-client.Configuration(
    host = "https://api.zenki.fi"
)

# Enter a context with an instance of the API client
with zenkipay-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhooks_api.WebhooksApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Svix-Id': "msg_2HYAP5mNDMxY0LurmzrPvGYJTdq",
        'Svix-Timestamp': "1668451615",
        'Svix-Signature': "v1,HNHAxGk8b5lX2xC1uVUQy6AXgmPKrfNV4I+yENBC4Fk=",
        'Content-Type': "application/json",
    }
    try:
        # Event notifications for merchant
        api_response = api_instance.send_event(
            header_params=header_params,
        )
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling WebhooksApi->send_event: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Svix-Id': "msg_2HYAP5mNDMxY0LurmzrPvGYJTdq",
        'Svix-Timestamp': "1668451615",
        'Svix-Signature': "v1,HNHAxGk8b5lX2xC1uVUQy6AXgmPKrfNV4I+yENBC4Fk=",
        'Content-Type': "application/json",
    }
    body = Webhook(
        event_type="order.pay",
        flat_data="{\"version\":\"v1.1.0\",\"zenkiOrderId\":\"f325da2b8e3f476caa07e039406e72f0\",\"orderId\":\"f3359498592b\",\"cartId\":\"96a17044f0e3\",\"type\":\"MIXED\",\"countryCodeIso2\":\"MX\",\"status\":\"PENDING\",\"createdAt\":1667353629,\"shopper\":{\"id\":\"f3359498592b\",\"name\":\"Juanito\",\"phone\":\"442536789\",\"email\":\"juanito@gmail.com\"},\"breakdown\":{\"currencyCodeIso3\":\"USD\",\"totalItemsAmount\":200,\"shipmentAmount\":50,\"subtotalAmount\":250,\"taxesAmount\":10,\"localTaxesAmount\":1.6,\"importCosts\":0,\"discountAmount\":0,\"additionalCharges\":{\"donation\":1.1234},\"grandTotalAmount\":262.7234},\"paymentInfo\":{\"exchangeRate\":{\"from\":\"MXN\",\"to\":\"USD\",\"value\":20,\"amount\":50,\"timestamp\":1667353629},\"cryptoLove\":{\"discountPercentage\":1,\"discountAmount\":0.5,\"finalAmount\":49.5,\"currency\":\"USD\"},\"cryptoPayment\":{\"amount\":\"0.038282960887513325\",\"currency\":\"ETH\",\"blockchain\":\"BSC\",\"transactionHash\":\"0xee8a3a5eb2a972785b7a56320682bbb843c29409c60dec2d25dbd3eaff91cf26\",\"networkScanUrl\":\"https://etherscan.io/tx/0x3e86fd3c50dbf8e050124e28f33392ce4f4278a925d7c472b3e7ab12af0da115\"}},\"settlementInfo\":{\"cryptoSettlement\":{\"finalAmount\":\"49.4\",\"currency\":\"USDC\"}},\"items\":[{\"externalId\":\"e40dbc7450f6\",\"quantity\":2,\"price\":10.33,\"name\":\"Libreta\",\"description\":\"Libretaderayas\",\"type\":\"WITH_CARRIER\",\"thumbnailUrl\":\"https://cdn.tshirts.boutique/wp-content/uploads/2022/07/12213723/12100-105.jpg\",\"metadata\":{\"size\":\"L\",\"color\":\"red\"}}],\"metadata\":{\"trackingId\":\"5514a95b0882\"},\"dispute\":{\"status\":\"OPEN\",\"createdAt\":1667353629,\"resolutionRequestType\":\"REQUEST_CONCILIATED\",\"resolutionRequestAt\":1667353629},\"claim\":{\"reason\":\"Seacaboelinventario\",\"status\":\"OPEN\",\"createdAt\":1667353629},\"_links\":{\"refund\":{\"href\":\"https://api.zenki.fi/v1/pay/orders/f325da2b8e3f476caa07e039406e72f0/refunds/e40dbc7450f6\"}}}",
    )
    try:
        # Event notifications for merchant
        api_response = api_instance.send_event(
            header_params=header_params,
            body=body,
        )
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling WebhooksApi->send_event: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Webhook**](../../models/Webhook.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Svix-Id | SvixIdSchema | | 
Svix-Timestamp | SvixTimestampSchema | | 
Svix-Signature | SvixSignatureSchema | | 
Content-Type | ContentTypeSchema | | 

# SvixIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SvixTimestampSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SvixSignatureSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#send_event.ApiResponseFor200) | Event received by the merchant.
500 | [ApiResponseFor500](#send_event.ApiResponseFor500) | Internal Server Error.

#### send_event.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### send_event.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

