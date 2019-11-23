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
    
    
    /* Require PASSWORD for delting a record on the confirmation modal */
    var conf = document.getElementById('confirm');
    var delBtn = document.getElementById(('delete-btn'));
    
    conf.addEventListener("input", function(){
        console.log(conf.value)
        if (conf.value == "Delete") {  
            delBtn.removeAttribute("disabled");
            delBtn.setAttribute('href', "{{url_for('delete_record', record_id = record._id)}}");
        } else {
            delBtn.removeAttribute("href");
            delBtn.setAttribute("disabled");
        }    
    });
        

/*end of IIFE*/
})();
