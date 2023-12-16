document.addEventListener("DOMContentLoaded", function(){
    window.addEventListener('scroll', function(){
        if (this.window.scrollY > 50) {
            this.document.getElementById('navbar_top').classList.add('fixed-top');
            // add pading top to show content navbar
            navbar_height = this.document.querySelector('.navbar').offsetHeight;
            this.document.body.style.paddingTop = navbar_height + 'px';
        } else {
            document.getElementById('navbar_top').classList.remove('fixed-top');
            this.document.body.style.paddingTop = '0'
        }
    })
})