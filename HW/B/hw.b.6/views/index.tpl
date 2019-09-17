% include('header.html', title='Page Title')
<body>
<main>
    <div class='container'>
        % include('navbar.html')
        <div class="jumbotron">
            <h1 class="display-4">Музопоиск!</h1>
            <p class="lead">Здесь вы найдете информацию о альбомах записанных музыкальными группами.</p>
            <hr class="my-4">
            <p>В настоящее время доступна информация о следующих группах:</p>
            <ul class="list-group">
                % for artist in artists:
                <li class="list-group-item"><a text-decoration=None href='/albums/{{ artist }}'>{{ artist }}</a></li>
                % end
            </ul>
        </div>
    </div>
</main>
% include('footer.html')
</body>