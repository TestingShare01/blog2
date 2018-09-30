KindEditor.ready(function(K) {
        K.create('textarea[name=Article_content]', {
        //K.create('#id_article', {
            width: '800px',
            height: '400px',
            uploadJson:"/admin/upload/kindeditor",
        });
});
