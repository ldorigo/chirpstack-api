"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class RatePolicy(_RatePolicy, metaclass=_RatePolicyEnumTypeWrapper):
    pass
class _RatePolicy:
    V = typing.NewType('V', builtins.int)
class _RatePolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_RatePolicy.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    # Drop
    DROP = RatePolicy.V(0)
    # Mark
    MARK = RatePolicy.V(1)

# Drop
DROP = RatePolicy.V(0)
# Mark
MARK = RatePolicy.V(1)
global___RatePolicy = RatePolicy


class ServiceProfile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NETWORK_SERVER_ID_FIELD_NUMBER: builtins.int
    UL_RATE_FIELD_NUMBER: builtins.int
    UL_BUCKET_SIZE_FIELD_NUMBER: builtins.int
    UL_RATE_POLICY_FIELD_NUMBER: builtins.int
    DL_RATE_FIELD_NUMBER: builtins.int
    DL_BUCKET_SIZE_FIELD_NUMBER: builtins.int
    DL_RATE_POLICY_FIELD_NUMBER: builtins.int
    ADD_GW_METADATA_FIELD_NUMBER: builtins.int
    DEV_STATUS_REQ_FREQ_FIELD_NUMBER: builtins.int
    REPORT_DEV_STATUS_BATTERY_FIELD_NUMBER: builtins.int
    REPORT_DEV_STATUS_MARGIN_FIELD_NUMBER: builtins.int
    DR_MIN_FIELD_NUMBER: builtins.int
    DR_MAX_FIELD_NUMBER: builtins.int
    CHANNEL_MASK_FIELD_NUMBER: builtins.int
    PR_ALLOWED_FIELD_NUMBER: builtins.int
    HR_ALLOWED_FIELD_NUMBER: builtins.int
    RA_ALLOWED_FIELD_NUMBER: builtins.int
    NWK_GEO_LOC_FIELD_NUMBER: builtins.int
    TARGET_PER_FIELD_NUMBER: builtins.int
    MIN_GW_DIVERSITY_FIELD_NUMBER: builtins.int
    GWS_PRIVATE_FIELD_NUMBER: builtins.int
    # Service-profile ID (UUID string).
    # This will be automatically set on create.
    id: typing.Text = ...
    # Service-profile name.
    name: typing.Text = ...
    # Organization ID to which the service-profile is assigned.
    organization_id: builtins.int = ...
    # Network-server ID on which the service-profile is provisioned.
    network_server_id: builtins.int = ...
    # Token bucket filling rate, including ACKs (packet/h).
    ul_rate: builtins.int = ...
    # Token bucket burst size.
    ul_bucket_size: builtins.int = ...
    # Drop or mark when exceeding ULRate.
    ul_rate_policy: global___RatePolicy.V = ...
    # Token bucket filling rate, including ACKs (packet/h).
    dl_rate: builtins.int = ...
    # Token bucket burst size.
    dl_bucket_size: builtins.int = ...
    # Drop or mark when exceeding DLRate.
    dl_rate_policy: global___RatePolicy.V = ...
    # GW metadata (RSSI, SNR, GW geoloc., etc.) are added to the packet sent to AS.
    add_gw_metadata: builtins.bool = ...
    # Frequency to initiate an End-Device status request (request/day).
    dev_status_req_freq: builtins.int = ...
    # Report End-Device battery level to AS.
    report_dev_status_battery: builtins.bool = ...
    # Report End-Device margin to AS.
    report_dev_status_margin: builtins.bool = ...
    # Minimum allowed data rate. Used for ADR.
    dr_min: builtins.int = ...
    # Maximum allowed data rate. Used for ADR.
    dr_max: builtins.int = ...
    # Channel mask. sNS does not have to obey (i.e., informative).
    channel_mask: builtins.bytes = ...
    # Passive Roaming allowed.
    pr_allowed: builtins.bool = ...
    # Handover Roaming allowed.
    hr_allowed: builtins.bool = ...
    # Roaming Activation allowed.
    ra_allowed: builtins.bool = ...
    # Enable network geolocation service.
    nwk_geo_loc: builtins.bool = ...
    # Target Packet Error Rate.
    target_per: builtins.int = ...
    # Minimum number of receiving GWs (informative).
    min_gw_diversity: builtins.int = ...
    # Gateways under this service-profile are private.
    # This means that these gateways can only be used by devices under the
    # same service-profile.
    gws_private: builtins.bool = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        name : typing.Text = ...,
        organization_id : builtins.int = ...,
        network_server_id : builtins.int = ...,
        ul_rate : builtins.int = ...,
        ul_bucket_size : builtins.int = ...,
        ul_rate_policy : global___RatePolicy.V = ...,
        dl_rate : builtins.int = ...,
        dl_bucket_size : builtins.int = ...,
        dl_rate_policy : global___RatePolicy.V = ...,
        add_gw_metadata : builtins.bool = ...,
        dev_status_req_freq : builtins.int = ...,
        report_dev_status_battery : builtins.bool = ...,
        report_dev_status_margin : builtins.bool = ...,
        dr_min : builtins.int = ...,
        dr_max : builtins.int = ...,
        channel_mask : builtins.bytes = ...,
        pr_allowed : builtins.bool = ...,
        hr_allowed : builtins.bool = ...,
        ra_allowed : builtins.bool = ...,
        nwk_geo_loc : builtins.bool = ...,
        target_per : builtins.int = ...,
        min_gw_diversity : builtins.int = ...,
        gws_private : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"add_gw_metadata",b"add_gw_metadata",u"channel_mask",b"channel_mask",u"dev_status_req_freq",b"dev_status_req_freq",u"dl_bucket_size",b"dl_bucket_size",u"dl_rate",b"dl_rate",u"dl_rate_policy",b"dl_rate_policy",u"dr_max",b"dr_max",u"dr_min",b"dr_min",u"gws_private",b"gws_private",u"hr_allowed",b"hr_allowed",u"id",b"id",u"min_gw_diversity",b"min_gw_diversity",u"name",b"name",u"network_server_id",b"network_server_id",u"nwk_geo_loc",b"nwk_geo_loc",u"organization_id",b"organization_id",u"pr_allowed",b"pr_allowed",u"ra_allowed",b"ra_allowed",u"report_dev_status_battery",b"report_dev_status_battery",u"report_dev_status_margin",b"report_dev_status_margin",u"target_per",b"target_per",u"ul_bucket_size",b"ul_bucket_size",u"ul_rate",b"ul_rate",u"ul_rate_policy",b"ul_rate_policy"]) -> None: ...
