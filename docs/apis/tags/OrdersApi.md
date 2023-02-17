<a name="__pageTop"></a>
# zenkipay-api-client.fi.zenki.zenkipay.api.services.tags.orders_api.OrdersApi

All URIs are relative to *https://api.zenki.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](#create_order) | **post** /v1/pay/orders | Payment order registration
[**get_order**](#get_order) | **get** /v1/pay/orders/{zenkiOrderId} | Order information
[**update_order**](#update_order) | **patch** /v1/pay/orders/{zenkiOrderId} | Order update for payment

# **create_order**
<a name="create_order"></a>
> Order create_order(content_typeaccept)

Payment order registration

Service that allows registering a payment order and associating it with a merchant.

### Example

* Bearer (ACCESS_TOKEN) Authentication (JWTAuth):
```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import orders_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.order import Order
from zenkipay-api-client.fi.zenki.zenkipay.api.model.create_order import CreateOrder
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
    api_instance = orders_api.OrdersApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Payment order registration
        api_response = api_instance.create_order(
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling OrdersApi->create_order: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-ZENKI-PLUGIN-ID': "4188918f7da1547d13e3",
        'Accept-Language': "en",
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    body = CreateOrder(
        version="v1.0.0",
        order_id="f3359498592b",
        cart_id="96a17044f0e3",
        type="MIXED",
        country_code_iso2="MX",
        shopper=Shopper(
            id="f3359498592b",
            name="Juanito",
            phone="442536789",
            email="juanito@gmail.com",
        ),
        breakdown=Breakdown(
            currency_code_iso3="USD",
            total_items_amount=200,
            shipment_amount=50,
            subtotal_amount=250,
            taxes_amount=10,
            local_taxes_amount=1.6,
            import_costs=0,
            discount_amount=0,
            additional_charges=dict(
                "key": "key_example",
            ),
            grand_total_amount=261.6,
        ),
        items=[
            Item(
                external_id="e40dbc7450f6",
                quantity=2,
                unit_price=100,
                name="Libreta",
                description="Striped notebook",
                type="WITH_CARRIER",
                thumbnail_url="https://cdn.tshirts.boutique/wp-content/uploads/2022/07/12213723/12100-105.jpg",
                metadata=dict(
                    "key": "key_example",
                ),
            )
        ],
        metadata=dict(
            "key": "key_example",
        ),
    )
    try:
        # Payment order registration
        api_response = api_instance.create_order(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling OrdersApi->create_order: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/hal+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateOrder**](../../models/CreateOrder.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_order.ApiResponseFor201) | Order created.
400 | [ApiResponseFor400](#create_order.ApiResponseFor400) | Expected order parameter.
403 | [ApiResponseFor403](#create_order.ApiResponseFor403) | Access denied.
404 | [ApiResponseFor404](#create_order.ApiResponseFor404) | Resource not found.
406 | [ApiResponseFor406](#create_order.ApiResponseFor406) | Headers not accepted.
428 | [ApiResponseFor428](#create_order.ApiResponseFor428) | Parameter name cannot be found.
500 | [ApiResponseFor500](#create_order.ApiResponseFor500) | Internal Server Error.

#### create_order.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationHaljson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**Order**](../../models/Order.md) |  | 


#### create_order.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_order.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_order.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_order.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_order.ApiResponseFor428
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor428ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor428ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_order.ApiResponseFor500
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

# **get_order**
<a name="get_order"></a>
> Order get_order(zenki_order_idcontent_typeaccept)

Order information

Order information is obtained based on the Zenkipay order id.

### Example

* Bearer (ACCESS_TOKEN) Authentication (JWTAuth):
```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import orders_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.order import Order
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
    api_instance = orders_api.OrdersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zenkiOrderId': "zenkiOrderId_example",
    }
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Order information
        api_response = api_instance.get_order(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)

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
    try:
        # Order information
        api_response = api_instance.get_order(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/hal+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
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

# ZenkiOrderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_order.ApiResponseFor200) | Get order by id.
400 | [ApiResponseFor400](#get_order.ApiResponseFor400) | Expected order parameter.
403 | [ApiResponseFor403](#get_order.ApiResponseFor403) | Access denied.
404 | [ApiResponseFor404](#get_order.ApiResponseFor404) | Resource not found.
406 | [ApiResponseFor406](#get_order.ApiResponseFor406) | Headers not accepted.
428 | [ApiResponseFor428](#get_order.ApiResponseFor428) | Parameter name cannot be found.
500 | [ApiResponseFor500](#get_order.ApiResponseFor500) | Internal Server Error.

#### get_order.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationHaljson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**Order**](../../models/Order.md) |  | 


#### get_order.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_order.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_order.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_order.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_order.ApiResponseFor428
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor428ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor428ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_order.ApiResponseFor500
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

# **update_order**
<a name="update_order"></a>
> Order update_order(zenki_order_idcontent_typeaccept)

Order update for payment

Service that allows updating a payment order.

### Example

* Bearer (ACCESS_TOKEN) Authentication (JWTAuth):
```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import orders_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.order import Order
from zenkipay-api-client.fi.zenki.zenkipay.api.model.update_order import UpdateOrder
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
    api_instance = orders_api.OrdersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zenkiOrderId': "3a89e750101049108eb884e3d2e1d7ba",
    }
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Order update for payment
        api_response = api_instance.update_order(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling OrdersApi->update_order: %s\n" % e)

    # example passing only optional values
    path_params = {
        'zenkiOrderId': "3a89e750101049108eb884e3d2e1d7ba",
    }
    header_params = {
        'X-ZENKI-PLUGIN-ID': "4188918f7da1547d13e3",
        'Accept-Language': "en",
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    body = UpdateOrder(
        order_id="f3359498592b",
        cart_id="96a17044f0e3",
        shopper=dict(
            id="f3359498592b",
        ),
        metadata=dict(
            "key": "key_example",
        ),
    )
    try:
        # Order update for payment
        api_response = api_instance.update_order(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling OrdersApi->update_order: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/hal+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateOrder**](../../models/UpdateOrder.md) |  | 


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
201 | [ApiResponseFor201](#update_order.ApiResponseFor201) | updated order.
400 | [ApiResponseFor400](#update_order.ApiResponseFor400) | Expected order parameter.
403 | [ApiResponseFor403](#update_order.ApiResponseFor403) | Access denied.
404 | [ApiResponseFor404](#update_order.ApiResponseFor404) | Resource not found.
406 | [ApiResponseFor406](#update_order.ApiResponseFor406) | Headers not accepted.
428 | [ApiResponseFor428](#update_order.ApiResponseFor428) | Parameter name cannot be found.
500 | [ApiResponseFor500](#update_order.ApiResponseFor500) | Internal Server Error.

#### update_order.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationHaljson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**Order**](../../models/Order.md) |  | 


#### update_order.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_order.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_order.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_order.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_order.ApiResponseFor428
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor428ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor428ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_order.ApiResponseFor500
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

