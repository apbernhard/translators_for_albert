# translators plugin for [Albert launcher](https://github.com/albertlauncher/albert)

Albert plugin, translates sentences using the python plugin [translators](https://github.com/UlionTse/translators/tree/master#supported-translation-services).

Syntax consists of optional parameter (`;;`) and text block (`Text...`).

Syntax Examples:

* all parameters: `engine;source;destination Text...`
* only source and destination language: `;source;destination Text...`
* Only destination language: `;;destination Text...`
* Only text: `Text...`

default values:

* engine: `bing`
* source: `auto`
* destination: `en`
