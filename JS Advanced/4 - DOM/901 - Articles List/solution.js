function createArticle() {
	
	let titleElement = document.getElementById('createTitle');
	let contentElement = document.getElementById('createContent');

	let headingElement = document.createElement('h3');
	headingElement.innerHTML = titleElement.value;	

	let pElement = document.createElement('p');
	pElement.innerHTML = contentElement.value;

	let articleElement = document.createElement('article');
	articleElement.appendChild(headingElement);
	articleElement.appendChild(pElement);

	let articleSectionElement = document.getElementById('articles');
	articleSectionElement.appendChild(articleElement);
}
