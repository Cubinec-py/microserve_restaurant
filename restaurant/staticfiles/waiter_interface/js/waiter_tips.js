$(document).on("click", ".open-tips", function (e) {
    e.preventDefault();
    let $popup = $("#tips");
    let popup_url = $(this).data("popup-url");
    console.log(popup_url)
    $(".modal-body", $popup).load(popup_url, function () {
        $popup.modal("show");
    });
});