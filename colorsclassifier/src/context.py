import json


class Context:
    """
    This class holds information about the current context.
    Yes, this is used for having "global variables". Maybe
    not that pretty but hey, it works.
    """
    app_images_folder = "images/"
    is_gui = False

    @classmethod
    def serialize(cls):
        """
        Serialize the Context class arguments.
        :return: JSON string of the arguments and their value.
        """
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
        """
        Deserialize a JSON string representing the Context class arguments.
        :param json_data: JSON string of the arguments and their value.
        """
        data = json.loads(json_data)
        for field, value in data:
            setattr(cls, field, value)
