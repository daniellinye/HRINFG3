from i18n.locale import en, nl
class Localize(object):

    def __init__(self):
        self.current_lang = 'nl'
        self.langs = {'en':en.lang, 'nl':nl.lang}
        self.lang = self.langs[self.current_lang]


    def load(self, lang):
        self.current_lang = lang
        self.lang = self.langs[self.current_lang]
        return self

    def translate(self, key):
        return self.lang[key]
