


let uri = '{{ request.get_full_path }}'
const urls = document.querySelectorAll('.url');
urls.forEach(function(p){
    if(p.getAttribute('href')==uri){
        $(p).addClass('active')
        console.log(p)
    }
})