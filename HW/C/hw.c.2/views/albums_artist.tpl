% include('header.html', title='Page Title')
<body>
<main>
    <div class='container'>
        % include('navbar.html')
        <div class="jumbotron">
            <h1 class="display-4">{{ message }}</h1>
            <ul class="list-group">
                % for album_name in album_names:
                <li class="list-group-item">{{ album_name }}</li>
                % end
            </ul>
        </div>
    </div>
</main>
% include('footer.html')
</body>


