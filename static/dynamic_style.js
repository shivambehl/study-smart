#autoresizing {
            display: block;
            overflow: hidden;
            resize: none;
}
textarea = document.querySelector("#autoresizing");
textarea.addEventListener('input', autoResize, false);

function autoResize() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
}