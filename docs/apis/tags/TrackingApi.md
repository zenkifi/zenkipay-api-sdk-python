<a name="__pageTop"></a>
# zenkipay-api-client.fi.zenki.zenkipay.api.services.tags.tracking_api.TrackingApi

All URIs are relative to *https://api.zenki.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_event_tracking**](#add_event_tracking) | **patch** /v1/pay/orders/{zenkiOrderId}/tracking/{zenkiTrackId} | Shipping Status Update
[**register_tracking_orders**](#register_tracking_orders) | **post** /v1/pay/orders/{zenkiOrderId}/tracking | Registration number for tracking

# **add_event_tracking**
<a name="add_event_tracking"></a>
> TrackingEvents add_event_tracking(zenki_order_idzenki_track_idcontent_typeaccept)

Shipping Status Update

Based on the order id and the tracking id the delivery status is updated.

### Example

* Bearer (ACCESS_TOKEN) Authentication (JWTAuth):
```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import tracking_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.tracking_events import TrackingEvents
from zenkipay-api-client.fi.zenki.zenkipay.api.model.add_tracking_event import AddTrackingEvent
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
    api_instance = tracking_api.TrackingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zenkiOrderId': "zenkiOrderId_example",
        'zenkiTrackId': "zenkiTrackId_example",
    }
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Shipping Status Update
        api_response = api_instance.add_event_tracking(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling TrackingApi->add_event_tracking: %s\n" % e)

    # example passing only optional values
    path_params = {
        'zenkiOrderId': "zenkiOrderId_example",
        'zenkiTrackId': "zenkiTrackId_example",
    }
    header_params = {
        'X-ZENKI-PLUGIN-ID': "4188918f7da1547d13e3",
        'Accept-Language': "en",
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    body = AddTrackingEvent(
        status="FAILED",
        location="Sopitas street, no 304, San Jeronimo neighborhood",
        description="Invalid address.",
    )
    try:
        # Shipping Status Update
        api_response = api_instance.add_event_tracking(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling TrackingApi->add_event_tracking: %s\n" % e)
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
[**AddTrackingEvent**](../../models/AddTrackingEvent.md) |  | 


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
zenkiTrackId | ZenkiTrackIdSchema | | 

# ZenkiOrderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ZenkiTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#add_event_tracking.ApiResponseFor201) | Successful shipping status update.
400 | [ApiResponseFor400](#add_event_tracking.ApiResponseFor400) | Expected trace parameter.
403 | [ApiResponseFor403](#add_event_tracking.ApiResponseFor403) | Access denied.
404 | [ApiResponseFor404](#add_event_tracking.ApiResponseFor404) | Resource not found.
406 | [ApiResponseFor406](#add_event_tracking.ApiResponseFor406) | Headers not accepted.
428 | [ApiResponseFor428](#add_event_tracking.ApiResponseFor428) | Parameter name cannot be found.
500 | [ApiResponseFor500](#add_event_tracking.ApiResponseFor500) | Internal Server Error.

#### add_event_tracking.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TrackingEvents**](../../models/TrackingEvents.md) |  | 


#### add_event_tracking.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### add_event_tracking.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### add_event_tracking.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### add_event_tracking.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### add_event_tracking.ApiResponseFor428
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor428ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor428ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### add_event_tracking.ApiResponseFor500
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

# **register_tracking_orders**
<a name="register_tracking_orders"></a>
> Tracking register_tracking_orders(zenki_order_idcontent_typeaccept)

Registration number for tracking

One or more shipment tracking numbers are recorded for the order number.

### Example

* Bearer (ACCESS_TOKEN) Authentication (JWTAuth):
```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import tracking_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.add_tracking import AddTracking
from zenkipay-api-client.fi.zenki.zenkipay.api.model.tracking import Tracking
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
    api_instance = tracking_api.TrackingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zenkiOrderId': "zenkiOrderId_example",
    }
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Registration number for tracking
        api_response = api_instance.register_tracking_orders(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling TrackingApi->register_tracking_orders: %s\n" % e)

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
    body = AddTracking(
        courier_type="EXTERNAL",
        tracking_id="d65a558951d3",
        courier_name="Internal messaging - Brothers Shoe Store",
    )
    try:
        # Registration number for tracking
        api_response = api_instance.register_tracking_orders(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling TrackingApi->register_tracking_orders: %s\n" % e)
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
[**AddTracking**](../../models/AddTracking.md) |  | 


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
201 | [ApiResponseFor201](#register_tracking_orders.ApiResponseFor201) | Recorded tracking.
400 | [ApiResponseFor400](#register_tracking_orders.ApiResponseFor400) | Expected trace parameter.
403 | [ApiResponseFor403](#register_tracking_orders.ApiResponseFor403) | Access denied.
404 | [ApiResponseFor404](#register_tracking_orders.ApiResponseFor404) | Resource not found.
406 | [ApiResponseFor406](#register_tracking_orders.ApiResponseFor406) | Headers not accepted.
428 | [ApiResponseFor428](#register_tracking_orders.ApiResponseFor428) | Parameter name cannot be found.
500 | [ApiResponseFor500](#register_tracking_orders.ApiResponseFor500) | Internal Server Error.

#### register_tracking_orders.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Tracking**](../../models/Tracking.md) |  | 


#### register_tracking_orders.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_tracking_orders.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_tracking_orders.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_tracking_orders.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_tracking_orders.ApiResponseFor428
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor428ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor428ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### register_tracking_orders.ApiResponseFor500
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

