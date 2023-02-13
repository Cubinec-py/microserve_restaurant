let updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		let product_id = this.dataset.product
		let action = this.dataset.action
		console.log('product_id:', product_id, 'Action:', action)
		addCookieItem(product_id, action)
	})
}

function addCookieItem(product_id, action){
	console.log('User is not authenticated')
	console.log('action', action)
	console.log('cart', cart)
	if (action === 'add'){
		if (cart[product_id] == undefined){
			cart[product_id] = {'quantity':1}

		} else {
			cart[product_id]['quantity'] += 1
		}
	}

	if (action === 'remove'){
		cart[product_id]['quantity'] -= 1

		if (cart[product_id]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[product_id];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload()
}