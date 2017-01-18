<html>
	<head>
		<title>Lord of Pictures</title>	
	</head>
	<body>
        <h1>Playlists</h1>
        % for playlist in dirs:
            <li>{{playlist}}</li>
        % end
        <br>
        <p>Currently Active: {{active}}</p>
        <br>
		<form action="/upload" method="post" enctype="multipart/form-data">
			Select file: <input type="file" name="upload" />
			<input type="submit" value="Upload" />
		</form>
	</body>
</html>
