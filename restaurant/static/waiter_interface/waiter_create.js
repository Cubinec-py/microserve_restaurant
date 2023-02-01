let form = document.getElementById('form-waiter')

document.getElementById('form-button-waiter').addEventListener('click', function (e) {
    submitFormData()
})

function submitFormData() {
    const csrf = getCookie('csrftoken');
    waiter_id = form.table.value
    order_id = form.order.value
    console.log('waiter_id', waiter_id, 'order_id', order_id)
    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrf
        }
    });
    $.ajax({
        url: '/waiter/',
        type: "POST",
        data: {'waiter_id': waiter_id, 'order_id': order_id},
        dataType: "json",
    });
    // location.reload()
}