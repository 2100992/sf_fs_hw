from tags import HTML, TopLevelTag, Tag

dif = Tag('dif', klass=("main-text", 'container'))
dif.attributes['class'] = 'h3'
dif.text = 'diftext'

print(f'dif = {dif}')
print()

with Tag('div', klass=("main-text", 'container')) as div:
    div.text = 'hello'
    div.attributes['class'] = 'h1'
    div.attributes['id'] = 'id_name'
    print(f'div внутри with = {div}')
print(f'div = {div}')
print()

with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
    img.text = 'World'
    img.attributes['class'] = 'h2'
    img.attributes['id'] = 'id_name2'
print(f'img = {img}')
print() 

print(f'div+img = {div+img}')
print()
print('div += img')
div += img
print(div)
print()

with Tag("body") as body:
    with Tag("h1", klass=("main-text",)) as h1:
        h1.text = "Test"
        print(f'body внутри р1 = {body}')
        body += h1
    
    print()
    print(f'body после p1 внутри with - {body}')
    body.attributes['class'] = 'h1'

print()
print(f'печатаем body извне with - {body}')

with HTML('html') as html:
    with TopLevelTag("head") as head:
        with Tag("title") as title:
            title.text = "hello"
            head += title
        html +=head
print(f'html = \n{html}')