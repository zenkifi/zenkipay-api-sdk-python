# zenkipay-api-client.fi.zenki.zenkipay.api.model.webhook.Webhook

Base structure of the notification that the merchant will receive, this notification will handle different types of events for its processing. The content of the message will be in string format so that it can be interpreted according to the type of event received by the merchant from Zenkipay.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Base structure of the notification that the merchant will receive, this notification will handle different types of events for its processing. The content of the message will be in string format so that it can be interpreted according to the type of event received by the merchant from Zenkipay. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**flatData** | str,  | str,  | Event data.  Possible values: * The Order object is to be received when the order.pay event is notified. | 
**eventType** | str,  | str,  | Set of events that the merchant can receive.  Possible values: * order.pay    - Event notification when an order has been successfully paid by the buyer. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

