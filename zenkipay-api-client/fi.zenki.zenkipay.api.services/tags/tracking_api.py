# coding: utf-8

"""
    Zenkipay API

    Definition of technical specification of the product; Zenkipay is a gateway cryptocurrency payment system that allows merchant's to receive payments on their e-commerce portals. Unlike other platforms, Zenkipay ensures customer satisfaction through its payment process. guarantee deposit (delivered product and expected quality) to settle payment to the merchant, thus avoiding the loss of client assets due to online scams.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@zenki.fi
    Generated by: https://openapi-generator.tech
"""

from zenkipay-api-client.paths.v1_pay_orders_zenki_order_id_tracking_zenki_track_id.patch import AddEventTracking
from zenkipay-api-client.paths.v1_pay_orders_zenki_order_id_tracking.post import RegisterTrackingOrders


class TrackingApi(
    AddEventTracking,
    RegisterTrackingOrders,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
