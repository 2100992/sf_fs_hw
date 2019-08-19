from tags import HTML, TopLevelTag, Tag

with Tag('div', klass=("main-text", 'container')) as div:
    div.text = 'hello'
    div.attributes['class'] = 'h1'
    div.attributes['id'] = 'id_name'
print('div = ')
print(div)
print()

with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
    img.text = 'World'
    img.attributes['class'] = 'h2'
    img.attributes['id'] = 'id_name2'
print('img = ')
print(img)
print() 

print('div+img = ')
print(div+img)
print()
print('div += img')
div += img
print(div)
print()

with TopLevelTag("body") as body:
    with Tag("h1", klass=("main-text",)) as h1:
        h1.text = "Test"
        body += h1
    print()
    print(f'печатаем body внутри with - {body}')
    body.attributes['class'] = 'h1'

print()
print(f'печатаем body извне with - {body}')