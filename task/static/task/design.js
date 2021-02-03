function checks(a,b){
    var id_number = parseInt(b); /* バツボタン */
    var value = String(a);       /* 列番号 */
    const string_yet = 'yet';
    const string_ing = 'doing';
    const string_ed = 'done';
    var id_name = 'str' + value;  /* idの値 */
       
    
    if(id_number == 1){
        /* 要素のテキスト取得 */
        var status = document.getElementById(id_name).innerHTML; 

        if (status == 'yet') {
            document.getElementById(id_name).innerHTML = string_ing;   
        }
        else if(status == 'doing') {
            document.getElementById(id_name).innerHTML = string_yet;   
        }  
    }

    else if(id_number == 2){
        document.getElementById(id_name).innerHTML = string_ed;
    }
}


