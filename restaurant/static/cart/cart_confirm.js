let form = document.getElementById('form')

form.addEventListener('submit', function (e) {
    e.preventDefault()
    console.log('Form Submitted...')
    document.getElementById('form-button').classList.add("hidden");
})

document.getElementById('form-button').addEventListener('click', function (e) {
    submitFormData()
})

function submitFormData() {

    let userFormData = {
        'first_name': form.first_name.value,
        'last_name': form.last_name.value,
    }
    console.log('first_name', form.first_name.value)
    let table = {
        'table_id': form.table.value,
    }

    const csrftoken = getCookie('csrftoken');
    let url = "/cart/cart_apply/"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'applicaiton/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'form': userFormData, 'table': table}),

    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data);
        alert('Заказ успешно подтвержден');

        cart = {'first_name': form.first_name.value, 'last_name': form.last_name.value}
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

        window.location.href = "/menu/"

    })
}