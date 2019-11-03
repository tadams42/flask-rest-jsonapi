# -*- coding: utf-8 -*-

from datetime import datetime
from uuid import UUID

from flask import current_app

_has_rapidjson = False

try:
    import rapidjson as json
    _has_rapidjson = True

except ImportError:
    import json

    class JSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, UUID):
                return str(obj)
            return json.JSONEncoder.default(self, obj)


# def json_dumps(obj, cls=JSONEncoder):
def json_dumps(obj):
    try:
        sort_keys = current_app.config.get('JSON_SORT_KEYS')

    except Exception:
        sort_keys = False

    if _has_rapidjson:
        return json.dumps(
            obj,
            sort_keys=sort_keys,
            number_mode=json.NM_DECIMAL,
            datetime_mode=json.DM_ISO8601,
            uuid_mode=json.UM_CANONICAL
        )

    else:
        return json.dumps(obj, sort_keys=sort_keys, cls=JSONEncoder)
