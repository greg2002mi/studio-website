document.addEventListener("DOMContentLoaded", function() {
    const videoThumbnails = document.querySelectorAll(".video-thumbnail");

    videoThumbnails.forEach(thumbnail => {
        const video = thumbnail.querySelector("video");
        video.addEventListener("loadeddata", () => {
            thumbnail.classList.add("loaded");
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const videoThumbnails = document.querySelectorAll(".video-thumbnail");
    const modal = document.getElementById("videoModal");
    const modalVideo = document.getElementById("modalVideo");
    const modalVideoSource = document.getElementById("modalVideoSource");
    const closeBtn = document.getElementsByClassName("close")[0];

    function adjustModalVideoHeight() {
        const windowHeight = window.innerHeight;
        const maxVideoHeight = windowHeight * 0.8; // 80% of the window height
        modalVideo.style.height = maxVideoHeight + 'px';
        modalVideo.style.width = 'auto'; // Maintain aspect ratio
    }

    // Adjust the video height when the window is resized
    window.onresize = adjustModalVideoHeight;

    // When a video thumbnail is clicked
    videoThumbnails.forEach(thumbnail => {
        thumbnail.addEventListener("click", function() {
            const videoSrc = this.getAttribute("data-video");
            modalVideoSource.src = videoSrc;
            modalVideo.load();
            modal.style.display = "flex";
            modalVideo.play();
            adjustModalVideoHeight(); // Adjust the height when the modal is shown
        });
    });

    // When the close button is clicked
    closeBtn.onclick = function() {
        modal.style.display = "none";
        modalVideo.pause();
        modalVideo.currentTime = 0; // Reset the video to start
    }

    // When anywhere outside of the modal is clicked
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            modalVideo.pause();
            modalVideo.currentTime = 0; // Reset the video to start
        }
    }
});