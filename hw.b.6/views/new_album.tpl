% include('header.html', title='Page Title')
<body>
<main>
    <div class='container'>
        % include('navbar.html')
        <div class="jumbotron">
            <h1 class="display-4">Давайте добавим новый альбом!</h1>
            <ul class="list-group">
            <form method="post">
              <div class="form-group">
                <label for="var1">Артист</label>
                <input type="text" class="form-control" id="var1" placeholder="Артист">
              </div>
              <div class="form-group">
                <label for="var2">Альбом</label>
                <input type="text" class="form-control" id="var2" placeholder="Альбом">
              </div>
              <div class="form-group">
                <label for="var3">Жанр</label>
                <input type="text" class="form-control" id="var3" placeholder="Жанр">
              </div>
              <div class="form-group">
                <label for="var4">Год</label>
                <input type="text" class="form-control" id="var4" placeholder="Год">
              </div>    
              <button type="button" class="btn btn-primary" data-toggle="modal" data-target=".modal">Создать</button>
            </form>
        </div>
    </div>
</main>
% include('footer.html')
</body>


