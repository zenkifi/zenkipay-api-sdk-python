# zenkipay-api-client.fi.zenki.zenkipay.api.model.merchant.Merchant

Merchant information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Merchant information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cryptoLovePercentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | Discount in percentage granted by the merchant to the buyer in his purchase for activating crypto love. | value must be a 64 bit float
**[escrowConfig](#escrowConfig)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Summary of the amount paid in crypto currency by the buyer. | 
**[integrationConfig](#integrationConfig)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Merchant integrations settings. | 
**[merchantInfo](#merchantInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | General information of the merchant. | 
**cryptoCurrencies** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**[cryptoAssets](#cryptoAssets)** | list, tuple,  | tuple,  | Supported crypto currencies list. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# merchantInfo

General information of the merchant.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | General information of the merchant. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**kycStatus** | str,  | str,  | State of the documentary process in which the merchant is located.  Possible values: * PENDING      - Indicates that you still need to send information or documents to complete your KYC process. * APPROVED     - The documentary registration process has been completed and the Zenki staff has authorized the business to operate. * REQUEST_INFO - Zenki Staff requested more information or change in trade documents. * REJECTED     - Zenki Staff definitively rejected the merchant request. | must be one of ["PENDING", "APPROVED", "REQUEST_INFO", "REJECTED", ] 
**accountType** | str,  | str,  | Merchant account type.  Possible values: * PERSONAL - Natural person with commercial activity. * ENTITY - Company with commercial activity | must be one of ["PERSONAL", "ENTITY", ] 
**integrationStatus** | str,  | str,  | Status of the integration process in merchant is located.  Possible values: * PENDING   - It indicates that the merchant has not yet concluded its technical integration process and is not yet in a productive environment. * COMPLETED - Indicates that the merchant has completed its technical integration process and is already in production or live. | must be one of ["PENDING", "COMPLETED", ] 
**commercialName** | str,  | str,  | Commercial name of the merchant that you registered when you created your Zenki account. | 
**legalName** | str,  | str,  | Merchant legal name that you register during the Zenki account activation process. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# integrationConfig

Merchant integrations settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Merchant integrations settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[plugins](#plugins)** | list, tuple,  | tuple,  | Configuration of each active plugin of the merchant. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# plugins

Configuration of each active plugin of the merchant.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Configuration of each active plugin of the merchant. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Configuration of an active plugin. | 

# items

Configuration of an active plugin.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Configuration of an active plugin. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clientId** | str,  | str,  | Active plugin key. | 
**name** | str,  | str,  | Active plugin name.  Posibles valores: * SCRIPT      - Integration through Zenkipay API. * WOOCOMMERCE - Integration through the WooCommerce plugin. * BIGCOMMERCE - Integration through the BigCommerce plugin. * MAGENTO     - Integration through the Magento plugin. * ECWID       - Integration through the ECWID plugin. * SHOPIFY     - Integration through the Shopify plugin. * VTEX        - Integration through the VTEX plugin. * ANGULAR     - Integration through the Angular Front-End library. * REACT       - Integration through the React Front-End library. * VUEJS       - Integration through the VUE JS Front-End library. * PRESTASHOP  - Integration through the Prestashop plugin. | must be one of ["SCRIPT", "WOOCOMMERCE", "BIGCOMMERCE", "MAGENTO", "ECWID", "SHOPIFY", "VTEX", "ANGULAR", "REACT", "VUEJS", "PRESTASHOP", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# escrowConfig

Summary of the amount paid in crypto currency by the buyer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Summary of the amount paid in crypto currency by the buyer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**blockchain** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**currency** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**orderType** | str,  | str,  | Indicates the model for the product delivery or service delivery.  Possible values: * WITH_CARRIER    - If a courier is going to be used for the shipment and delivery of the product or service. * WITHOUT_CARRIER - If a courier is not going to be used for the shipment and delivery of the product or service. * MIXED           - If a courier is going to be used to send part of the products or services and another part is delivered without using a courier. | [optional] must be one of ["WITH_CARRIER", "WITHOUT_CARRIER", "MIXED", ] 
**shopperNotification** | decimal.Decimal, int,  | decimal.Decimal,  | Number of hours to wait for the merchant to notify Zenki that they have delivered the services to the shopper. Time is expressed in hours. | [optional] value must be a 64 bit integer
**timeWaitToApproval** | decimal.Decimal, int,  | decimal.Decimal,  | Number of hours that Zenki will wait for confirmation from the buyer before approving the payment and releasing the funds to the merchant. Time is expressed in hours. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cryptoAssets

Supported crypto currencies list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Supported crypto currencies list. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Configuration for each cryptocurrency. | 

# items

Configuration for each cryptocurrency.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Configuration for each cryptocurrency. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**active** | bool,  | BoolClass,  | Indicates if the cryptocurrency is active or not. | 
**currency** | str,  | str,  | Supported currency identifier, see: https://developer.zenki.fi/global-v1/docs/zenkipay-recursos-catalogos-criptomonedas-soportadas | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

