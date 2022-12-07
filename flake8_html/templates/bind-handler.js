function bindHandler(link) {
    var code = link.getAttribute('data-code');
    var key = location.pathname + '#' + code;

    var ul = link.parentNode.querySelector('.details');
    if (sessionStorage[key] != 'open') {
        ul.style.display = 'none';
    }
    link.addEventListener('click', function(event) {
        if (!ul.style.display || ul.style.display == 'none') {
            ul.style.display = 'block';
            sessionStorage[key] = 'open';
        } else {
            ul.style.display = 'none';
            sessionStorage[key] = 'closed';
        }
    });
}

window.addEventListener('DOMContentLoaded', function() {
    var links = document.querySelectorAll('.file-report > #index > li > a');
    for (var i = 0; i < links.length; i++) {
        bindHandler(links[i]);
    }
});
