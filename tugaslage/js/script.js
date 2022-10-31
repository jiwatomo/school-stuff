const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
const popoverList = [...popoverTriggerList].map((popoverTriggerEl) => new bootstrap.Popover(popoverTriggerEl));
$(document).ready(function () {
  if (!$.browser.webkit) {
    $(".wrapper").html("<p>Sorry! Non webkit users. :(</p>");
  }
});
