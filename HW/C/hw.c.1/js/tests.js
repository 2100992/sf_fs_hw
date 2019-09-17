const but1 = $('#but1')
const but2 = $('#but2')
const but3 = $('#but3')
const but4 = $('#but4')
const but = $('button')
const div = $('div')
const container = $('.container')
const h1 = $('h1')
const htmlTest = $('.htmlTest')

// but1.click(() => console.log('but1'))
//$('button').hide().show().click(e => console.log(e)).class('name')
but1.click(() => {
	but.class('btn btn-success');
	h1.text('btn-success')
	htmlTest.html('<h2>h2</h2>')
})
but2.click(() => {
	but.class('btn btn-danger');
	h1.text('btn-danger')
	htmlTest.html('<h3>h3</h3>')
})
but3.click(() => {
	but.class('btn btn-warning');
	h1.text('btn-warning')
	htmlTest.html('<h4>h4</h4>')
})
but4.click(() => {
	but.class('btn btn-primary');
	h1.text('btn-primary')
	htmlTest.html('<h5>h5</h5>')
})
