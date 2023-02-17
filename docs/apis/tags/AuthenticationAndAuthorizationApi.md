<a name="__pageTop"></a>
# zenkipay-api-client.fi.zenki.zenkipay.api.services.tags.authentication_and_authorization_api.AuthenticationAndAuthorizationApi

All URIs are relative to *https://api.zenki.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](#create_token) | **post** /v1/oauth/tokens | Create an authentication token in Zenki

# **create_token**
<a name="create_token"></a>
> TokenOAuth2 create_token(content_typeaccept)

Create an authentication token in Zenki

This request must be sent each time it is required to generate a token to consume Zenki services.

### Example

```python
import zenkipay-api-client
from zenkipay-api-client.fi.zenki.zenkipay.api.services.tags import authentication_and_authorization_api
from zenkipay-api-client.fi.zenki.zenkipay.api.model.token_o_auth2 import TokenOAuth2
from zenkipay-api-client.fi.zenki.zenkipay.api.model.request_token_o_auth2 import RequestTokenOAuth2
from zenkipay-api-client.fi.zenki.zenkipay.api.model.authentication_error_response import AuthenticationErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.zenki.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = zenkipay-api-client.Configuration(
    host = "https://api.zenki.fi"
)

# Enter a context with an instance of the API client
with zenkipay-api-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_and_authorization_api.AuthenticationAndAuthorizationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    try:
        # Create an authentication token in Zenki
        api_response = api_instance.create_token(
            header_params=header_params,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling AuthenticationAndAuthorizationApi->create_token: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    body = RequestTokenOAuth2(
        client_id="4188918f7da1547d13e3",
        client_secret="4ed3872fccacc77ce842",
        grant_type="client_credentials",
    )
    try:
        # Create an authentication token in Zenki
        api_response = api_instance.create_token(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except zenkipay-api-client.ApiException as e:
        print("Exception when calling AuthenticationAndAuthorizationApi->create_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTokenOAuth2**](../../models/RequestTokenOAuth2.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | 
Accept | AcceptSchema | | 

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
200 | [ApiResponseFor200](#create_token.ApiResponseFor200) | Token created successfully.
400 | [ApiResponseFor400](#create_token.ApiResponseFor400) | Token creation failed, please review the details and try again.
500 | [ApiResponseFor500](#create_token.ApiResponseFor500) | Unexpected error creating auth token, contact Zenki support team at support@zenki.fi

#### create_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TokenOAuth2**](../../models/TokenOAuth2.md) |  | 


#### create_token.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationErrorResponse**](../../models/AuthenticationErrorResponse.md) |  | 


#### create_token.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthenticationErrorResponse**](../../models/AuthenticationErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

