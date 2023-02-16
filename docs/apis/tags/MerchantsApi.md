<a name="__pageTop"></a>
# zenkipay-api-client.fi.zenki.zenkipay.api.services.tags.merchants_api.MerchantsApi

All URIs are relative to *https://api.zenki.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_merchant_info**](#get_merchant_info) | **get** /v1/pay/me | Merchant information

# **get_merchant_info**
<a name="get_merchant_info"></a>
> Merchant get_merchant_info(content_typeaccept)

Merchant information

The current configuration of the merchnat is obtained.

### Example

* Bearer (ACCESS_TOKEN) Authentication (JWTAuth):
```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import merchants_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.merchant import Merchant
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
    api_instance = merchants_api.MerchantsApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Merchant information
        api_response = api_instance.get_merchant_info(
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling MerchantsApi->get_merchant_info: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-ZENKI-PLUGIN-ID': "4188918f7da1547d13e3",
        'Accept-Language': "en",
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Merchant information
        api_response = api_instance.get_merchant_info(
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling MerchantsApi->get_merchant_info: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_merchant_info.ApiResponseFor200) | Obtain merchnat information.
400 | [ApiResponseFor400](#get_merchant_info.ApiResponseFor400) | Parámetro de comercio esperado.
403 | [ApiResponseFor403](#get_merchant_info.ApiResponseFor403) | Access denied.
404 | [ApiResponseFor404](#get_merchant_info.ApiResponseFor404) | Resource not found.
406 | [ApiResponseFor406](#get_merchant_info.ApiResponseFor406) | Headers not accepted.
428 | [ApiResponseFor428](#get_merchant_info.ApiResponseFor428) | Parameter name cannot be found.
500 | [ApiResponseFor500](#get_merchant_info.ApiResponseFor500) | Internal Server Error.

#### get_merchant_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Merchant**](../../models/Merchant.md) |  | 


#### get_merchant_info.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_merchant_info.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_merchant_info.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_merchant_info.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_merchant_info.ApiResponseFor428
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor428ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor428ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_merchant_info.ApiResponseFor500
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