global___ServiceProfile = ServiceProfile

class DeviceProfile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class TagsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NETWORK_SERVER_ID_FIELD_NUMBER: builtins.int
    SUPPORTS_CLASS_B_FIELD_NUMBER: builtins.int
    CLASS_B_TIMEOUT_FIELD_NUMBER: builtins.int
    PING_SLOT_PERIOD_FIELD_NUMBER: builtins.int
    PING_SLOT_DR_FIELD_NUMBER: builtins.int
    PING_SLOT_FREQ_FIELD_NUMBER: builtins.int
    SUPPORTS_CLASS_C_FIELD_NUMBER: builtins.int
    CLASS_C_TIMEOUT_FIELD_NUMBER: builtins.int
    MAC_VERSION_FIELD_NUMBER: builtins.int
    REG_PARAMS_REVISION_FIELD_NUMBER: builtins.int
    RX_DELAY_1_FIELD_NUMBER: builtins.int
    RX_DR_OFFSET_1_FIELD_NUMBER: builtins.int
    RX_DATARATE_2_FIELD_NUMBER: builtins.int
    RX_FREQ_2_FIELD_NUMBER: builtins.int
    FACTORY_PRESET_FREQS_FIELD_NUMBER: builtins.int
    MAX_EIRP_FIELD_NUMBER: builtins.int
    MAX_DUTY_CYCLE_FIELD_NUMBER: builtins.int
    SUPPORTS_JOIN_FIELD_NUMBER: builtins.int
    RF_REGION_FIELD_NUMBER: builtins.int
    SUPPORTS_32BIT_F_CNT_FIELD_NUMBER: builtins.int
    PAYLOAD_CODEC_FIELD_NUMBER: builtins.int
    PAYLOAD_ENCODER_SCRIPT_FIELD_NUMBER: builtins.int
    PAYLOAD_DECODER_SCRIPT_FIELD_NUMBER: builtins.int
    GEOLOC_BUFFER_TTL_FIELD_NUMBER: builtins.int
    GEOLOC_MIN_BUFFER_SIZE_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    UPLINK_INTERVAL_FIELD_NUMBER: builtins.int
    ADR_ALGORITHM_ID_FIELD_NUMBER: builtins.int
    # Device-profile ID (UUID string).
    id: typing.Text = ...
    # Device-profile name.
    name: typing.Text = ...
    # Organization ID to which the service-profile is assigned.
    organization_id: builtins.int = ...
    # Network-server ID on which the service-profile is provisioned.
    network_server_id: builtins.int = ...
    # End-Device supports Class B.
    supports_class_b: builtins.bool = ...
    # Maximum delay for the End-Device to answer a MAC request or a confirmed DL frame (mandatory if class B mode supported).
    class_b_timeout: builtins.int = ...
    # Mandatory if class B mode supported.
    ping_slot_period: builtins.int = ...
    # Mandatory if class B mode supported.
    ping_slot_dr: builtins.int = ...
    # Mandatory if class B mode supported.
    ping_slot_freq: builtins.int = ...
    # End-Device supports Class C.
    supports_class_c: builtins.bool = ...
    # Maximum delay for the End-Device to answer a MAC request or a confirmed DL frame (mandatory if class C mode supported).
    class_c_timeout: builtins.int = ...
    # Version of the LoRaWAN supported by the End-Device.
    mac_version: typing.Text = ...
    # Revision of the Regional Parameters document supported by the End-Device.
    reg_params_revision: typing.Text = ...
    # Class A RX1 delay (mandatory for ABP).
    rx_delay_1: builtins.int = ...
    # RX1 data rate offset (mandatory for ABP).
    rx_dr_offset_1: builtins.int = ...
    # RX2 data rate (mandatory for ABP).
    rx_datarate_2: builtins.int = ...
    # RX2 channel frequency (mandatory for ABP).
    rx_freq_2: builtins.int = ...
    # List of factory-preset frequencies (mandatory for ABP).
    @property
    def factory_preset_freqs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Maximum EIRP supported by the End-Device.
    max_eirp: builtins.int = ...
    # Maximum duty cycle supported by the End-Device.
    max_duty_cycle: builtins.int = ...
    # End-Device supports Join (OTAA) or not (ABP).
    supports_join: builtins.bool = ...
    # RF region name.
    rf_region: typing.Text = ...
    # End-Device uses 32bit FCnt (mandatory for LoRaWAN 1.0 End-Device).
    supports_32bit_f_cnt: builtins.bool = ...
    # Payload codec.
    # Leave blank to disable the codec feature.
    payload_codec: typing.Text = ...
    # Payload encoder script.
    # Depending the codec, it is possible to provide a script which implements
    # the encoder function.
    payload_encoder_script: typing.Text = ...
    # Payload decoder script.
    # Depending the codec, it is possible to provide a script which implements
    # the decoder function.
    payload_decoder_script: typing.Text = ...
    # Geolocation buffer TTL (in seconds).
    # When > 0, uplink RX meta-data will be stored in a buffer so that
    # the meta-data of multiple uplinks can be used for geolocation.
    geoloc_buffer_ttl: builtins.int = ...
    # Geolocation minimum buffer size.
    # When > 0, geolocation will only be performed when the buffer has
    # at least the given size.
    geoloc_min_buffer_size: builtins.int = ...
    # User defined tags.
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    # Uplink interval.
    # This defines the expected uplink interval which the device uses for
    # communication. When the uplink interval has expired and no uplink has
    # been received, the device is considered inactive.
    @property
    def uplink_interval(self) -> google.protobuf.duration_pb2.Duration: ...
    # ADR algorithm ID.
    # In case this is left blank, or is configured to a non-existing ADR
    # algorithm (plugin), then it falls back to 'default'.
    adr_algorithm_id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        name : typing.Text = ...,
        organization_id : builtins.int = ...,
        network_server_id : builtins.int = ...,
        supports_class_b : builtins.bool = ...,
        class_b_timeout : builtins.int = ...,
        ping_slot_period : builtins.int = ...,
        ping_slot_dr : builtins.int = ...,
        ping_slot_freq : builtins.int = ...,
        supports_class_c : builtins.bool = ...,
        class_c_timeout : builtins.int = ...,
        mac_version : typing.Text = ...,
        reg_params_revision : typing.Text = ...,
        rx_delay_1 : builtins.int = ...,
        rx_dr_offset_1 : builtins.int = ...,
        rx_datarate_2 : builtins.int = ...,
        rx_freq_2 : builtins.int = ...,
        factory_preset_freqs : typing.Optional[typing.Iterable[builtins.int]] = ...,
        max_eirp : builtins.int = ...,
        max_duty_cycle : builtins.int = ...,
        supports_join : builtins.bool = ...,
        rf_region : typing.Text = ...,
        supports_32bit_f_cnt : builtins.bool = ...,
        payload_codec : typing.Text = ...,
        payload_encoder_script : typing.Text = ...,
        payload_decoder_script : typing.Text = ...,
        geoloc_buffer_ttl : builtins.int = ...,
        geoloc_min_buffer_size : builtins.int = ...,
        tags : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        uplink_interval : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        adr_algorithm_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"uplink_interval",b"uplink_interval"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"adr_algorithm_id",b"adr_algorithm_id",u"class_b_timeout",b"class_b_timeout",u"class_c_timeout",b"class_c_timeout",u"factory_preset_freqs",b"factory_preset_freqs",u"geoloc_buffer_ttl",b"geoloc_buffer_ttl",u"geoloc_min_buffer_size",b"geoloc_min_buffer_size",u"id",b"id",u"mac_version",b"mac_version",u"max_duty_cycle",b"max_duty_cycle",u"max_eirp",b"max_eirp",u"name",b"name",u"network_server_id",b"network_server_id",u"organization_id",b"organization_id",u"payload_codec",b"payload_codec",u"payload_decoder_script",b"payload_decoder_script",u"payload_encoder_script",b"payload_encoder_script",u"ping_slot_dr",b"ping_slot_dr",u"ping_slot_freq",b"ping_slot_freq",u"ping_slot_period",b"ping_slot_period",u"reg_params_revision",b"reg_params_revision",u"rf_region",b"rf_region",u"rx_datarate_2",b"rx_datarate_2",u"rx_delay_1",b"rx_delay_1",u"rx_dr_offset_1",b"rx_dr_offset_1",u"rx_freq_2",b"rx_freq_2",u"supports_32bit_f_cnt",b"supports_32bit_f_cnt",u"supports_class_b",b"supports_class_b",u"supports_class_c",b"supports_class_c",u"supports_join",b"supports_join",u"tags",b"tags",u"uplink_interval",b"uplink_interval"]) -> None: ...
global___DeviceProfile = DeviceProfile
