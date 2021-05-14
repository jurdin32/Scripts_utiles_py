var QueryString = function () {
    var query_string = {};
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (typeof query_string[pair[0]] === "undefined") {
            query_string[pair[0]] = decodeURIComponent(pair[1]);
        } else if (typeof query_string[pair[0]] === "string") {
            var arr = [query_string[pair[0]], decodeURIComponent(pair[1])];
            query_string[pair[0]] = arr;
        } else {
            query_string[pair[0]].push(decodeURIComponent(pair[1]));
        }
    }
    return query_string;
}();

function url(nombre, valor) {
    let uri = `${nombre}=${valor}`
    for (const property in QueryString) {
        if (property == nombre) {
            console.log("existe")
        } else {
            if (QueryString[property] != "") {
                uri += `&${property}=${QueryString[property]}`
            }
        }
        console.log(uri)
    }
    location.href = "?" + uri
}