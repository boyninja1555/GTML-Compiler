import re

class gtml_parser:
    def __init__(self, gtml):
        self.gtml = gtml
        self.parsed_data = {}

    def parse(self):
        self.parsed_data["settings"] = self._parse_block("settings")
        self.parsed_data["main"] = self._parse_block("main")

    def _parse_block(self, block_name):
        pattern = re.compile(rf"\{{{block_name}\}}(.*?)\{{END:{block_name}\}}", re.DOTALL)
        block_content = pattern.search(self.gtml)
        if not block_content:
            return {}
        block_content = block_content.group(1).strip()
        return self._parse_elements(block_content)

    def _parse_elements(self, content):
        elements = {}
        pattern = re.compile(r"\{(\w+)([^}]*)\}(.*?)\{END:\1\}", re.DOTALL)
        for match in pattern.finditer(content):
            tag, attributes, inner_text = match.groups()
            if tag not in elements:
                elements[tag] = []
            elements[tag].append({"attributes": self._parse_attributes(attributes), "content": inner_text.strip()})
        return elements

    def _parse_attributes(self, attribute_string):
        attributes = {}
        pattern = re.compile(r'(\w+)="(.*?)"')
        for match in pattern.finditer(attribute_string):
            attr_name, attr_value = match.groups()
            attributes[attr_name] = attr_value
        return attributes

    def get_parsed_data(self):
        return self.parsed_data

    def compile_to_html(self, elements=None):
        if elements is None:
            elements = self.parsed_data

        html = []

        settings = elements.get("settings", {})
        main = elements.get("main", {})

        lang_attr = settings.get("lang", [{}])[0].get("attributes", {}).get("lang", "")

        html.append("<!DOCTYPE html>")
        html.append(f'<html lang="{lang_attr}">')

        html.append("<head>")
        if "page_title" in settings:
            for title in settings["page_title"]:
                html.append(f"    <title>{title['content']}</title>")
        if "page_icon" in settings:
            for icon in settings["page_icon"]:
                pageIconUrl = icon["attributes"].get("url", "")
                html.append(f'    <link rel="icon" href="{pageIconUrl}" />')
        if "cssfile" in settings:
            for cssfile in settings["cssfile"]:
                cssfileUrl = cssfile["attributes"].get("url", "")
                html.append(f'    <link rel="stylesheet" href="{cssfileUrl}" />')
        html.append("</head>")

        html.append("<body>")
        if "heading" in main:
            for heading in main["heading"]:
                html.append(f"    <h1>{heading['content']}</h1>")
        if "text" in main:
            for text in main["text"]:
                html.append(f"    <p>{text['content']}</p>")
        if "hyperlink" in main:
            for link in main["hyperlink"]:
                html.append(f'    <a href="{link["attributes"]["url"]}">{link["content"]}</a>')
        if "button" in main:
            for button in main["button"]:
                html.append(f'    <button onclick="{button["attributes"]["onclick"]}">{button["content"]}</button>')
        if "box" in main:
            for box in main["box"]:
                boxClass = box["attributes"].get("class", "")
                html.append(f'    <div class="{boxClass}">')
                html.append(self.compile_to_html({"main": self._parse_elements(box["content"])}))
                html.append(f'    </div>')
        if "script" in main:
            for script in main["script"]:
                scriptUrl = script["attributes"].get("url", "")
                if scriptUrl != "":
                    html.append(f'    <script src="{scriptUrl}"></script>')
                else:
                    html.append(f'    <script>{script["content"]}</script>')
        html.append("</body>")

        html.append("</html>")
        html.append("")

        return "\n".join(html)