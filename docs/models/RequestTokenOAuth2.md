# zenkipay-api-client.fi.zenki.zenkipay.api.model.request_token_o_auth2.RequestTokenOAuth2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clientId** | str,  | str,  | Client ID Key must be obtained from the Zenkipay portal in the security section. | 
**clientSecret** | str,  | str,  | Client Secret Key in Zenkipay must be obtained from the Zenkipay portal in the security section. | 
**grantType** | str,  | str,  | Permission type, for all operations carried out in the Zenkipay API from the merchant&#x27;s server, it is required to send the value &#x27;client_credentials&#x27; as grant type. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

