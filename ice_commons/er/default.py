from ice_commons.er.ice_ner import IceNER

def get_supported_engines():
    return [
        "ICE"
    ]

def get_default_ner():
    return IceNER(serviceid="DEFAULT")