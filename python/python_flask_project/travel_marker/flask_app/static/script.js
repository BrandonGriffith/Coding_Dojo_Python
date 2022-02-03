function changeImg(){
    var imgCount = 0;
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
