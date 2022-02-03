var imgCount = 0;
function changeImg(){
    mainImg = document.getElementById("mainImg");
    if(imgCount == 0){
        mainImg.src = "static/imgs/red_heart.png";
        imgCount += 1;
    }
    else if(imgCount == 1){
        mainImg.src = "static/imgs/clear_heart.png";
        imgCount += -1;
    }
}
