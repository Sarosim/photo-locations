(function() {

    
    var pictures = document.getElementsByClassName("postcard-link");
    var thisPicture;
    var picture;

/*bluring the pictures that are not in focus on the landing page*/
    function blurAllTheOthers(element) {
        for (var i = 0; i < pictures.length; i++) {
            picture = pictures[i];
            $(picture).addClass("postcard-image-blur");
        }
        $(element).removeClass("postcard-image-blur");
    }
    
    function unBlur(){
        for (var i = 0; i < pictures.length; i++) {
            picture = pictures[i];
            $(picture).removeClass("postcard-image-blur");
        }
    }


    $(".postcard-link").mouseover(function(){
        console.log("event fired");
        thisPicture = $(this);
        blurAllTheOthers(thisPicture);
    });
    
    $(".postcard-image").mouseout(function(){
        unBlur();
    });

/*end of IIFE*/
})();
