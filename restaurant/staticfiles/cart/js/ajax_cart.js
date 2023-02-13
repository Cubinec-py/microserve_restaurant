$(document).ready(function () {
    console.log('some_value', JSON.parse(localStorage.getItem("cart")))
    let compare = localStorage.getItem("cart");

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

    const csrftoken = getCookie('csrftoken');
    console.log('csrftoken', csrftoken)
    $.ajax({
        url: '/cart',
        type: "GET",
        data: {'cart': compare},
        dataType: "json",
    });
    if (localStorage.getItem("cart") != null) {
        let update_btns = document.getElementsByClassName('btn-primary');
        let items = JSON.parse(localStorage.getItem("cart"));
        let lst = []
        let quant = 0
        for (let i = 0; i < update_btns.length; i++) {
            let idx = update_btns[i]['id']
            if (items[idx] !== undefined) {
                lst.push(items[idx])
                quant += items[idx]['quantity']
            }
            for (let j = 0; j < lst.length; j++) {
                cart = items;
                setBadge();
            }
        }
    }

    $(".btn-primary").click(function (e) {
        console.log(e.target)
        setLocalStorage(e.target.id, 0);
        setBadge();
    });

    $(".btn-danger").on('click', function () {
        removeItem($(this).parent("li"));
        setLocalStorage($(this).data('id'), 1);
    });
});

function removeItem(item) {
    console.log(item);
    let id = item[0].attributes[1].value;
    $(`#${id}`).removeClass("btn-warning");
    item.remove();
    setBadge();
}

function setBadge() {
    let quant = 0
    if (localStorage.getItem("cart") != null) {
        let update_btns = document.getElementsByClassName('btn-primary');
        let items = JSON.parse(localStorage.getItem("cart"));
        for (let i = 0; i < update_btns.length; i++) {
            let idx = update_btns[i]['id']
            if (items[idx] !== undefined) {
                quant += items[idx]['quantity']
            }
        }
    }
    $(".badge").remove();
    $("h3").after("<span class='badge'>" + quant + "</span>");
}

let cart = {};

function setLocalStorage(id, flag) {
    if (flag) {
        cart.items.splice(cart.items.indexOf(id), 1);
    } else {
        if (cart[id]) {
            cart[id]['quantity'] += 1
        } else {
            cart[id] = {'quantity': 1}
        }
    }
    console.log(JSON.stringify(cart));
    localStorage.setItem("cart", JSON.stringify(cart));
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

    // let compare = localStorage.getItem("cart");
    //
    // function getCookie(name) {
    //     let cookieValue = null;
    //     if (document.cookie && document.cookie !== '') {
    //         const cookies = document.cookie.split(';');
    //         for (let i = 0; i < cookies.length; i++) {
    //             const cookie = cookies[i].trim();
    //             // Does this cookie string begin with the name we want?
    //             if (cookie.substring(0, name.length + 1) === (name + '=')) {
    //                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    //                 break;
    //             }
    //         }
    //     }
    //     return cookieValue;
    // }
    //
    // const csrftoken = getCookie('csrftoken');
    // console.log('csrftoken', csrftoken)
    // $.ajax({
    //     url: '/cart',
    //     type: "GET",
    //     data: {'cart': compare},
    //     dataType: "json",
    // });
}
