let form = document.getElementById('form-payed')

document.getElementById('form-button-payed').addEventListener('click', function (e) {
    submitPayedData()
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const csrf = getCookie('csrftoken')

function submitPayedData() {
    tips = form.tips.value
    total = form.total_payment.value
    id_order = form.id_order.value

    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrf
        }
    })
    $.ajax({
        url: '/order/order_confirm/' + id_order,
        type: "POST",
        data: {'tips': tips, 'total': total, 'id_order': id_order},
        dataType: "json",
    })
    .then((data) => {
        console.log('Success:', data);

        cart = {}
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

        window.location.href = "/menu/"

    })
}