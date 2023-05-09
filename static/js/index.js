window.onload = function() {
    document.querySelector('#header h2').addEventListener('animationend', function() {
      document.querySelector('.img-its-me').style.display = 'block';
    });
};
  