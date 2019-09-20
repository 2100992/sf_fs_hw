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

//функция читает или записывает HTML содержимое объекта
//работает для первого элемента из группы
jQuery.prototype.html = function(newHTML = undefined){
    if (newHTML === undefined) {
        return this.elements[0].innerHTML;
    }
    else{
        this.each(element => element.innerHTML = newHTML)
    }
}

//функция читает или записывает текстовое содержимое объекта
//работает для первого элемента из группы
jQuery.prototype.text = function(newText = undefined){
  if (newText === undefined) {
      return this.elements[0].innerText;
  }
  else{
      this.each(element => element.innerText = newText)
  }
}

//функция вычисляет геометрический центр объекта
//работает для первого элемента из группы
jQuery.prototype.middle = function(){
  let box = this.elements[0].getBoundingClientRect();
  return {
    x: box.left + box.width/2,
    y: box.top + box.height/2
  }
}

const $ = (e) => new jQuery(e);



