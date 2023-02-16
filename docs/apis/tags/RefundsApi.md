<a name="__pageTop"></a>
# zenkipay-api-client.fi.zenki.zenkipay.api.services.tags.refunds_api.RefundsApi

All URIs are relative to *https://api.zenki.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_refund_order**](#get_refund_order) | **get** /v1/pay/orders/{zenkiOrderId}/refunds/{zenkiRefundId} | Request refunds for an order
[**register_refund_order**](#register_refund_order) | **post** /v1/pay/orders/{zenkiOrderId}/refunds | Register of refunds for an order

# **get_refund_order**
<a name="get_refund_order"></a>
> Refund get_refund_order(zenki_order_idzenki_refund_idcontent_typeaccept)

Request refunds for an order

The refund is consulted by the order number.

### Example

* Bearer (ACCESS_TOKEN) Authentication (JWTAuth):
```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import refunds_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.refund import Refund
from zenkipay-api-client.fi.zenki.zenkipay.api.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.zenki.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = zenkipay-api-client.Configuration(
    host = "https://api.zenki.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ACCESS_TOKEN): JWTAuth
configuration = zenkipay-api-client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with zenkipay-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = refunds_api.RefundsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zenkiOrderId': "zenkiOrderId_example",
        'zenkiRefundId': "zenkiRefundId_example",
    }
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Request refunds for an order
        api_response = api_instance.get_refund_order(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling RefundsApi->get_refund_order: %s\n" % e)

    # example passing only optional values
    path_params = {
        'zenkiOrderId': "zenkiOrderId_example",
        'zenkiRefundId': "zenkiRefundId_example",
    }
    header_params = {
        'X-ZENKI-PLUGIN-ID': "4188918f7da1547d13e3",
        'Accept-Language': "en",
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Request refunds for an order
        api_response = api_instance.get_refund_order(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling RefundsApi->get_refund_order: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-ZENKI-PLUGIN-ID | XZENKIPLUGINIDSchema | | optional
Accept-Language | AcceptLanguageSchema | | optional
Content-Type | ContentTypeSchema | | 
Accept | AcceptSchema | | 

# XZENKIPLUGINIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AcceptLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zenkiOrderId | ZenkiOrderIdSchema | | 
zenkiRefundId | ZenkiRefundIdSchema | | 

# ZenkiOrderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ZenkiRefundIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#get_refund_order.ApiResponseFor201) | refund information.
400 | [ApiResponseFor400](#get_refund_order.ApiResponseFor400) | Expected repayment parameter.
403 | [ApiResponseFor403](#get_refund_order.ApiResponseFor403) | Access denied.
404 | [ApiResponseFor404](#get_refund_order.ApiResponseFor404) | Resource not found.
406 | [ApiResponseFor406](#get_refund_order.ApiResponseFor406) | Headers not accepted.
428 | [ApiResponseFor428](#get_refund_order.ApiResponseFor428) | Parameter name cannot be found.
500 | [ApiResponseFor500](#get_refund_order.ApiResponseFor500) | Internal Server Error.

#### get_refund_order.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Refund**](../../models/Refund.md) |  | 


#### get_refund_order.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_refund_order.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_refund_order.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_refund_order.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_refund_order.ApiResponseFor428
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor428ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor428ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_refund_order.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[JWTAuth](../../../README.md#JWTAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **register_refund_order**
<a name="register_refund_order"></a>
> Refund register_refund_order(zenki_order_idcontent_typeaccept)

Register of refunds for an order

One or more refunds are recorded by the order number.

### Example

* Bearer (ACCESS_TOKEN) Authentication (JWTAuth):
```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import refunds_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.request_refund import RequestRefund
from zenkipay-api-client.fi.zenki.zenkipay.api.model.refund import Refund
from zenkipay-api-client.fi.zenki.zenkipay.api.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.zenki.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = zenkipay-api-client.Configuration(
    host = "https://api.zenki.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ACCESS_TOKEN): JWTAuth
configuration = zenkipay-api-client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with zenkipay-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = refunds_api.RefundsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zenkiOrderId': "zenkiOrderId_example",
    }
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Register of refunds for an order
        api_response = api_instance.register_refund_order(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling RefundsApi->register_refund_order: %s\n" % e)

    # example passing only optional values
    path_params = {
        'zenkiOrderId': "zenkiOrderId_example",
    }
    header_params = {
        'X-ZENKI-PLUGIN-ID': "4188918f7da1547d13e3",
        'Accept-Language': "en",
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    body = RequestRefund(
        reason="Product without inventory.",
    )
    try:
        # Register of refunds for an order
        api_response = api_instance.register_refund_order(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling RefundsApi->register_refund_order: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestRefund**](../../models/RequestRefund.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-ZENKI-PLUGIN-ID | XZENKIPLUGINIDSchema | | optional
Accept-Language | AcceptLanguageSchema | | optional
Content-Type | ContentTypeSchema | | 
Accept | AcceptSchema | | 

# XZENKIPLUGINIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AcceptLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zenkiOrderId | ZenkiOrderIdSchema | | 

# ZenkiOrderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#register_refund_order.ApiResponseFor201) | Refund generated.
400 | [ApiResponseFor400](#register_refund_order.ApiResponseFor400) | Expected repayment parameter.
403 | [ApiResponseFor403](#register_refund_order.ApiResponseFor403) | Access denied.
404 | [ApiResponseFor404](#register_refund_order.ApiResponseFor404) | Resource not found.
406 | [ApiResponseFor406](#register_refund_order.ApiResponseFor406) | Headers not accepted.
428 | [ApiResponseFor428](#register_refund_order.ApiResponseFor428) | Parameter name cannot be found.
500 | [ApiResponseFor500](#register_refund_order.ApiResponseFor500) | Internal Server Error.

#### register_refund_order.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Refund**](../../models/Refund.md) |  | 


#### register_refund_order.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_refund_order.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_refund_order.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_refund_order.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_refund_order.ApiResponseFor428
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor428ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor428ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_refund_order.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[JWTAuth](../../../README.md#JWTAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

