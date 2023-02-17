<a name="__pageTop"></a>
# zenkipay-api-client.fi.zenki.zenkipay.api.services.tags.escrow_api.EscrowApi

All URIs are relative to *https://api.zenki.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_escrow**](#update_escrow) | **patch** /v1/pay/escrow/{zenkiOrderId}/fulfillments | Escrow update

# **update_escrow**
<a name="update_escrow"></a>
> Order update_escrow(zenki_order_idcontent_typeaccept)

Escrow update

Service in charge of updating the escrow for orders without tracking.

### Example

* Bearer (ACCESS_TOKEN) Authentication (JWTAuth):
```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import escrow_api
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
    api_instance = escrow_api.EscrowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zenkiOrderId': "zenkiOrderId_example",
    }
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Escrow update
        api_response = api_instance.update_escrow(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling EscrowApi->update_escrow: %s\n" % e)

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
        # Escrow update
        api_response = api_instance.update_escrow(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling EscrowApi->update_escrow: %s\n" % e)
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
201 | [ApiResponseFor201](#update_escrow.ApiResponseFor201) | Escrow updated.
400 | [ApiResponseFor400](#update_escrow.ApiResponseFor400) | Expected order parameter.
403 | [ApiResponseFor403](#update_escrow.ApiResponseFor403) | Access denied.
404 | [ApiResponseFor404](#update_escrow.ApiResponseFor404) | Resource not found.
406 | [ApiResponseFor406](#update_escrow.ApiResponseFor406) | Headers not accepted.
428 | [ApiResponseFor428](#update_escrow.ApiResponseFor428) | Parameter name cannot be found.
500 | [ApiResponseFor500](#update_escrow.ApiResponseFor500) | Internal Server Error.

#### update_escrow.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationHaljson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationHaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**Order**](../../models/Order.md) |  | 


#### update_escrow.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_escrow.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_escrow.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_escrow.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_escrow.ApiResponseFor428
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor428ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor428ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_escrow.ApiResponseFor500
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

