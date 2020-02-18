class IceNER():


    def predict(self, text, original_text, pos=None):
        assert isinstance(text, str), "Invalid text for provided"
        if not isinstance(text, str):
            text = str(text, "utf-8")
        if self.serviceid == 'DEFAULT':
            return self.pre_defined_entity_model.predict(text, original_text, pos)
        else:
            return self.custom_entity_model.predict(text, original_text, pos)

    def load(self, file_name):
        self.custom_entity_model.load(file_name)