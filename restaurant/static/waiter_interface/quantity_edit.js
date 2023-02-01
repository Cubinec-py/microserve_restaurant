$(document).ready(function () {
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

    const csrf = getCookie('csrftoken');
    $(".btn-remove").click(function (e) {
        quantity = e.target.id
        item_id = e.target.alt
        console.log(item_id)
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': csrf
            }
        });
        $.ajax({
            url: '/waiter/order_detail/' + item_id,
            type: "POST",
            data: {'item_id': item_id, 'quantity': parseInt(quantity) - 1},
            dataType: "json",
        });
        location.reload()
    })
    $(".btn-primary").click(function (e) {
        quantity = e.target.id
        item_id = e.target.alt
        console.log(item_id)
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': csrf
            }
        });
        $.ajax({
            url: '/waiter/order_detail/' + item_id,
            type: "POST",
            data: {'item_id': item_id, 'quantity': parseInt(quantity) + 1},
            dataType: "json",
        });
        location.reload()
    })
    $(".update-order-item").click(function (e) {
        // item_id = e.target.about
        order_id = e.target.value
        dish_id = e.target.id
        table_id = e.target.name
        console.log('order_id', order_id, 'dish_id', dish_id, 'table_id', table_id)
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': csrf
            }
        });
        $.ajax({
            url: '/waiter/order_detail/' + order_id,
            type: "POST",
            data: {'order_id': order_id, 'dish_id': dish_id, 'table_id': table_id},
            dataType: "json",
        });
        location.reload()
    })
})

let form = document.getElementById('form')

document.getElementById('form-button-status').addEventListener('click', function (e) {
    submitFormData()
})

function submitFormData() {
    const csrf = getCookie('csrftoken');
    status_order_id = form.order.value
    order_status = form.table.value
    console.log('order_status', order_status, 'status_order_id', status_order_id)
    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrf
        }
    });
    $.ajax({
        url: '/waiter/order_detail/' + status_order_id,
        type: "POST",
        data: {'status_order_id': status_order_id, 'order_status': order_status},
        dataType: "json",
    });
    location.reload()
}