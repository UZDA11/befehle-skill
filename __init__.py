from mycroft import MycroftSkill, intent_file_handler


class Befehle(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('befehle.intent')
    def handle_befehle(self, message):
        self.speak_dialog('befehle')


def create_skill():
    return Befehle()

