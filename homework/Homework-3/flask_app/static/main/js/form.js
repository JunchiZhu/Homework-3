var count = 0;

document.querySelector("#feedback").addEventListener("click",feedback);

function openFeedback() {
    count = 1;
    document.querySelector(".popup").classList.add("show");
}

function closeFeedback() {
    count = 0;
    document.querySelector(".popup").classList.remove("show");
}

function feedback(){
    if (count === 0){
        openFeedback();
    }
    else {
        closeFeedback();
    }

}