function jQuery (selector, context = document){
	this.elements = Array.from(context.querySelectorAll(selector));
	return this
}

jQuery.prototype.each = function (fn){
	this.elements.forEach((element, index) => fn.call(element, element, index));
	return this;
}

jQuery.prototype.click = function(fn){
	this.each(element => element.addEventListener('click', fn))
	return this
}

jQuery.prototype.hide = function(){
	this.each(element => element.style.display = 'none')
  return this;
}

jQuery.prototype.show = function(){
	this.each(element => element.style.display = '')
  return this;
}

jQuery.prototype.remove = function(){
	this.each(element => element.remove())
  return this;
}

jQuery.prototype.class = function(name){
	this.each(element => element.className = name)
  return this;
}

jQuery.prototype.html = function(newHTML = undefined){
    if (newHTML === undefined) {
        this.html = Array.from(this.each(element => element.innerHTML))
        console.log(this.html)
    }
    else{
        this.each(element => element.innerHTML = newHTML)
    }
    return this
}

jQuery.prototype.text = function(newText = undefined){
    this.each(element => element.text(newText))
}


const $ = (e) => new jQuery(e);



const but1 = $('#but1')
const but2 = $('#but1')
const but3 = $('#but1')
const but4 = $('#but1')
const but = $('button')
const div = $('div')

// but1.click(() => console.log('but1'))

$('button').hide().show().click(e => console.log(e)).class('name')


