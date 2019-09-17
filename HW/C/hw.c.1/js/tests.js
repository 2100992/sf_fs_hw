function smallQuery (element) {
	return document.querySelector(element);
}


smallQuery.prototype.all = function (elements) {
	return document.querySelectorAll(elements);
}