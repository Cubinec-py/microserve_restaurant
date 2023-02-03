$(document).on("click", ".open-incident", function (e) {
    e.preventDefault();
    let $popup = $("#popup");
    let popup_url = $(this).data("popup-url");
    console.log(popup_url)
    $(".modal-body", $popup).load(popup_url, function () {
        $popup.modal("show");
    });
});