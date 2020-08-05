import json


class Context:
    app_images_folder = "images/"
    is_gui = False

    @classmethod
    def serialize(cls):
        attributes = [
            (attr, getattr(cls, attr))
            for attr in dir(cls)
            if (
                not callable(getattr(cls, attr)) and not attr.startswith("__")
            )
        ]
        return json.dumps(attributes)

    @classmethod
    def deserialize(cls, json_data):
        data = json.loads(json_data)
        for field, value in data:
            setattr(cls, field, value)
