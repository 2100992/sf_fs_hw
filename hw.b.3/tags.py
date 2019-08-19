class Tag:
    def __init__(self, *args, is_single = False, **kwargs):
        self.tag = args[0]
        self.text = ''
        self.is_single = is_single
        self.attributes = kwargs
        self.result = ''

    def __enter__(self, *args, **kwargs):
        return self

    def __exit__(self, *args, **kwargs):
        return self

    #Немного модифицируем аттрибуты экземпляра, а именно:
    # - в случае если klass - кортеж, сольем его воедино через пробел
    # - аттрибуты class и klass сольем воедино через пробел
    # - поменяем все '_' на '-'
    def __get_attr(self):
        attributes = []
        if self.attributes.get('klass') is not None:
            if isinstance(self.attributes['klass'], tuple):
                self.attributes['klass'] = ' '.join(self.attributes['klass'])
            self.attributes['class'] = self.attributes.pop('klass') + (' ' + str(self.attributes.get('class','')))
        for attr, value in self.attributes.items():
            if '_' in value:
                value = value.replace('_', "-")   # Тут нужно на всякий случай поменять _ на - 
            attributes.append(f'{attr}="{value}"')
        return attributes

    def __get_str(self): 
        attributes = self.__get_attr()
        if self.is_single:
            return f'<{str(self.tag)} {" ".join(attributes)} />'
        else:
            return f'<{str(self.tag)} {" ".join(attributes)}>{self.text}</{str(self.tag)}>'
    
    def __str__(self):
        self.result = self.__get_str()
        return self.result

    def __add__(self, other):
        self.result = f'{self.__get_str()}\n{other}'
        return self.result



class TopLevelTag(Tag):
    def __iadd__(self, other):
        attributes = self.__get_attr()
        self.result = f'<{str(self.tag)} {" ".join(attributes)}>{self.text}\n{other}</{str(self.tag)}>'
       # return self.result




class HTML(Tag):
    def __init__(self, *args, output = False, **kwargs):
        self.tag = {'internal':'<html>', 'ending':'</html>'}
        self.output = output
        self.text = ''
    
    def __exit__(self, *args, **kwargs):
        if self.output:
            params = {}
            params["file"] = self.output
            params["mode"] = "w"
            params["encoding"] = "utf-8"
            with open(self.output) as fp:
                print(self, file=fp)

    def __add__(self, other):
        attributes = self.__get_attr()
        return f'<{str(self.tag)} {" ".join(attributes)}>{self.text}\n{other}</{str(self.tag)}>'