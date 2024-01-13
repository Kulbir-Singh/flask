function displayImage() {
  var input = document.getElementById("image");
  var image = document.getElementById("uploadedImage");
  var bgImage = document.getElementById("uploadedBGImage");
  let cancelBtn = document.getElementById("cancelButton");

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      image.src = e.target.result;
      bgImage.src = e.target.result;
      bgImage.style.opacity = "20%";
      bgImage.style.filter = "blur(10px)";
      cancelBtn.style.display = "inline";
    };
    cancelBtn.onclick = function () {
      image.src = "/static/placeholder.svg";
      bgImage.src = "";
      cancelBtn.style.display = "none";
    };
    reader.readAsDataURL(input.files[0]);
  }
}
