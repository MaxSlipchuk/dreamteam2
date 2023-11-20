const buttons = document.querySelectorAll(".btn-buy");

buttons.forEach((button) => {
  const video = button.querySelector(".video");

  function startPreview() {
    video.muted = true;
    video.currentTime = 1;
    video.play();
  }

  function stopPreview() {
    video.currentTime = 0;
    video.playbackRate = 1;
    video.pause();
  }

  button.addEventListener("mouseenter", () => {
    startPreview();
  });

  button.addEventListener("mouseleave", () => {
    stopPreview();
  });

  video.addEventListener("ended", () => {
    stopPreview();
  });
});