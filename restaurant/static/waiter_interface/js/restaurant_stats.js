$(document).on("click", ".open-restaurant-stats", function (e) {
    e.preventDefault();
    let $popup = $("#restaurant");
    let popup_url = $(this).data("popup-url");
    console.log(popup_url)
    $(".modal-body", $popup).load(popup_url, function () {
        $popup.modal("show");
    });
});