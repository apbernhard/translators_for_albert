# -*- coding: utf-8 -*-

"""
Translator plugin using py-translators
"""

from albert import *
from translators import translate_text, get_languages
from locale import getdefaultlocale
from time import sleep
import os

md_iid = '1.0'
md_version = "0.1"
md_name = "translators"
md_description = "Translate sentences using translators"
md_lib_dependencies = "translators==5.8.7"

LANGUAGES = get_languages()
class Plugin(TriggerQueryHandler):

    def id(self):
        return md_id

    def name(self):
        return md_name

    def description(self):
        return md_description

    def defaultTrigger(self):
        return "trans "

    def synopsis(self):
        return "[[src] dest] text"

    def initialize(self):
        self.icon = [os.path.dirname(__file__)+"/translators_logo.png"]
        self.lang = getdefaultlocale()[0][0:2]

    def handleTriggerQuery(self, query):
        stripped = query.string.strip()
        if stripped:
            for number in range(50):
                sleep(0.01)
                if not query.isValid:
                    return
            
            # Todo: implement search engine selector
            src = None
            dest, text = self.lang, stripped
            splits = text.split(maxsplit=1)
            if 1 < len(splits) and splits[0] in LANGUAGES:
                dest, text = splits[0], splits[1]
                splits = text.split(maxsplit=1)

                if 1 < len(splits) and splits[0] in LANGUAGES:
                    src = dest
                    dest, text = splits[0], splits[1]

            if src:
                translation = translate_text(text, from_language=src, to_language=dest)
            else:
                translation = translate_text(text, to_language=dest)

            query.add(Item(
                id=md_id,
                text=translation,
                subtext=f'From {src} to {dest}: {translation}',
                icon=self.icon,
                actions = [Action("copy", "Copy result to clipboard",
                                  lambda t=translation: setClipboardText(t))]
            ))
