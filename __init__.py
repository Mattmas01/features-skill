from mycroft import MycroftSkill, intent_file_handler


class Features(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('features.intent')
    def handle_features(self, message):
        self.speak_dialog('features')


def create_skill():
    return Features()

