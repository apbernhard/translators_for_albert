"""
Translator plugin using py-translators. Syntax consists of optional parameter (`;;`) and text block (`Text...`)

Syntax Examples: 
* all parameters: `engine;source;destination Text...`
* only source and destination language: `;source;destination Text...`
* Only destination language: `;;destination Text...`
* Only text: Text...

default values:
* engine: `bing`
* source: `auto`
* destination: `en`.

"""

from albert import *
from translators import translate_text, get_languages, translators_pool
from locale import getdefaultlocale
from time import sleep
import os

md_iid = '1.0'
md_version = "0.1"
md_name = "Translators"
md_license = 'BSD-3'
md_description = "Translate sentences using the python translators plugin"
md_url = "https://github.com/apbernhard/translators_for_albert/"
md_lib_dependencies = "translators==5.8.7"
md_maintainers = "@apbernhard"

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
        return "[engine;source_language;destination_language] text"

    def initialize(self):
        self.icon = [os.path.dirname(__file__)+"/translators_logo.png"]
        self.lang = getdefaultlocale()[0][0:2]

    def handleTriggerQuery(self, query):
        stripped = query.string.strip()

        # wait for query entry and delay output
        if stripped:
            for number in range(50):
                sleep(0.01)
                if not query.isValid:
                    return
            
            # explication of standard parameters as defined for translators.translate_text()
            engine = 'bing'
            src = 'auto'
            dest = 'en'

            # check for parameters
            if ';' in stripped:
                parameters, text = stripped.split(maxsplit=1)
                engine_temp, src_temp, dest_temp = parameters.split(";")
                if engine_temp:
                    engine = engine_temp
                if src_temp:
                    src = src_temp
                if dest_temp:
                    dest = dest_temp
            else:
                text = stripped

            # entry showing translation result
            translation = translate_text(text, translator=engine, from_language=src, to_language=dest)
            query.add(Item(
                id=md_id,
                text=translation,
                subtext=f'Translated from {src} to {dest} using {engine}',
                icon=self.icon,
                actions = [Action("copy", "Copy result to clipboard",
                                  lambda t=translation: setClipboardText(t))]
            ))

            # Todo: resolve workaround; for now shows the available languages per translation engine
            engine_languages = "\n".join(get_languages(engine).keys())
            query.add(Item(
                id=md_id,
                text=engine_languages,
                subtext=f'available languages on {engine}',
                icon=self.icon,
                actions = [Action("copy", "Copy result to clipboard",
                                  lambda t=engine_languages: setClipboardText(t))]
            ))