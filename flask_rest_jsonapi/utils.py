# -*- coding: utf-8 -*-

from datetime import datetime
from uuid import UUID

from flask import json, current_app


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, UUID):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def json_dumps(obj, cls=JSONEncoder):
    try:
        sort_keys = current_app.config.get('JSON_SORT_KEYS')

    except Exception:
        sort_keys = False

    return json.dumps(obj, cls=cls, sort_keys=sort_keys)
