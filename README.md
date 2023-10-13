# translators plugin for [Albert launcher](https://github.com/albertlauncher/albert)

### Description
Albert plugin for translating sentences using the python plugin [translators](https://github.com/UlionTse/translators/tree/master#supported-translation-services).

### Syntax

**trans** [translation engine;source language;destination language] Text...

|parameter|default value|
|-|-|
|translation engine|`bing`|
|source language|`auto`|
|destination language|`en`|

### Examples
|query|explanation|
|---|---|
|`trans google;de;it Text...`|translate from German to Italian using Google translate engine|
|`trans ;de;it Text...`|translate from German to Italian using default engine|
| `trans ;;it Text...`|translate from auto-detected language to Italian |
| `trans ;de; Text...`|translate from German to default destination language (en) |
|`trans ;; Text...`|translate auto-detected language to default destination language using default engine |
|`trans Text...`|(same as above) translate auto-detected language to default destination language using default engine |

### Additional Information
As the translator engines make use of differenct abbreviations for languages, for now there is a quick fix displaying all the language codes of the selected translation engine as the second query result.
