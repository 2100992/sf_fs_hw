% include('header.html', title='Page Title')
<body>
<main>
    <div class='container'>
        % include('navbar.html')
        <div class="jumbotron">
            <h1 class="display-4">Давайте добавим новый альбом!</h1>
            <ul class="list-group">
            <form action="/albums" method="POST">
              <div class="form-group">
                <label for="artist">Артист</label>
                <input type="text" class="form-control" name="artist" id="artist" placeholder="Артист">
              </div>
              <div class="form-group">
                <label for="album">Альбом</label>
                <input type="text" class="form-control" name="album" id="album" placeholder="Альбом">
              </div>
              <div class="form-group">
                <label for="genre">Жанр</label>
                <input type="text" class="form-control" name="genre" id="genre" placeholder="Жанр">
              </div>
              <div class="form-group">
                <label for="year">Год</label>
                <input type="text" class="form-control" name="year" id="year" placeholder="Год">
              </div>    
              <button type="submit" class="btn btn-primary">Создать</button>
            </form>
        </div>
    </div>
</main>
% include('footer.html')
</body>


