validation_schemes = {
            "settings": {
                "type": "object",
                "properties": {
                    "minimize": {"type": "boolean"},
                    "startup": {"type": "boolean"},
                    "notification": {"type": "string"},
                    "refresh": {"type": "string"}
                }
            },
            "shrine": {
                "type": "object",
                "properties": {
                    "shrine_perk1": {"type": "string"},
                    "shrine_perk2": {"type": "string"},
                    "shrine_perk3": {"type": "string"},
                    "shrine_perk4": {"type": "string"},
                    "download_date": {"type": "string"},
                    "refresh_date": {"type": "string"}
                }
            },
            "perks": {
                "type": "object",
                "properties": {
                    "perks_list": {"type": "array"}
                }
            },
            "user_perks": {
                "type": "object",
                "properties": {
                    "perks_list": {"type": "array"}
                }
            }
        }