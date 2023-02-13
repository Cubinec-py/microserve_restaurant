let form = document.getElementById('form-payed')

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

let urla = document.getElementById('rating'); // Parent
urla.addEventListener('click', function (e) {
    let target = e.target;
    while (target && target.parentNode !== urla) {
        target = target.parentNode;
        if (!target) {
            return;
        }
    }
    if (target.tagName === 'I') {
        for (let i = 0; i < urla.children.length; i++) {
            if (i < [...urla.children].indexOf(e.target)) {
                urla.children[i].classList.remove('checked')
            } else {
                urla.children[i].classList.add('checked')
            }
        }
    }
});

document.getElementById('form-button-payed').addEventListener('click', function (e) {
    submitPayedData()
})


function submitPayedData() {
    tips = form.tips.value
    total = form.total_payment.value
    id_order = form.id_order.value
    rate_amount = $('.fa-star.checked').length


    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrf
        }
    })
    $.ajax({
        url: '/order/order_confirm/' + id_order,
        type: "POST",
        data: {'tips': tips, 'total': total, 'id_order': id_order, 'rate_amount': rate_amount},
        dataType: "json",
    })
        .then((data) => {
            console.log('Success:', data);

            cart = {}
            document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

            window.location.href = "/menu/"

        })
}