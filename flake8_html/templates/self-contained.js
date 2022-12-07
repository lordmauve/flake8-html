function hideAllPages() {
    for (const s of document.getElementsByClassName("page")) {
        s.style.display = "none";
    }
}

function changePageSev(sev = null) {
    var head = document.getElementById('masthead');
    if (sev === null) {
        sev = head.dataset['sev'];
    }
    head.className = 'sev-' + sev;
}

function switchToPage(pageId, highestSev = null) {
    hideAllPages();
    changePageSev(highestSev);
    var htmlShow = document.getElementById(pageId);
    if (htmlShow.style.display === "none") {
        htmlShow.style.display = "block";
    } else {
        htmlShow.style.display = "none";
    }
}

window.addEventListener('DOMContentLoaded', function() {
    hideAllPages();
    switchToPage('index-page');
});
